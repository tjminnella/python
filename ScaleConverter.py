#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ScaleConverter.py
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
class ScalConverter:

    def __int__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to
        self.factor = factor

    def description(self):
        return 'Convert ' + self.units_from + ' to ' + self.units_to

    def convert(self, value):
        return value * self.factor

c1 = ScalConverter('inches', 'mm', 25)
print(c1.description())
print('converting 2 inches')
print(str(str(c1.convert(2)) + c1.units_to)
