from setuptools import setup, find_packages

setup(
    name="pyviv",
    version="1.0.0",
    author="Ofekm5",
    description="A Python tool for managing VHDL designs with Vivado",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),  # Finds packages inside src
    package_dir={"": "src"},              # Sets src as the package root
    scripts=["src/pyviv.py"],              # Command-line script
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[],                    # Add any dependencies here if needed
    entry_points={
        "console_scripts": [
            "pyviv=pyviv:main",              # Allows using 'pyviv' in terminal
        ],
    },
    python_requires=">=3.6",
)
