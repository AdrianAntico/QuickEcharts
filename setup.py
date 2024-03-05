# Copyright (C) 2021 Adrian Antico <adrianantico@gmail.com>
# License: AGPL (>= 3), adrianantico@gmail.com

import pathlib
from setuptools import setup, find_packages
import os

# The directory containing this file
HERE = os.path.dirname(os.path.abspath("__file__"))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()
with open(os.path.join(HERE, "requirements.txt")) as f:
    required = f.read().splitlines()

setup(
    name="QuickEcharts",
    version="0.1.0",
    description="Create Echart plots in a single simple function call, with internal data wrangling via polars",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AdrianAntico/QuickEcharts",
    author=["Adrian Antico"],
    author_email="adrianantico@gmail.com",
    license="AGPL >= 3",
    install_requires=required,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
