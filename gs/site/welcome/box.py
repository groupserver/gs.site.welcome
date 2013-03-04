# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from gs.viewlet import SiteViewlet
from message import WelcomeMessage


class WelcomeBox(SiteViewlet):

    def __init__(self, site, request, view, manager):
        super(WelcomeBox, self).__init__(site, request, view, manager)

    @Lazy
    def welcomeMessage(self):
        retval = WelcomeMessage(self.siteInfo)
        return retval