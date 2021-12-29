from setuptools import setup, find_packages
import codecs
import os
import pathlib

VERSION = '1.0.0'
DESCRIPTION = 'Agora Token Builder. RTC & RTM'
LONG_DESCRIPTION = ''

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

# Setting up
setup(
    name="agora_token_builder",
    version=VERSION,
    author="Dennis",
    author_email="<dennis@agora.io>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=README,
    url="https://github.com/AgoraIO-Community/python-token-builder",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'agora', 'token-builder'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
