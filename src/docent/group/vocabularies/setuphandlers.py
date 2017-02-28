# -*- coding: utf-8 -*-
from plone import api
from plone.api.exc import GroupNotFoundError

from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

# from docent.group.vocabularies.vocabularies import (BOOSTER_BOARD_MEMBERS_GROUP_ID,
#                                                     ADVISORS_GROUP_ID,
#                                                     EXECUTIVE_COMMITTEE_GROUP_ID,
#                                                     LWHS_STAFF_MEMBERS_GROUP_ID,
#                                                     TRAINED_MEMBERS_GROUP_ID,
#                                                     BOOSTER_MEMBERS_GROUP_ID,)

from docent.group.vocabularies.app_config import GROUP_ID_DICT

@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'docent.group.vocabularies:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # create base groups if they do not exist
    group_ids = GROUP_ID_DICT.keys()
    for group_id in group_ids:
        try:
            group = api.group.get(groupname=group_id)
        except GroupNotFoundError:
            group = api.group.create(groupname=group_id,
                                     title=GROUP_ID_DICT.get(group_id, ''))

        if not group:
            api.group.create(groupname=group_id,
                             title=GROUP_ID_DICT.get(group_id, ''))


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
