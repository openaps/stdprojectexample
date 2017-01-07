#!/usr/bin/python

from setuptools import setup, find_packages
import platform

# import the package works here if and only if it's a sibling to this file
import stdprojectexample

def readme():
    with open("README.md") as f:
        return f.read()

setup(name='stdprojectexample',
    version='0.0.1', # http://semver.org/
    description='Frib with Frobs with excellent Fermocity.',
    long_description=readme(),
    # Original Author
    author="Author Autherian",
    # I'm just maintaining the package, @compbrain authored it.
    author_email="original@auth.or",
    # Maintainer Info
    maintainer="Maintainer McGroo",
    maintainer_email="work@maintain.er",
    url="https://github.com/openaps/stdprojectexample",
    packages=find_packages( ),
    # list of packages to be installed automatically
    install_requires = [
      'pyserial'
    ],
    # pypi and package metadata
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries'
    ],
    # files to install alongside the package in site location
    package_data={
      # 'dexcom_reader': ['etc/udev/rules.d/*']
    },
    # files to install in arbitrary locations, may require root permissions for
    # install
    data_files = [
      # installing to root locations breaks things for virtualenv based
      # environments which do not have root.
      # ('/etc/udev/rules.d', ['dexcom_reader/etc/udev/rules.d/80-dexcom.rules'] ),

    ],
    # eggs can be zipped, but doing so prevents live docs from working correctly
    zip_safe=False,
    include_package_data=True
)

#####
# EOF
