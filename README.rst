===================
``gs.site.welcome``
===================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Welcome message on a GroupServer Site
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2014-10-24
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

Introduction
============

The `Welcome Box`_ shows the introductory text on the homepage of
a GroupServer_ site. It is made up of two parts.

Greeting: 
  A short greeting that is the first part of the welcome. It is
  shown as a header.

Message:
  A longer HTML message that forms the bulk of the welcome.

The welcome is modified by the `Change page`_. Both the Welcome
Box and the Change page use the `WelcomeMessage class`_.

Welcome Box
===========

The *Welcome Box* is a viewlet_ for displaying the introductory
text in the main part of the site homepage. It is made up of a
header, and a *viewlet manager*
(``gs.site.welcome.interfaces.IWelcomeBox``). Two viewlets are
provided by this product for the Welcome Box: one to provide the
message, and another to provide a link to the `Change page`_

Change Page
===========

The *Change* page ``/admin_changewelcome.html`` is used by the
site-administrator to change the welcome message. The form uses
the ``WelcomeMessage`` class to change both the greeting and the
message.

The Change page is linked from a viewlet that is added to the
`Welcome Box`_

``WelcomeMessage`` Class
========================

The ``gs.site.welcome.WelcomeMessage`` class is used to get or
set the welcome message. It has two properties for the
``greeting`` and ``message``.  The properties themselves are
stored in the ``welcome`` page template in the site-folder.

If the page template does not exist then the ``WelcomeMessage``
class will create it (with the identifier
``WelcomeMessage.welcomeId``), and populate it with default
values (``WelcomeMessage.defaultGreeting`` and
``WelcomeMessage.defaultMsg`` for the greeting and message
respectively.

Resources
=========

- Code repository: https://github.com/groupserver/gs.site.welcome/
- Questions and comments to http://groupserver.org/groups/development/
- Report bugs at https://redmine.iopen.net/projects/groupserver/

.. _onlinegroups.net: http://onlinegroups.net/
.. _GroupServer.org: http://groupserver.org/
.. _GroupServer: http://groupserver.org/
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/
.. _viewlet: http://docs.zope.org/zope.viewlet/
