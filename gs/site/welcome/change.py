# -*- coding: utf-8 -*-
from __future__ import absolute_import
from zope.cachedescriptors.property import Lazy
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form.base import SiteForm
from gs.content.form.base.wymeditor import wym_editor_widget
from .interfaces import IChangeWelcome
from .message import WelcomeMessage
#from audit import ChangeAuditor, CHANGE


class Change(SiteForm):
    label = u'Change the welcome'
    pageTemplateFileName = 'browser/templates/change.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)

    def __init__(self, context, request):
        super(Change, self).__init__(context, request)

    @Lazy
    def welcomeMessage(self):
        retval = WelcomeMessage(self.siteInfo)
        return retval

    @Lazy
    def form_fields(self):
        retval = form.Fields(IChangeWelcome,
                            render_context=False)
        retval['message'].custom_widget = wym_editor_widget
        return retval

    def setUpWidgets(self, ignore_request=False):
        data = {'greeting': self.welcomeMessage.greeting,
                'message': self.welcomeMessage.message}

        self.widgets = form.setUpWidgets(
            self.form_fields, self.prefix, self.context,
            self.request, form=self, data=data,
            ignore_request=ignore_request)

    @form.action(label=u'Change', failure='handle_change_action_failure')
    def handle_change(self, action, data):
        self.welcomeMessage.greeting = data['greeting']
        self.welcomeMessage.message = data['message']
        self.status = u'The welcome that appears on <a href="/">the site '\
                        u'homepage</a> has been changed.'
        assert type(self.status) == unicode

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = u'<p>There is an error:</p>'
        else:
            self.status = u'<p>There are errors:</p>'
        assert type(self.status) == unicode
