#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 08 discussion 02."""
from generic_stove import GenericStove


class RangeWithOven(GenericStove):
    def __init__(self):
        GenericStove.__init__(self)
        self.oven_temp = 0
        self.heating = False

    def toggle_oven(self, on=False, oven_temp=0):
        if not on or oven_temp <= 0:
            self.heating = False
            return
        self.heating = True
        self.oven_temp = oven_temp