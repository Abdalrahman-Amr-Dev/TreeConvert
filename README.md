# OSMC - Media Converter

A free, open-source desktop app for batch-converting images between formats. Built with Python and CustomTkinter, it converts entire folders (including subfolders) in one click.

## Features

- Batch convert all images in a folder, recursively including subfolders
- Output formats: **AVIF**, **WebP**, **JPEG**, PNG
- Adjustable quality slider (10–100)
- Preserves EXIF metadata
- Handles transparency (RGBA) correctly when converting to JPEG/AVIF
- Keeps folder structure in the output directory
- Live progress bar and per-file log output
- Windows, macOS, and Linux support

## Requirements

- Python 3.11+
- [pillow-avif-plugin](https://pypi.org/project/pillow-avif-plugin/) (or Pillow 10.4+, which includes AVIF support built-in)
- CustomTkinter

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the app:

```bash
python main.py
```

1. Click **Browse** next to "Source Folder" and pick the folder containing your images.
2. Click **Browse** next to "Save Folder" and pick where converted images should go.
3. Choose an **Output Format** (AVIF, WebP, JPEG, or PNG).
4. Adjust the **Quality** slider if needed.
5. Click **Start Conversion**.

Converted images keep their relative folder structure under the destination folder.

## Building a Windows .exe

Build a standalone single-file exe with PyInstaller:

```bash
pip install pyinstaller customtkinter pillow pillow-avif-plugin
pyinstaller --noconfirm main.spec
```

The exe is produced at `dist/OSMC_Media_Converter.exe` (a windowed app — no console).

## Project Structure

```
OSMC-media-converter/
├── main.py        # Application entry point (CustomTkinter GUI + conversion logic)
├── main.spec      # PyInstaller build configuration
├── convert.ico    # Windows app icon
└── convert.png    # macOS/Linux app icon
```

## License

Free to use and modify. This is an open-source project.
