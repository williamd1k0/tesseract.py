import os
from setuptools import setup


longDesc = ""
if os.path.exists("README.md"):
	longDesc = open("README.md").read().strip()

setup(
    name = "tesseract.py",
    version = "0.1.6",
    author = "Samuel Hoffstaetter",
    author_email="",
    maintainer = "Matthias Lee",
    maintainer_email = "pytesseract@madmaze.net",
    description = ("Python-tesseract is a python wrapper for google's Tesseract-OCR"),
    long_description = longDesc,
    license = "MIT",
    keywords = "python-tesseract OCR Python",
    url = "https://github.com/williamd1k0/tesseract.py",
    packages=['tesseractpy'],
    package_dir={'tesseractpy': 'src'},
    package_data = {'tesseractpy': ['*.png','*.jpg']},
    entry_points = {'console_scripts': ['tesseractpy = tesseractpy.tesseractpy:main']},
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
