# setup.py
from setuptools import setup, find_packages

setup(
    name='urgent-care-scraper',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'urgent-care-scraper=urgent-care-scraper.main:main',
        ],
    },
)