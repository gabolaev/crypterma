from setuptools import setup

setup(
    name='crypterma',
    version='0.1.7',
    author='George Gabolaev',
    author_email='gabolaev98@gmail.com',
    url='https://github.com/gabolaev/crypterma',
    license='MIT',
    python_requires='>=3.6',
    description='ASCII-chart version of how Bitcoin grows',
    long_description='''A console application that allows you to see a graph of the Bitcoin price change in any time interval. Also prints the current cost and comparison with yesterday's value.
Almost all currencies are supported.
More info: https://github.com/gabolaev/crypterma/blob/master/README.md''',
    packages=['crypterma','crypterma.configs'],
    install_requires=[
        'termcolor',
        'requests'
        ],
    entry_points={
        'console_scripts': [
            'crypterma = crypterma.__main__:main'
            ]
        },
    )
