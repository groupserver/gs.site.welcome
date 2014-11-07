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
from __future__ import unicode_literals, absolute_import
from zope.cachedescriptors.property import Lazy
from . import GSMessageFactory as _


class WelcomeMessage(object):
    welcomeId = b'welcome'

    def __init__(self, siteInfo):
        assert siteInfo, 'siteInfo is {0}'.format(type(siteInfo))
        self.siteInfo = siteInfo

    @Lazy
    def pageTemplate(self):
        '''Get the page template for the Welcome message, creating it if
        necessary'''
        r = getattr(self.siteInfo.siteObj, self.welcomeId, None)
        if not r:
            r = self.create_welcome()
        retval = r
        assert retval, 'No page template for the Welcome'
        return retval

    def create_welcome(self):
        folder = self.siteInfo.siteObj
        manageAdd = folder.manage_addProduct['PageTemplates']
        manageAdd.manage_addPageTemplate(self.welcomeId, title='',
                                         text='', REQUEST=None)
        retval = getattr(folder, self.welcomeId)
        assert retval
        retval.write('')
        return retval

    greeting_doc = 'The greeting on the site.'

    @Lazy
    def defaultGreeting(self):
        retval = _('Welcome')
        return retval

    def get_greeting(self):
        t = self.pageTemplate.title
        retval = t if t else self.defaultGreeting
        assert retval
        return retval

    def set_greeting(self, g):
        self.pageTemplate.title = g

    greeting = property(get_greeting, set_greeting, greeting_doc)

    message_doc = 'The Welcome message on the site.'

    @Lazy
    def defaultMsg(self):
        retval = _(
            'default-welcome-message',
            '<p>Welcome to the new online group site for ${siteName}. We '
            'hope that this will be a useful way for everyone to discuss '
            'and share information.</p>',
            mapping={'siteName': self.siteInfo.name})
        return retval

    def get_message(self):
        m = self.pageTemplate()
        retval = m if m else self.defaultMsg
        assert retval
        return retval

    def set_message(self, m):
        self.pageTemplate.write(m)

    message = property(get_message, set_message, message_doc)
