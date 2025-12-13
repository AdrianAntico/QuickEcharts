# Copyright (C) 2024 Adrian Antico <adrianantico@gmail.com>
# License: MIT, adrianantico@gmail.com

from setuptools import setup, find_packages
from pathlib import Path

# Project directory
HERE = Path(__file__).parent.resolve()

# Read the README file
README = (HERE / "README.md").read_text(encoding="utf-8")

# Read the requirements file
required = (HERE / "requirements.txt").read_text(encoding="utf-8").splitlines()

setup(
    name="QuickEcharts",
    version="2.1.6",
    description="Create ECharts plots in a single simple function call, with internal data wrangling via polars",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AdrianAntico/QuickEcharts",
    author="Adrian Antico",
    author_email="adrianantico@gmail.com",
    license="MIT",
    python_requires=">=3.10",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "QuickEcharts": [
            "shiny_app/www/*",
        ],
    },
    install_requires=required,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)
