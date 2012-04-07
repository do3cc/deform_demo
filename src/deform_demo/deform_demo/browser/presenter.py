from five import grok
from Products.CMFCore.interfaces import IFolderish
from example.conference.presenter import IPresenter

from deform_demo.browser.deform_base import BaseAddView, BaseEditForm, BaseView
from deform_demo.layer import IDeformDemo

grok.layer(IDeformDemo)

grok.templatedir('deform_templates')


class Edit(BaseEditForm):
    grok.context(IPresenter)
    grok.template('baseform')


class View(BaseView):
    grok.context(IPresenter)
    grok.template('baseform')


class AddPresenter(BaseAddView):
    grok.context(IFolderish)
    portal_type = 'example.conference.presenter'
    grok.template('baseform')
