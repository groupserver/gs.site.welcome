# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals
from zope.cachedescriptors.property import Lazy
from zope.formlib import form
from zope.i18n import translate
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form.base import SiteForm
from gs.content.form.base.wymeditor import wym_editor_widget
from .interfaces import IChangeWelcome
from .message import WelcomeMessage
from . import GSMessageFactory as _
#from audit import ChangeAuditor, CHANGE


class Change(SiteForm):
    label = _('Change the welcome')
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
        retval = form.Fields(IChangeWelcome, render_context=False)
        retval['message'].custom_widget = wym_editor_widget
        return retval

    def setUpWidgets(self, ignore_request=False):
        data = {'greeting': translate(self.welcomeMessage.greeting),
                'message': translate(self.welcomeMessage.message)}

        self.widgets = form.setUpWidgets(
            self.form_fields, self.prefix, self.context,
            self.request, form=self, data=data,
            ignore_request=ignore_request)

    @form.action(label=_('Change'), failure='handle_change_action_failure')
    def handle_change(self, action, data):
        self.welcomeMessage.greeting = data['greeting']
        self.welcomeMessage.message = data['message']
        self.status = _(
            'The welcome that appears on <a href="/">the site homepage</a> '
            'has been changed.')

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = _('<p>There is an error:</p>')
        else:
            self.status = _('<p>There are errors:</p>')
