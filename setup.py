#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="langchain",
    author_email='agsl0905@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="\",
    entry_points={
        'console_scripts': [
            'langchain_personal=langchain_personal.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='langchain_personal',
    name='langchain_personal',
    packages=find_packages(include=['langchain_personal', 'langchain_personal.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/angusll/langchain_personal',
    version='0.1.0',
    zip_safe=False,
)
