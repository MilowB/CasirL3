from setuptools import setup
from Cython.Build import cythonize

setup(
    name='TP4_app',
    ext_modules=cythonize("TP4_correction.py"),
    zip_safe=False,
)