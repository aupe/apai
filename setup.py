import os
from ast import literal_eval

from setuptools import find_packages, setup


def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return ".".join(map(str, version_tuple[:-1])) + version_tuple[-1]
    return ".".join(map(str, version_tuple))


init = os.path.join(os.path.dirname(__file__), "apai", "__init__.py")

version_line = list(filter(lambda l: l.startswith("VERSION"), open(init)))[0]

# VERSION is a tuple so we need to eval 'version_line'.
# We could simply import it from the package but we
# cannot be sure that this package is importable before
# installation is done.
PKG_VERSION = get_version(literal_eval(version_line.split(" = ")[-1]))

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="apai",
    version=PKG_VERSION,
    description="ML & DL helper library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ausra Petrenaite",
    author_email="ausra.petrenaite@gmail.com",
    url="https://github.com/aupe/apai",
    download_url="https://github.com/mokahaiku/toai",
    install_requires=[
        "attrs",
        "fastparquet",
        "fastprogress",
        "funcy",
        "imagehash",
        "joblib",
        "lightgbm",
        "numpy",
        "pandas",
        "Pillow",
        "pyarrow",
        "scikit-learn",
        "scikit-optimize",
        "seaborn",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
)
