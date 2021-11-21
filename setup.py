from setuptools import setup

setup(
    name = 'rasloader',
    version = '1.0.0',
    description = 'Load Rigaku .ras files',
    author = 'Tristan K Truttmann',
    author_email = 'tristan.truttmann@gmail.com',
    license = 'MIT',
    packages=['rasloader'],
    zip_safe=False,
    requires=['numpy','pandas']
)
