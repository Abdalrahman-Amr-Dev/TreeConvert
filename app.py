import os
import sys
import threading
import time
from pathlib import Path
from flask import Flask, render_template, jsonify, request
from PIL import Image

app = Flask(__name__)

# Shared state for conversion
conversion_state = {
    "running": False,
    "progress": 0,
    "log": [],
    "total": 0,
    "current": 0,
    "done": False,
}

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/status")
def api_status():
    return jsonify({
        "running": conversion_state["running"],
        "progress": conversion_state["progress"],
        "total": conversion_state["total"],
        "current": conversion_state["current"],
        "done": conversion_state["done"],
    })


@app.route("/api/log")
def api_log():
    return jsonify({"log": conversion_state["log"]})


@app.route("/api/convert", methods=["POST"])
def api_convert():
    if conversion_state["running"]:
        return jsonify({"error": "Conversion already running"}), 409

    data = request.json
    src = data.get("src", "")
    dst = data.get("dst", "")
    quality = int(data.get("quality", 93))
    selected_format = data.get("format", "AVIF")

    if not src or not dst:
        return jsonify({"error": "Please select both source and destination folders."}), 400

    src_path = Path(src)
    dst_path = Path(dst)

    if not src_path.exists():
        return jsonify({"error": "Source folder does not exist."}), 400
    if not dst_path.exists():
        return jsonify({"error": "Destination folder does not exist."}), 400

    thread = threading.Thread(
        target=run_conversion,
        args=(src, dst, quality, selected_format),
        daemon=True,
    )
    thread.start()
    return jsonify({"status": "started"})


@app.route("/api/reset", methods=["POST"])
def api_reset():
    conversion_state["done"] = False
    conversion_state["progress"] = 0
    conversion_state["log"] = []
    conversion_state["current"] = 0
    conversion_state["total"] = 0
    return jsonify({"status": "reset"})


def run_conversion(src, dst, quality, selected_format):
    conversion_state["running"] = True
    conversion_state["progress"] = 0
    conversion_state["log"] = []
    conversion_state["current"] = 0
    conversion_state["done"] = False

    format_settings = {
        "AVIF": {"ext": ".avif", "pil": "AVIF"},
        "WebP": {"ext": ".webp", "pil": "WEBP"},
        "JPEG": {"ext": ".jpg", "pil": "JPEG"},
        "PNG": {"ext": ".png", "pil": "PNG"},
    }

    target_ext = format_settings[selected_format]["ext"]
    target_pil = format_settings[selected_format]["pil"]

    src_path = Path(src)
    dst_path = Path(dst)
    input_extensions = {".png", ".webp", ".jpg", ".jpeg", ".bmp", ".tiff", ".avif"}

    files = [f for f in src_path.rglob("*") if f.suffix.lower() in input_extensions]

    if not files:
        conversion_state["log"].append("No supported images found.")
        conversion_state["running"] = False
        conversion_state["done"] = True
        return

    conversion_state["total"] = len(files)

    for i, file_path in enumerate(files):
        try:
            relative_path = file_path.relative_to(src_path)
            output_file_path = dst_path.joinpath(relative_path).with_suffix(target_ext)
            output_file_path.parent.mkdir(parents=True, exist_ok=True)

            with Image.open(file_path) as img:
                if target_pil in ["JPEG", "AVIF"] and img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                save_kwargs = {"format": target_pil}

                exif_data = img.info.get("exif")
                if exif_data is not None:
                    save_kwargs["exif"] = exif_data

                if target_pil != "PNG":
                    save_kwargs["quality"] = quality

                if target_pil == "AVIF":
                    save_kwargs["speed"] = 6

                img.save(output_file_path, **save_kwargs)

            conversion_state["log"].append(f"Success: {file_path.name}")
        except Exception as e:
            conversion_state["log"].append(f"Failed {file_path.name}: {str(e)}")

        conversion_state["current"] = i + 1
        conversion_state["progress"] = (i + 1) / len(files)

    conversion_state["running"] = False
    conversion_state["done"] = True
    conversion_state["log"].append(f"Done! Converted to {selected_format}.")
