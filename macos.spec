# Build on macOS: python -m PyInstaller --noconfirm macos.spec
import sys

if sys.platform != 'darwin':
    raise SystemExit('Build macos.spec on macOS.')

a = Analysis(
    ['main.py'],
    pathex=[SPECPATH],
    datas=[('templates', 'templates')],
    hiddenimports=['webview.platforms.cocoa'],
    excludes=['tkinter', 'PyQt5', 'PyQt6', 'PySide2', 'PySide6'],
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, [],
    exclude_binaries=True,
    name='TreeConvert',
    console=False,
    argv_emulation=False,
)
collection = COLLECT(exe, a.binaries, a.datas, name='TreeConvert')
app = BUNDLE(
    collection,
    name='TreeConvert.app',
    icon='convert.png',
    bundle_identifier='com.treeconvert.desktop',
    version='1.0.0',
    info_plist={
        'CFBundleDisplayName': 'TreeConvert',
        'NSHighResolutionCapable': True,
        'NSPrincipalClass': 'NSApplication',
    },
)
