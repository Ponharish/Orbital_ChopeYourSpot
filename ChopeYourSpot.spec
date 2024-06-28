# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['manage.py'],
    pathex=[],
    binaries=[],
    datas=[
	('assets', 'assets'),
	('Company_Admin/static', 'Company_Admin/static'),
('Company_Admin/templates', 'Company_Admin/templates'),
	('Employer_Employee/static', 'Employer_Employee/static'),
('Employer_Employee/templates', 'Employer_Employee/templates'),
	('homePage/static', 'homePage/static'),
('homePage/templates', 'homePage/templates'),
	('login/static', 'login/static'),
('login/templates', 'login/templates'),
('System_Admin/static', 'System_Admin/static'),
('System_Admin/templates', 'System_Admin/templates'),
	('Company_Admin/migrations', 'Company_Admin/migrations'),
('Employer_Employee/migrations', 'Employer_Employee/migrations'),
('homePage/migrations', 'homePage/migrations'),
('login/migrations', 'login/migrations'),
('System_Admin/migrations', 'System_Admin/migrations')

],
    hiddenimports=[
	'django',
        'asgiref',
        'gunicorn',
        'packaging',
        'pytz',
        'sqlparse',
        'typing_extensions'
],
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ChopeYourSpot',
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
