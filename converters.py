#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  converters.py
#  
#  Copyright 2019  <pi@DukeLover>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#

class ScaleAndOffsetConverter:

    def __init__(self, units_from, units_to, factor, offset):
                self.units_from = units_from
                self.units_to = units_to
                self.factor = factor
                self.offset = offset

    def description(self, value):
                return 'Convert ' + self.units_from + ' to ' + self.units_to
    
    def convert(self, value):
                return value * self.factor + self.offset
