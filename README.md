# 🌳 TreeConvert

<div align="center">

**A fast, lightweight, open-source desktop image converter.**

Convert entire folders between **AVIF, WebP, JPEG, and PNG** while preserving your folder structure and image metadata.

<br>

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-555?style=for-the-badge)](#)
[![Formats](https://img.shields.io/badge/Formats-AVIF%20%7C%20WebP%20%7C%20JPEG%20%7C%20PNG-6C63FF?style=for-the-badge)](#supported-formats)
[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-success?style=for-the-badge)](#license)

</div>

---

## 📖 About

**TreeConvert** is a free and open-source desktop application for **batch image conversion**.

Instead of converting images one by one, simply select a folder and TreeConvert will recursively process all supported images — including images inside nested directories.

Your original folder structure is automatically recreated in the output directory.

> **Select → Configure → Convert → Done.**

---

## ✨ Features

* 📂 **Batch Conversion** — Convert entire folders in a single operation
* 🌳 **Recursive Processing** — Automatically process nested subfolders
* 🖼️ **Multiple Formats** — AVIF, WebP, JPEG, and PNG
* 🎚️ **Quality Control** — Adjustable quality from `10` to `100`
* 🧾 **EXIF Preservation** — Preserve image metadata when supported
* 🔲 **Transparency Handling** — Properly handle RGBA images when converting to formats such as JPEG
* 🗂️ **Structure Preservation** — Keep the original directory hierarchy
* 📊 **Live Progress** — Monitor conversion progress in real time
* 📝 **Per-file Logging** — See the status of every processed image
* 💻 **Cross-platform** — Windows, macOS, and Linux

---

## 🖼️ Supported Formats

|  Format  | Output | Transparency | Recommended For                  |
| :------: | :----: | :----------: | :------------------------------- |
| **AVIF** |    ✅   |       ✅      | Modern web & maximum compression |
| **WebP** |    ✅   |       ✅      | Web images & general use         |
| **JPEG** |    ✅   |       ❌      | Photos & compatibility           |
|  **PNG** |    ✅   |       ✅      | Lossless images                  |

---

## 🌲 Directory Structure

TreeConvert preserves your folder hierarchy during conversion.

### Before

```text
photos/
├── image-01.jpg
├── image-02.png
│
├── vacation/
│   ├── beach.jpg
│   └── hotel.png
│
└── family/
    └── photo.jpg
```

### After

```text
converted/
├── image-01.webp
├── image-02.webp
│
├── vacation/
│   ├── beach.webp
│   └── hotel.webp
│
└── family/
    └── photo.webp
```

No manually recreating folders.
No flattened output directory.

**Your image library stays organized.**

---

## ⚡ Quick Start

### Requirements

* Python `3.11+`
* [Flask](https://flask.palletsprojects.com/)
* [pywebview](https://pywebview.flowrl.com/)
* [Pillow](https://python-pillow.org/)

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/TreeConvert.git
cd TreeConvert
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## 🚀 Usage

### 1. Select the source folder

Click **Browse** next to `Source Folder` and select the folder containing your images.

### 2. Select the destination

Choose where TreeConvert should save the converted images using `Save Folder`.

### 3. Choose the output format

Select one of:

```text
AVIF
WebP
JPEG
PNG
```

### 4. Adjust quality

Use the quality slider to select a value between:

```text
10 ─────────────────────────────── 100
Low                              High
```

### 5. Start conversion

Click **Start Conversion** and let TreeConvert handle the rest.

The application will recursively scan your source folder and preserve its directory structure in the destination.

---

## 🔐 Local & Private

TreeConvert is designed as a **local desktop application**.

Your images don't need to be uploaded to a server or processed through a third-party web service.

> 🔒 **Your files stay on your machine.**

---

## 🛠️ Built With

| Technology           | Purpose                      |
| :------------------- | :--------------------------- |
| 🐍 **Python**        | Core application             |
| 🌐 **Flask**         | Web server backend           |
| 🖥️ **pywebview**    | Native desktop window        |
| 🖼️ **Pillow**       | Image processing             |
| 📦 **PyInstaller**   | Standalone executable builds |

---

## 📦 Project Structure

```text
TreeConvert/
├── main.py
├── app.py
├── templates/
│   └── index.html
├── main.spec
├── convert.ico
├── convert.png
├── requirements.txt
└── README.md
```

| File               | Description                                        |
| :----------------- | :------------------------------------------------─ |
| `main.py`          | Application entry point, pywebview launcher         |
| `app.py`           | Flask backend, API routes, and conversion logic     |
| `templates/`       | HTML/CSS/JS frontend                               |
| `main.spec`        | PyInstaller configuration                          |
| `convert.ico`      | Windows application icon                           |
| `convert.png`      | macOS/Linux application icon                       |
| `requirements.txt` | Python dependencies                                |
| `README.md`        | Project documentation                              |

---

## 🪟 Build for Windows

TreeConvert can be packaged into a standalone `.exe` using [PyInstaller](https://pyinstaller.org/).

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the application:

```bash
pyinstaller --noconfirm main.spec
```

The executable will be generated at:

```text
dist/TreeConvert.exe
```

The build is configured as a **windowed application**, so no console window will appear when running the `.exe`.

---

## 🧩 Architecture

```text
┌──────────────────────────────────────────────────┐
│                  pywebview                        │
│          (Native Desktop Window)                  │
│                                                  │
│  ┌──────────────────────────────────────────┐    │
│  │         HTML/CSS/JS Frontend             │    │
│  │        templates/index.html              │    │
│  └──────────────────┬───────────────────────┘    │
│                     │ HTTP                       │
│                     ▼                            │
│  ┌──────────────────────────────────────────┐    │
│  │            Flask Backend                 │    │
│  │              app.py                      │    │
│  │                                          │    │
│  │  POST /api/convert   → Start conversion  │    │
│  │  GET  /api/status    → Progress updates  │    │
│  │  GET  /api/log       → Conversion log    │    │
│  └──────────────────┬───────────────────────┘    │
│                     │                            │
│                     ▼                            │
│  ┌──────────────────────────────────────────┐    │
│  │         Pillow Image Processing          │    │
│  │  • Format Conversion                     │    │
│  │  • Quality Control                       │    │
│  │  • EXIF Metadata                         │    │
│  │  • Transparency Handling                 │    │
│  └──────────────────────────────────────────┘    │
└──────────────────────────────────────────────────┘
```

---

## 🤝 Contributing

Contributions are welcome!

If you discover a bug, have a feature request, or want to improve TreeConvert:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Open a Pull Request

For larger changes, opening an issue first is recommended.

---

## 🗺️ Roadmap

Potential future improvements:

* [ ] Drag & drop support
* [ ] Image preview
* [ ] More output formats
* [ ] Parallel conversion
* [ ] Conversion presets
* [ ] Custom output naming
* [ ] Dark/light theme customization
* [ ] Conversion statistics
* [ ] Cancel / pause conversion

---

## 📜 License

TreeConvert is **free and open-source software**.

You are free to use, modify, and contribute to the project according to the terms of the project's license.

---

<div align="center">

## 🌳 TreeConvert

**Batch image conversion, made simple.**

<br>

Made with ❤️ By Abdalrahman_Amr using Python.

</div>
