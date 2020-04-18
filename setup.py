import os
import re
import setuptools

HERE = os.path.abspath(os.path.dirname(__file__))

VERSION_PY = ["version.py"]

REQUIRED_PCKGS = [
    'bokeh',
]


def read(*args):
    """Read complete file contest."""
    fp = os.path.join(HERE, *args)
    with open(fp) as fh:
        return fh.read()


def get_requirements():
    """Read the requirements file."""
    requirements = read("requirements.txt")
    return [r for r in requirements.strip().splitlines()]


def get_version():
    """Parse version from file."""
    version_file = read(*VERSION_PY)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string")


setuptools.setup(
    install_requires=get_requirements(),
    version=get_version(),
)
