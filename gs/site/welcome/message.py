# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy


class WelcomeMessage(object):
    welcomeId = 'welcome'

    def __init__(self, siteInfo):
        assert siteInfo, 'siteInfo is {0}'.format(type(siteInfo))
        self.siteInfo = siteInfo

    @Lazy
    def pageTemplate(self):
        u'''Get the page template for the Welcome message, creating it if
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
        manageAdd.manage_addPageTemplate(self.welcomeId, title='', text='',
                                            REQUEST=None)
        return getattr(folder, self.welcomeId)

    greeting_doc = u'The greeting on the site.'

    def get_greeting(self):
        t = self.pageTemplate.title
        retval = t if t else u'Welcome'
        assert retval
        return retval

    def set_greeting(self, g):
        self.pageTemplate.title = g

    greeting = property(get_greeting, set_greeting, greeting_doc)

    message_doc = u'The Welcome message on the site.'

    @Lazy
    def defaultMsg(self):
        retval = 'Welcome to {0}.'.format(self.siteInfo.name)
        return retval

    def get_message(self):
        m = self.pageTemplate()
        retval = m if m else self.defaultMsg
        assert retval
        return retval

    def set_message(self, m):
        self.pageTemplate.write(m)

    message = property(get_message, set_message, message_doc)
