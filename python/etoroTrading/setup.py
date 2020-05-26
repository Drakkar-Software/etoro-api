# coding: utf-8

"""
    eToro Trading API

    The Trading API allows the development of the full trading capabilities in the eToro platform  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "etoro-api"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="eToro Trading API",
    author_email="",
    url="https://github.com/mkhaled87/etoro-api/",
    keywords=["Swagger", "eToro Trading API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The Trading API allows the development of the full trading capabilities in the eToro platform  # noqa: E501
    """
)
