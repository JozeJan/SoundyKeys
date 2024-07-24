from glob import glob
from py2exe import freeze
freeze(
    console=[{"script":"main.py"}],
    data_files=[("Audio",glob("Audio/*.wav"))],
    zipfile=None,
    options={"includes":["pygame","keyboard"]}
)
#