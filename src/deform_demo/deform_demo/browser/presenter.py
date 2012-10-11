#!/usr/bin/python
# -*- coding: utf-8 -*-
from collective.deform import base_views
from example.conference.presenter import IPresenter
from five import grok
from zope.interface import Interface

from deform_demo.layer import IDeformDemo

grok.layer(IDeformDemo)


class Edit(base_views.BaseEditForm):
    grok.context(IPresenter)


class View(base_views.BaseView):
    grok.context(IPresenter)


class AddPresenter(base_views.BaseAddView):
    grok.context(Interface)
    portal_type = 'example.conference.presenter'

