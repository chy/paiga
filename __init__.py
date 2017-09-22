#Init File for PyGA

# Ugly hack to allow absolute import from the root folder
# whatever its name is. Please forgive the heresy.
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "pyga"

from .builders import Literal
from .builders import Condition
# from pyga.builders import Function
# from pyga.builders import Rule
from .script import Script
