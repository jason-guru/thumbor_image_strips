#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

__version__ = '0.1.0'

try:
    from watermark_image_strips_filter.strips import Filter  # NOQA
except ImportError:
    logging.exception('Could not import text_strips. Probably due to setup.py installing it.')