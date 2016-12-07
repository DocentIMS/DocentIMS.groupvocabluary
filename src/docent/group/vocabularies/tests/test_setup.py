# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from docent.group.vocabularies.testing import DOCENT_GROUP_VOCABULARIES_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that docent.group.vocabularies is properly installed."""

    layer = DOCENT_GROUP_VOCABULARIES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if docent.group.vocabularies is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'docent.group.vocabularies'))

    def test_browserlayer(self):
        """Test that IDocentGroupVocabulariesLayer is registered."""
        from docent.group.vocabularies.interfaces import (
            IDocentGroupVocabulariesLayer)
        from plone.browserlayer import utils
        self.assertIn(IDocentGroupVocabulariesLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = DOCENT_GROUP_VOCABULARIES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['docent.group.vocabularies'])

    def test_product_uninstalled(self):
        """Test if docent.group.vocabularies is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'docent.group.vocabularies'))

    def test_browserlayer_removed(self):
        """Test that IDocentGroupVocabulariesLayer is removed."""
        from docent.group.vocabularies.interfaces import \
            IDocentGroupVocabulariesLayer
        from plone.browserlayer import utils
        self.assertNotIn(IDocentGroupVocabulariesLayer,
                         utils.registered_layers())
