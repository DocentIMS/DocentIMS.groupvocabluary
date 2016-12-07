# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import transaction
from zope.schema.vocabulary import getVocabularyRegistry

from docent.group.vocabularies.testing import DOCENT_GROUP_VOCABULARIES_INTEGRATION_TESTING  # noqa

import unittest

GROUP_IDS = ['Booster_Board_Members',
             'Advisors',
             'Executive_Committee',
             'LWHS_Staff_Members',
             'Trained_Members']

MEMBER_PROPERTIES = {'member_a':{'fullname':'Member A'},
                     'member_b':{'fullname':'Member B'},
                     'member_c':{'fullname':'Member C'}
                    }

class DocentGroupVocabulariesIntegrationTest(unittest.TestCase):

    layer = DOCENT_GROUP_VOCABULARIES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_vocabularies(self):

        booster_board_members_vocab = getVocabularyRegistry().get(None, u"docent.group.Booster_Board_Members")
        advisors_members_vocab = getVocabularyRegistry().get(None, u"docent.group.Advisors")
        executive_members_vocab = getVocabularyRegistry().get(None, u"docent.group.Executive_Committee")
        lwhs_staff_members_vocab = getVocabularyRegistry().get(None, u"docent.group.LWHS_Staff_Members")
        trained_members_vocab = getVocabularyRegistry().get(None, u"docent.group.Trained_Members")

        #libraries should have no members
        self.assertEqual(len(booster_board_members_vocab), 1)
        self.assertEqual(len(advisors_members_vocab), 1)
        self.assertEqual(len(executive_members_vocab), 1)
        self.assertEqual(len(lwhs_staff_members_vocab), 1)
        self.assertEqual(len(trained_members_vocab), 1)

        self.assertEqual(booster_board_members_vocab.getTerm('no_members').value, 'no_members')
        self.assertEqual(advisors_members_vocab.getTerm('no_members').value, 'no_members')
        self.assertEqual(executive_members_vocab.getTerm('no_members').value, 'no_members')
        self.assertEqual(lwhs_staff_members_vocab.getTerm('no_members').value, 'no_members')
        self.assertEqual(trained_members_vocab.getTerm('no_members').value, 'no_members')

        #lets create groups and re initialize vocabularies
        for group_id in GROUP_IDS:
            api.group.create(groupname=group_id)

        #let's create our users too, but not assign them to groups
        for member_id in MEMBER_PROPERTIES.keys():
            api.user.create(username=member_id,
                            email='%s@email.com' % member_id,
                            properties=MEMBER_PROPERTIES[member_id])

        booster_board_members_vocab = getVocabularyRegistry().get(None, u"docent.group.Booster_Board_Members")
        advisors_members_vocab = getVocabularyRegistry().get(None, u"docent.group.Advisors")
        executive_members_vocab = getVocabularyRegistry().get(None, u"docent.group.Executive_Committee")
        lwhs_staff_members_vocab = getVocabularyRegistry().get(None, u"docent.group.LWHS_Staff_Members")
        trained_members_vocab = getVocabularyRegistry().get(None, u"docent.group.Trained_Members")

        #libraries should have no members
        self.assertEqual(len(booster_board_members_vocab), 1)
        self.assertEqual(len(advisors_members_vocab), 1)
        self.assertEqual(len(executive_members_vocab), 1)
        self.assertEqual(len(lwhs_staff_members_vocab), 1)
        self.assertEqual(len(trained_members_vocab), 1)

        self.assertEqual(booster_board_members_vocab.getTerm('no_members').value, 'no_members')
        self.assertEqual(advisors_members_vocab.getTerm('no_members').value, 'no_members')
        self.assertEqual(executive_members_vocab.getTerm('no_members').value, 'no_members')
        self.assertEqual(lwhs_staff_members_vocab.getTerm('no_members').value, 'no_members')
        self.assertEqual(trained_members_vocab.getTerm('no_members').value, 'no_members')

        #let's add members to groups now
        api.group.add_user(groupname='Booster_Board_Members',username='member_a')
        api.group.add_user(groupname='Advisors',username='member_b')
        api.group.add_user(groupname='Executive_Committee',username='member_c')
        api.group.add_user(groupname='LWHS_Staff_Members',username='member_a')
        api.group.add_user(groupname='LWHS_Staff_Members',username='member_b')
        api.group.add_user(groupname='Trained_Members',username='member_b')
        api.group.add_user(groupname='Trained_Members',username='member_c')

        booster_board_members_vocab = getVocabularyRegistry().get(None, u"docent.group.Booster_Board_Members")
        advisors_members_vocab = getVocabularyRegistry().get(None, u"docent.group.Advisors")
        executive_members_vocab = getVocabularyRegistry().get(None, u"docent.group.Executive_Committee")
        lwhs_staff_members_vocab = getVocabularyRegistry().get(None, u"docent.group.LWHS_Staff_Members")
        trained_members_vocab = getVocabularyRegistry().get(None, u"docent.group.Trained_Members")

        #libraries should have members
        self.assertEqual(len(booster_board_members_vocab), 1)
        self.assertEqual(len(advisors_members_vocab), 1)
        self.assertEqual(len(executive_members_vocab), 1)
        self.assertEqual(len(lwhs_staff_members_vocab), 2)
        self.assertEqual(len(trained_members_vocab), 2)

        #verify which members
        self.assertEqual(booster_board_members_vocab.getTerm('member_a').value, 'member_a')
        self.assertEqual(advisors_members_vocab.getTerm('member_b').value, 'member_b')
        self.assertEqual(executive_members_vocab.getTerm('member_c').value, 'member_c')
        self.assertEqual(lwhs_staff_members_vocab.getTerm('member_a').value, 'member_a')
        self.assertEqual(lwhs_staff_members_vocab.getTerm('member_b').value, 'member_b')
        self.assertEqual(trained_members_vocab.getTerm('member_b').value, 'member_b')
        self.assertEqual(trained_members_vocab.getTerm('member_c').value, 'member_c')

        self.assertEqual(booster_board_members_vocab.getTerm('member_a').title, 'Member A')
        self.assertEqual(advisors_members_vocab.getTerm('member_b').title, 'Member B')
        self.assertEqual(executive_members_vocab.getTerm('member_c').title, 'Member C')
        self.assertEqual(lwhs_staff_members_vocab.getTerm('member_a').title, 'Member A')
        self.assertEqual(lwhs_staff_members_vocab.getTerm('member_b').title, 'Member B')
        self.assertEqual(trained_members_vocab.getTerm('member_b').title, 'Member B')
        self.assertEqual(trained_members_vocab.getTerm('member_c').title, 'Member C')

        print 'all done!'