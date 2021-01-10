from setuptools import setup

setup(
    name='hidapi-cffi',
    version="0.2.3",
    description=("CFFI wrapper for hidapi"),
    author="Johannes Baiter",
    url="http://github.com/jbaiter/hidapi-cffi.git",
    author_email="johannes.baiter@gmail.com",
    license='BSD',
    py_modules=['hidapi'],
    setup_requires=['cffi >= 1.14.4']
)
