# -*- coding: utf-8 -*-
from zope.interface.interface import Interface
from zope.schema import Text, TextLine
from zope.viewlet.interfaces import IViewletManager


class IChangeWelcome(Interface):

    greeting = TextLine(title=u'Greeting',
                        description=u'The greeting that appears in the '
                            u'Welcome message',
                        required=True,
                        default=u'Welcome')

    message = Text(title=u'Message',
                    description=u'The text of the message that appears on the '
                        u'site homepage.',
                    required=True)


class IWelcomeBox(IViewletManager):
    '''The Welcome box.'''
