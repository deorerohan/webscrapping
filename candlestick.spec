# -*- mode: python -*-
a = Analysis(['candlestick.py'],
             pathex=['/home/rohan/Documents/repos/Python Hacks'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='candlestick',
          debug=False,
          strip=None,
          upx=True,
          console=True )
