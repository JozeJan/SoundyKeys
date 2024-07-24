import py2exe
from py2exe import freeze
import os

freeze(
    console=[{"script":"main.py"}],
    windows=[],
    data_files=os.listdir("Audio"),
    zipfile='CUkeys.zip',
    options={},
    version_info={}
)