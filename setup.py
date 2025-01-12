# Copyright (C) 2024 Adrian Antico <adrianantico@gmail.com>
# License: AGPL (>= 3), adrianantico@gmail.com

from setuptools import setup, find_packages
import os

# The directory containing this file
HERE = os.path.dirname(os.path.abspath(__file__))

# Read the README file
with open(os.path.join(HERE, "README.md"), encoding="utf-8") as fid:
    README = fid.read()

# Read the requirements file
with open(os.path.join(HERE, "requirements.txt"), encoding="utf-8") as f:
    required = f.read().splitlines()

# Setup configuration
setup(
    name="QuickEcharts",
    version="2.1.0",
    description="Create Echart plots in a single simple function call, with internal data wrangling via polars",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AdrianAntico/QuickEcharts",
    author="Adrian Antico",
    author_email="adrianantico@gmail.com",
    license="AGPL >= 3",
    packages=[
        "QuickEcharts",
        "QuickEcharts.shiny_app",
        "QuickEcharts.shiny_app.modules",
    ],
    include_package_data=True,  # Ensure non-Python files are included
    package_data={
        "QuickEcharts": ["shiny_app/www/*"],  # Include static files
    },
    install_requires=required,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
