# -*- coding: utf-8 -*-
"""Propertyshelf MLS Nica."""

# python imports
import logging

# zope imports
from zope.i18nmessageid import MessageFactory

# local imports
from ps.diazo.mlsnica import config

logger = logging.getLogger(config.PROJECT_NAME)
_ = MessageFactory('ps.diazo.mlsnica')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
