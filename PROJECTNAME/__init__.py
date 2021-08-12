"""
PROJECTNAME Project description in __init__.py
"""
# imports __version__ variable
from pathlib import Path
thisdir = Path(__file__).resolve().parent
with open(thisdir / 'VERSION') as f: 
    __version__ = f.readline().strip()

from .train import train
from .infer import infer
from .validate import validate

__all__ = ['train', 'infer', 'validate']

if __name__ == 'PROJECTNAME':
    raise RuntimeError('Please customise the module name before running.')
