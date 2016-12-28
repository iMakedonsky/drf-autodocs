from setuptools import find_packages, setup

setup(
    name="drf_autodocs",
    version=__import__('drf_autodocs').__version__,
    author="Mashianov Oleksander",
    author_email="mashianov@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/iMakedonsky/drf-autodocs",
    license='BSD',
    description="Extensible auto django rest framework api generator",
    long_description=open("README.md").read(),
    install_requires=[
        'django>=1.10',
        'markdown>=2.6.7',
        'addict>=2.0.0',
        'djangorestframework>=3.5'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
)
