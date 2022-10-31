import os
import sys
from setuptools import setup, find_packages

def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()

def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")

long_description = read("README.rst")

setup(
    name="dopy",
    version=get_version("src/dopy/__init__.py"),
    description="A command line application for managing tasks via ToDo.txt files written in python.",
    long_description=long_description,
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Office/Business",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    url="https://dopy.prokopto.dev/",
    project_urls={
        "Documentation": "https://dopy.prokopto.dev/",
        "Source": "https://github.com/CapularisPerpetua/dopy",
        "Changelog": "https://dopy.prokopto.dev/en/stable/news/",
    },
    author="Courtney Caldwell",
    author_email="courtney@prokopto.dev",
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        exclude=["contrib", "docs", "tests*", "tasks"],
    ),
    package_data={
        "pip": ["py.typed"],
        "pip._vendor": ["vendor.txt"],
        "pip._vendor.certifi": ["*.pem"],
        "pip._vendor.requests": ["*.pem"],
        "pip._vendor.distlib._backport": ["sysconfig.cfg"],
        "pip._vendor.distlib": [
            "t32.exe",
            "t64.exe",
            "t64-arm.exe",
            "w32.exe",
            "w64.exe",
            "w64-arm.exe",
        ],
    },
    entry_points={
        "console_scripts": [
            "dopy=dopy._internal.cli.main:main",
            "pip{}=dopy._internal.cli.main:main".format(sys.version_info[0]),
            "pip{}.{}=dopy._internal.cli.main:main".format(*sys.version_info[:2]),
        ],
    },
    zip_safe=False,
    # NOTE: python_requires is duplicated in __pip-runner__.py.
    # When changing this value, please change the other copy as well.
    python_requires=">=3.7",
)


if __name__ == '__main__':
    setup()
