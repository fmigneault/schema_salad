from __future__ import absolute_import

import logging

__author__ = "peter.amstutz@curoverse.com"

_logger = logging.getLogger("salad")
_logger.addHandler(logging.StreamHandler())
_logger.setLevel(logging.INFO)
