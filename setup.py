# !/bin/python
# -*- coding:utf-8 -*-

# @Author  : Daniel.Pei
# @Email   : peixq1222@icloud.com
# @Created : 2020/4/2 22:02


from os.path import join, dirname

from setuptools import setup, find_packages

VERSION = (0, 0, 1)
__version__ = VERSION
__version_str__ = '.'.join(map(str, VERSION))

f = open(join(dirname(__file__), 'README'))
long_description = f.read().strip()
f.close()

install_requires = [
    # 'urllib3>=1.8, <2.0',
]
tests_require = [
    # 'requests>=2.0.0, <3.0.0',
]

setup(
    name='py_ml',
    description="Python machine learning demo project",
    license="MIT License, Version 2.0",
    url="https://github.com/DanielPei/py-ml",
    long_description=long_description,
    version=__version_str__,
    author="Daniel Pei",
    author_email="peixq1222@icloud.com",
    packages=find_packages(
        where='src',
        exclude=['tests']
    ),
    classifiers=[
        "Programming Language :: Python :: 3.7"
    ],
    install_requires=install_requires,

    test_suite='src.tests.run_tests.run_all',
    tests_require=tests_require,

    extras_require={
        'develop': tests_require + ["sphinx", "sphinx_rtd_theme"]
    },
)
