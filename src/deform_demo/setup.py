from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

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
          # -*- Extra requirements: -*-
        "Acquisition",
        "colander",
        "collective.colander",
        "collective.deform",
        "collective.deformwidgets",
        "deform",
        "five.grok",
        "imsvdex",
        "plone.dexterity",
        "plone.memoize",
        "Products.statusmessages",
        "zope.component",
        "zope.event",
        "zope.lifecycleevent",
        "plone.app.referenceablebehavior",
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone

      # -*- Entry points: -*-
      """,
      )
