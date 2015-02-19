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
from __future__ import unicode_literals
from zope.interface.interface import Interface
from zope.schema import Text, TextLine
from zope.viewlet.interfaces import IViewletManager
from . import GSMessageFactory as _


class IChangeWelcome(Interface):

    greeting = TextLine(
        title=_('greeting-entry-label', 'Greeting'),
        description=_('greeting-entry-description', 
            'The greeting that appears in the Welcome message'),
        required=True,
        default=_('default-greeting', 'Welcome'))

    message = Text(
        title=_('welcome-message-entry-label', 'Message'),
        description=_('welcome-message-entry-description', 
            'The text of the message that appears on the site homepage.'),
        required=True)


class IWelcomeBox(IViewletManager):
    '''The Welcome box.'''
