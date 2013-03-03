# -*- coding: utf-8 -*-
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form.form import SiteForm
from gs.content.form.wymeditor import wym_editor_widget
from interfaces import IChangeWelcome
#from audit import ChangeAuditor, CHANGE


class Change(SiteForm):
    label = u'Change the Welcome'
    pageTemplateFileName = 'browser/templates/change.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    form_fields = form.Fields(IChangeWelcome, render_context=False)

    def __init__(self, context, request):
        super(Change, self).__init__(context, request)
        self.form_fields['message'].custom_widget = \
            wym_editor_widget

    @form.action(label=u'Change', failure='handle_change_action_failure')
    def handle_change(self, action, data):
        self.set_greeting(data['greeting'])
        self.set_message(data['message'])
        self.status = u'The Welcome that appears on <a href="/">the site '\
                        u'homepage</a> has been changed.'
        assert type(self.status) == unicode

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = u'<p>There is an error:</p>'
        else:
            self.status = u'<p>There are errors:</p>'
        assert type(self.status) == unicode

    def set_greeting(self, greeting):
        pass

    def set_message(self, message):
        pass