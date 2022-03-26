import sys
from cx_Freeze import setup, Executable


files =['main.py']
option = {
    'include_files': files,
}
target = Executable(script='main.py')

setup(
    name ='P455 W1ZZ4RD',
    version = '0.2.6',
    description ='A Password Manager Tool',
    options = {'build_exe':option},
    executables=[target]
)