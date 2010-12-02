from setuptools import setup, find_packages
import os

version = '0.3'

def read(input):
    return open(input, 'rw').read()

setup(name='collective.package',
      version=version,
      description="Sample package to demonstrate development of add-ons for the Plone CMS",
      long_description=read('README.txt') + read('docs/HISTORY.txt'),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Alex Clark',
      author_email='aclark@aclark.net',
      url='http://svn.plone.org/svn/collective/collective.package/',
      license='GPL',
      packages=find_packages(),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
