# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Sporta_viktorina.py'],
    pathex=[],
    binaries=[],
    datas=[('attels1.png', '.'), ('attels2.png', '.'), ('attels3.png', '.'), ('attels4.png', '.'), ('attels5.png', '.'), ('attels6.png', '.'), ('attels7.png', '.'), ('attels8.png', '.'), ('attels9.png', '.'), ('attels10.png', '.'), ('attels11.png', '.'), ('attels12.png', '.'), ('attels13.png', '.'), ('attels14.png', '.'), ('attels15.png', '.')],
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
    name='Sporta_viktorina',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
