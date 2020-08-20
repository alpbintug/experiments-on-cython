from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules=cythonize('trying_c.pyx','trying.py',annotate=True))