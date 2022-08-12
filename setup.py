import os

from setuptools import setup

basedir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(basedir, 'README.md'), encoding='utf-8') as f:
    long_des = f.read()

setup(
    name='Flask-AceEditor',
    version='1.0.0',
    packages=['flask_aceeditor'],
    url='https://github.com/lrsgzs/flask-aceeitor',
    license='MIT',
    author='LRS',
    author_email='liurongshuo2022@outlook.com',
    description='This is AceEditor on flask.',
    long_description=long_des,
    keywords="flask extension lrspackages",
    long_description_content_type='text/markdown',
    install_requires=['flask'],
    extras_require={},
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
