import threading
import webview
from werkzeug.serving import make_server
from app import app


class DesktopAPI:
    def __init__(self):
        self._window = None

    def choose_folder(self):
        folders = self._window.create_file_dialog(webview.FileDialog.FOLDER)
        return folders[0] if folders else None


def main():
    # Bind before opening the window so its first request cannot race startup.
    server = make_server("127.0.0.1", 0, app, threaded=True)
    flask_thread = threading.Thread(target=server.serve_forever, daemon=True)
    flask_thread.start()
    api = DesktopAPI()
    api._window = webview.create_window(
        "TreeConvert",
        f"http://127.0.0.1:{server.server_port}",
        js_api=api,
        width=620,
        height=700,
        min_size=(500, 550),
        resizable=True,
    )
    try:
        webview.start(debug=False)
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
