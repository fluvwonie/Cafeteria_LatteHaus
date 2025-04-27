# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['caf_frontend_portable.py'],
    pathex=[],
    binaries=[],
    datas=[('imagenes', 'imagenes'), ('productos.json', '.'), ('users.json', '.'), ('inventario.json', '.'), ('orders.json', '.'), ('historial.json', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='caf_frontend_portable',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
