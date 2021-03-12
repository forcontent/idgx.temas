# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import idgx.temas


class IdgxTemasLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=idgx.temas)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'idgx.temas:default')


IDGX_TEMAS_FIXTURE = IdgxTemasLayer()


IDGX_TEMAS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IDGX_TEMAS_FIXTURE,),
    name='IdgxTemasLayer:IntegrationTesting',
)


IDGX_TEMAS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(IDGX_TEMAS_FIXTURE,),
    name='IdgxTemasLayer:FunctionalTesting',
)


IDGX_TEMAS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        IDGX_TEMAS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='IdgxTemasLayer:AcceptanceTesting',
)
