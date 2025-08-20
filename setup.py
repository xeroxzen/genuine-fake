import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="genuine-fake",
    version="1.2.23",
    description="Get genuine data for your testing requirements.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/xeroxzen/genuine-fake",
    author="Andile Jaden Mbele",
    author_email="andilembele020@gmail.com",
    # license="MIT",  # Removed to avoid license-file metadata issues
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=["genuine"],
    include_package_data=True,
    python_requires=">=3.7",
    license_files=None,
)
