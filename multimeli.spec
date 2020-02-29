# -*- mode: python -*-

block_cipher = None


a = Analysis(['multimeli.py'],
             pathex=['H:\\Programmes_DEVELOPPEMENT\\Qt\\5.11.1\\msvc2017_64\\bin', 'E:\\Zone Documents\\ToF\\Documents\\GitHub\\multimeli'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='multimeli',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
