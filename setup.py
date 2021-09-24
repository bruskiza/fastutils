import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "fastutils",
    version = "0.0.1",
    author = "Bruce McIntyre",
    author_email = "bruce.mcintyre@gmail.com",
    description = ("Musings with Fast API"),
    license = "BSD",
    keywords = "fastapi utils",
    url = "https://github.com/bruskiza/fastutils",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
