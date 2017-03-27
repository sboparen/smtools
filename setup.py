from setuptools import setup

setup(
    name='smtools',
    version='0.3',
    packages=[
        'smtools',
    ],
    entry_points={
        'console_scripts': [
            'itgoggpatch = smtools.itgoggpatch:main',
            'r21patch = smtools.r21patch:main',
            ]
    },
    package_data={
        'smtools': ['itgoggpatch'],
    },
    )
