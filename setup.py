# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='PYSqlClient',
    version='0.1.0',
    description='Package for sql data client equivalent',
    long_description=readme,
    author='Anubrij Chandra',
    author_email='anubrij@live.com',
    url='https://github.com/anubrij/PYSQLCLIENT',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
