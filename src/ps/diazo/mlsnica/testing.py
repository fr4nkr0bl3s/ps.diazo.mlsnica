# -*- coding: utf-8 -*-
"""Test Layer for ps.diazo.mlsnica."""

# zope imports
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    PLONE_FIXTURE,
    applyProfile,
)
from plone.testing import (
    Layer,
    z2,
)
from zope.configuration import xmlconfig


class PsDiazoMlsnicaLayer(PloneSandboxLayer):
    """Custom Test Layer for ps.diazo.mlsnica."""
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        """Set up Zope for testing."""
        # Load ZCML
        import ps.diazo.mlsnica
        xmlconfig.file(
            'configure.zcml',
            ps.diazo.mlsnica,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ps.diazo.mlsnica:default')


PS_DIAZO_MLSNICA_FIXTURE = PsDiazoMlsnicaLayer()


PS_DIAZO_MLSNICA_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PS_DIAZO_MLSNICA_FIXTURE,),
    name='PsDiazoMlsnicaLayer:IntegrationTesting'
)


PS_DIAZO_MLSNICA_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PS_DIAZO_MLSNICA_FIXTURE,),
    name='PsDiazoMlsnicaLayer:FunctionalTesting'
)


PS_DIAZO_MLSNICA_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PS_DIAZO_MLSNICA_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PsDiazoMlsnicaLayer:AcceptanceTesting'
)


ROBOT_TESTING = Layer(name='ps.diazo.mlsnica:Robot')
