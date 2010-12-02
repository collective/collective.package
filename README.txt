.. contents::

Introduction
============

``collective.package`` is a sample add-on package for Plone developers.

Motivation
----------

Boilerplate from template generators like ``ZopeSkel`` is nice; but not quite as
nice as real, but still generic, examples.

In the same way the collective developer's manual
(http://svn.plone.org/svn/collective/collective.developermanual/trunk/) aims to
document every single occurence along the way to Plone coding zen,
``collective.package`` aims to code it then release it as an installable add-on.

Installation
------------

You may install this add-on via Buildout, like so::

    [buildout]
    extends = http://dist.plone.org/release/4.0.2/versions.cfg
    versions = versions
    parts = plone

    [plone]
    recipe = plone.recipe.zope2instance
    user = admin:admin
    eggs = 
        Plone
        collective.package

Usage
-----

This package contains code examples for common add-on package tasks in Plone.
For example, creating a Python package that "shows up" as an installable
add-on in the Plone control panel. Or installing an authentication plugin.

Examples
--------

Here is a list of examples: 

* How do I make my package "show up" in Plone? Use the ``Quick Installer`` of
  course.
* How do I create an authentication plugin? Use the ``Pluggable Auth Service``, of
  course.

