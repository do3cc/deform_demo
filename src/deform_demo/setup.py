from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='deform_demo',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "starzel.deformwidgets",
        "imsvdex",
        "deform",
        "plone.memoize",
        "colander",
        "collective.deform",
        "collective.colander",
        "Products.statusmessages",
        "zope.event",
        "zope.lifecycleevent",
        "Acquisition",
        "plone.dexterity",
        "zope.component",
        "five.grok",
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone

      # -*- Entry points: -*-
      """,
      )
