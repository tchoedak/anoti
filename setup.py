import os
from setuptools import setup


setup(
    name='anoti',
    packages=['anoti'],
    version='0.2.0',
    description='anoti',
    author='tchoedak',
    author_email='tchoedak@gmail.com',
    url='https://anoti.tech',
    install_requires=[
        'requests',
        'SQLAlchemy',
        'click',
        'beautifultable',
        'pandas',
        'twilio',
        'bugsnag',
        'mws'
    ],
    entry_points={
        'console_scripts': ['anoti=anoti.app:cli'],
    },
)
