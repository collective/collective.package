Introduction
============

``collective.package`` is a sample add-on package for Plone developers.

Motivation
----------

Boilerplate code from ``ZopeSkel`` is nice; but not quite as nice as example code.

Installation
------------

You may install this add-on via Buildout, like so::

    virtualenv-2.7 .
    bin/pip install zc.buildout
    bin/buildout init
    cat << EOF > buildout.cfg
    [buildout]
    extends = http://build.pythonpackages.com/buildout/plone/latest
    [plone]
    eggs += collective.package
    EOF
    bin/buildout
    bin/plone fg

Examples
--------

This package contains code examples for common add-on package tasks in Plone.
For example, creating a Python package that "shows up" as an installable
add-on in the Plone control panel. Or installing an authentication plugin.

Here is a list of examples:

* How do I make my package "show up" in Plone?

  * Use the ``Quick Installer``.

* How do I create an authentication plugin?

  * Use the ``Pluggable Auth Service``.

