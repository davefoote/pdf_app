# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['pdf_app.py'],
             pathex=['/Users/dave/Desktop/py_office/pdf_app'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='fotee_pdfapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='logo.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='fotee_pdfapp')
app = BUNDLE(coll,
             name='fotee_pdfapp.app',
             icon='logo.icns',
             bundle_identifier=None)
