import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Genuine-fake",
    version="1.2.9",
    description="Get genuine data for your testing requirements.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/xeroxzen/genuine-fake",
    author="Andile Jaden Mbele",
    author_email="andilembele020@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["genuine"],
    include_package_data=True,
    # install_requires=[],
)
