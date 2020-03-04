from setuptools import setup

setup(
    name='scrapylib',
    version='1.7.0',
    license='BSD',
    description='Scrapy helper functions and processors',
    author='Scrapinghub',
    url='http://github.com/nyov/scrapylib',
    packages=['scrapylib', 'scrapylib.constraints', 'scrapylib.processors'],
    platforms=['Any'],
    classifiers=[
        'Development Status :: 7 - Inactive',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    install_requires=[
        'Scrapy>=1.0.0',
    ]
)
