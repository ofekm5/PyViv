from setuptools import setup, find_packages

setup(
    name="PyViv",
    version="1.0.0",
    description="A Python package for managing VHDL projects in Vivado.",
    author="Ofek Markus",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "PyViv=PyViv.main:main",
        ]
    },
)
