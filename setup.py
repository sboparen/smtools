from setuptools import setup

setup(
    name='smtools',
    version='0.1',
    packages=[
        'smtools',
    ],
    entry_points={
        'console_scripts': [
            'r21patch = smtools.r21patch:main',
            ]
    },
    )
