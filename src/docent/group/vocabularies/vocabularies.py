
from plone import api
from plone.api.exc import GroupNotFoundError

from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implementer

# BOOSTER_BOARD_MEMBERS_GROUP_ID = 'Booster_Board_Members'
# ADVISORS_GROUP_ID = 'Advisors'
# EXECUTIVE_COMMITTEE_GROUP_ID = 'Executive_Committee'
# LWHS_STAFF_MEMBERS_GROUP_ID = 'LWHS_Staff_Members'
# TRAINED_MEMBERS_GROUP_ID = 'Trained_Members'
# BOOSTER_MEMBERS_GROUP_ID = 'Booster_Members'

from docent.group.vocabularies.app_config import (BOOSTER_BOARD_MEMBERS_GROUP_ID,
                                                  ADVISORS_GROUP_ID,
                                                  EXECUTIVE_COMMITTEE_GROUP_ID,
                                                  LWHS_STAFF_MEMBERS_GROUP_ID,
                                                  TRAINED_MEMBERS_GROUP_ID,
                                                  BOOSTER_MEMBERS_GROUP_ID,)

def getGroupMemberVocabulary(group_name):
    """Return a set of groupmembers, return an empty set if group not found
    """
    try:
        group_members = api.user.get_users(groupname=group_name)
    except GroupNotFoundError:
        group_members = ()

    terms = []

    if group_members:
        terms.append(SimpleVocabulary.createTerm('', '', 'Choose One'))
        for member_data in group_members:
            member_id = member_data.getId()
            member_fullname = member_data.getProperty('fullname')

            terms.append(SimpleVocabulary.createTerm(member_id, str(member_id), member_fullname))
    else:
        terms.append(SimpleVocabulary.createTerm('no_members', 'no_members', 'No Members'))

    return SimpleVocabulary(terms)

@implementer(IVocabularyFactory)
class IBoosterBoardMembersVocabulary(object):
    """
    build a vocabulary based on a the Booster Board Member Group
    """
    def __call__(self, context):
        return getGroupMemberVocabulary(BOOSTER_BOARD_MEMBERS_GROUP_ID)
IBoosterBoardMembersVocabularyFactory = IBoosterBoardMembersVocabulary()


@implementer(IVocabularyFactory)
class IAdvisorsVocabulary(object):
    """
    build a vocabulary based on a the Advisors Group
    """
    def __call__(self, context):
        return getGroupMemberVocabulary(ADVISORS_GROUP_ID)
IAdvisorsVocabularyFactory = IAdvisorsVocabulary()


@implementer(IVocabularyFactory)
class IExecutiveCommitteeVocabulary(object):
    """
    build a vocabulary based on a the Executive Committee Group
    """
    def __call__(self, context):
        return getGroupMemberVocabulary(EXECUTIVE_COMMITTEE_GROUP_ID)
IExecutiveCommitteeVocabularyFactory = IExecutiveCommitteeVocabulary()


@implementer(IVocabularyFactory)
class ILWHSStaffMembersVocabulary(object):
    """
    build a vocabulary based on a the LWHS Staff Member Group
    """
    def __call__(self, context):
        return getGroupMemberVocabulary(LWHS_STAFF_MEMBERS_GROUP_ID)
ILWHSStaffMembersVocabularyFactory = ILWHSStaffMembersVocabulary()


@implementer(IVocabularyFactory)
class ITrainedMembersVocabulary(object):
    """
    build a vocabulary based on a the Trained Member Group
    """
    def __call__(self, context):
        return getGroupMemberVocabulary(TRAINED_MEMBERS_GROUP_ID)
ITrainedMembersVocabularyFactory = ITrainedMembersVocabulary()

@implementer(IVocabularyFactory)
class IBoosterMembersVocabulary(object):
    """
    build a vocabulary based on a the Booster Members Group
    """
    def __call__(self, context):
        return getGroupMemberVocabulary(BOOSTER_MEMBERS_GROUP_ID)
IBoosterMembersVocabularyFactory = IBoosterMembersVocabulary()