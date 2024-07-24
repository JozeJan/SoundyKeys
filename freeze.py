import py2exe
from py2exe import freeze
import os
freeze(
    console=[{"script":"main.py"}],
    windows=[],
    data_files=os.listdir("C:\\Users\\matej\\PycharmProjects\\CUkeys\\Audio"),
    zipfile='CUkeys.zip',
    options={"packages":["pygame","keyboard"]},
    version_info={}
)

#