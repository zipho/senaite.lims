# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS.
#
# SENAITE.LIMS is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2018-2019 by it's authors.
# Some rights reserved, see README and LICENSE.

from senaite.impress import logger
from senaite.lims.setuphandlers import setup_html_filter

PROFILE_ID = "profile-senaite.lims:default"


def to_1000(portal_setup):
    """Initial version to 1000

    :param portal_setup: The portal_setup tool
    """

    logger.info("Run all import steps from SENAITE LIMS ...")
    context = portal_setup._getImportContext(PROFILE_ID)
    portal = context.getSite()
    setup_html_filter(portal)
    portal_setup.runAllImportStepsFromProfile(PROFILE_ID)
    logger.info("Run all import steps from SENAITE LIMS [DONE]")
