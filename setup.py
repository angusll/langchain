#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

requirements = []

test_requirements = []

setup(
    author="Angus",
    author_email="agsl0905@gmail.com",
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
    ],
    description="Personalized search engine for PDFs",
    entry_points={
        "console_scripts": [
            "personal_pdf_assistant=personal_pdf_assistant.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords="personal_pdf_assistant",
    name="personal_pdf_assistant",
    packages=find_packages(
        include=["personal_pdf_assistant", "personal_pdf_assistant.*"]
    ),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/angusll/personal_pdf_assistant",
    version="0.1.0",
    zip_safe=False,
)
