# -*- coding: utf-8 -*-
"""Common interface definitions for ps.diazo.mlsnica."""

# zope imports
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IPsDiazoMlsnicaLayer(IDefaultBrowserLayer):
    """Marker interface that defines a Zope 3 browser layer."""
