from setuptools import setup

setup(
    name='crypterma',
    version='0.1.4',
    description='ASCII-chart version of how Bitcoin grows',
    long_description='''A console application that allows you to see a graph of the Bitcoin price change in any time interval. Also prints the current cost and comparison with yesterday's value.
Almost all currencies are supported.''',
    author='George Gabolaev',
    author_email='gabolaev98@gmail.com',
    url='https://github.com/gabolaev/crypterma',
    license='MIT',
    python_requires='>=3.6',
    packages=['crypterma','crypterma.configs'],
    install_requires=[
        'termcolor',
        'requests'
        ],
    entry_points={
        'console_scripts': [
            'crypterma = crypterma.__main__:main'
            ]
        }
    )
