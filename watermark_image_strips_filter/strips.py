#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import urllib2
from PIL import ImageOps, Image, ImageFont, ImageDraw
from thumbor.filters import BaseFilter, filter_method


class Filter(BaseFilter):
    @filter_method(
        BaseFilter.String,#logo url
    )
    def image_strips(self, logoUrl):
        backgroundImage = self.engine.image
        im = Image.open(urllib2.urlopen(logoUrl))
        self.engine.image = im