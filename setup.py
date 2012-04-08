from setuptools import find_packages
from setuptools import setup
import os

VERSION = '0.3.1'


setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    classifiers=[
      "Framework :: Plone",
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="Sample package to demonstrate development of \
        add-ons for the Plone CMS",
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    include_package_data=True,
    install_requires=[
        'setuptools',
    ],
    long_description=(
        open('README.rst').read() +
        open(os.path.join('docs', 'HISTORY.txt')).read()
    ),
    keywords='plone example package',
    license='ZPL',
    name='collective.package',
    namespace_packages=[
        'collective'
    ],
    packages=find_packages(),
    url='http://collective.github.com/collective.package/',
    version=VERSION,
    zip_safe=False,
)
