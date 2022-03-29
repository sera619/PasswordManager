import sys
from cx_Freeze import setup, Executable


files =['main.py','favicon.ico']

target = Executable(script='main.py', icon='favicon.ico')

setup(
    name ='P455 W1ZZ4RD',
    version = '0.3.6',
    description ='A Password Manager Tool',
    author = 'S3R43o3',
    options = {'build_exe':{'include_files':files}},
    executables=[target]
)