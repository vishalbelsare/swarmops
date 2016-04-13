# -*- coding: utf-8 -*-
from setuptools import setup

MY_VERSION = '1.0.0'

setup(
    name='swarmops',
    packages=['swarmops'],
    version=MY_VERSION,
    description='Heuristic Optimization for Python',
    author='Magnus Erik Hvass Pedersen',
    author_email='magnus(at)hvass-labs(dot)org',
    url='https://github.com/Hvass-Labs/swarmops',
    download_url='git+https://github.com/Hvass-Labs/swarmops.git',
    license='BSD',
    keywords=['heuristic optimization', 'particle swarm optimization',
              'differential evolution', 'meta-optimization'],
    install_requires=[
        'numpy>=1.9',
        'scipy>=0.16',
        'matplotlib>=1.5',
    ],
)