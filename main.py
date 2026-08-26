import sys
import socket
import threading
import webview
from app import app


def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def start_flask(port):
    app.run(host="127.0.0.1", port=port, debug=False, use_reloader=False)


def main():
    port = find_free_port()

    flask_thread = threading.Thread(target=start_flask, args=(port,), daemon=True)
    flask_thread.start()

    webview.create_window(
        "TreeConvert",
        f"http://127.0.0.1:{port}",
        width=620,
        height=700,
        min_size=(500, 550),
        resizable=True,
    )
    webview.start(debug=False)


if __name__ == "__main__":
    main()
