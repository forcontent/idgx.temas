# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from Products.CMFPlone.interfaces import ISiteSchema
from plone.formwidget.namedfile.converter import b64encode_file
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.interface import implementer
import os


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'idgx.temas:uninstall',
        ]


def get_file(filename):
    """Return contents of file from current directory."""
    path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(path, 'browser/static', filename)
    with open(path, 'rb') as f:
        return f.read()


def logo(context, remove=False):
    registry = getUtility(IRegistry)
    settings = registry.forInterface(ISiteSchema, prefix="plone", check=False)

    filename = 'logo.png'
    b64 = b64encode_file(filename, get_file(filename))

    if hasattr(settings, 'site_logo'):
        if remove:
            setattr(settings, 'site_logo', '')
        else:
            setattr(settings, 'site_logo', b64)


def post_install(context):
    """Post install script"""
    logo(context)


def uninstall(context):
    """Uninstall script"""
    logo(context, remove=True)
