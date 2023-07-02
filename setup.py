"""Devvit Manager setup.py"""
import re
from distutils.core import setup
from pathlib import Path

PACKAGE_NAME = "devvit_mgr"
HERE = Path(__file__).parent
VERSION_REGEX = re.compile(r'__version__ = "([^"]+)"')
extras = {
    "ci": ["docutils", "packaging"],
    "lint": ["pre-commit"],
}
extras["dev"] = extras["lint"] + extras["ci"]

setup(
    author="Joel Payne",
    author_email="lilspazjoekp@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities",
    ],
    description="Devvit Manager is a Python package that enables you to easily utilize"
    " devvit with multiple Reddit user accounts.",
    entry_points={"console_scripts": ["devvit-mgr = devvit_mgr.cli:main"]},
    extras_require=extras,
    install_requires=["click==8.*", "pick==2.*", "praw==7.*"],
    keywords="devvit manager reddit",
    license="Simplified BSD License",
    long_description=((HERE / "README.rst").read_text()),
    name="devvit-manager",
    package_data={"": ["LICENSE.txt"]},
    packages=["devvit_mgr"],
    python_requires="~=3.8",
    version=(
        VERSION_REGEX.search((HERE / PACKAGE_NAME / "const.py").read_text()).group(1)
    ),
)
