from setuptools import setup, find_packages

setup(
    name='rabby-clone',
    version='0.1.0',
    description='Mac to Mac migration utility',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'paramiko',
    ],
    entry_points={
        'console_scripts': [
            'rabby-clone=src.main:main',
        ],
    },
)