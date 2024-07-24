from distutils.core import setup
import py2exe
import os

setup(
    console=[{"script": "main.py"}],
    windows=[],
    data_files=[("Audio", [os.path.join("C:\\Users\\matej\\PycharmProjects\\CUkeys\\Audio", f) for f in os.listdir("C:\\Users\\matej\\PycharmProjects\\CUkeys\\Audio")])],
    zipfile='CUkeys.zip',
    options={
        "py2exe": {
            "packages": ["pygame", "keyboard"]
        }
    },
    version_info={}
)
