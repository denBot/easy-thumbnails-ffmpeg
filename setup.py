from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='easy-thumbnails-ffmpeg',
    version='0.1.0',
    license='CC0 1.0',
    description='Video thumbnails source generator.',
    long_description='Video thumbnails source generator for `easy_thumbnails` using `ffmpeg`.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Multimedia :: Video :: Display',
    ],
    keywords='easy_thumbnails ffmpeg video thumbnails django',
    url='https://github.com/pluma/easy-thumbnails-ffmpeg',
    author='Alan Plum',
    author_email='me@pluma.io',
    packages=['easy_thumbnails_ffmpeg'],
    install_requires=[
        'easy_thumbnails',
    ],
    zip_safe=False)
