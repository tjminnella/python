#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hello.py
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

from tkinter import *
from converters import *

class App:

    def __init__(self, master):
        self.t_conv = ScaleAndOffsetConverter('C', 'F', 1.8, 32)
        frame = Frame(master)
        frame.pack(fill=BOTH, expand=1)

        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)
        text = Text(master, yscrollcommand=scrollbar.set)
        text.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=text.yview)
        
        Label(frame, text='deg C').grid(row=0, column=0)
        
        self.c_var = DoubleVar()
        Entry(frame, textvariable=self.c_var).grid(row=0, column=1)
        
        Label(frame, text='deg F').grid(row=1, column=0)
        
        self.result_var = DoubleVar()
        Label(frame, textvariable=self.result_var).grid(row=1, column=1)
        
        button = Button(frame, text='Convert', command=self.convert)
        button.grid(row=2, columnspan=2)
        
        check_var = StringVar()
        check = Checkbutton(frame, text='Checkbutton',variable = check_var,onvalue='Y', offvalue='N')
        check.grid(row=3, columnspan=1)

        listbox = Listbox(frame, height=3, selectmode=BROWSE)
        for item in ['red', 'blue', 'green', 'yellow', 'black']:
            listbox.insert(END, item)
        listbox.grid(row=3, column=2)
        
        Spinbox(frame, values=('a','b','c')).grid(row=4)

        radio_frame = Frame(frame)
        radio_select = StringVar()
        b1 = Radiobutton(radio_frame, text='portraite', variable=radio_select, value='P')
        b1.pack(side=LEFT)
        b2 = Radiobutton(radio_frame, text='landscape', variable=radio_select, value='L')
        radio_frame.grid(row=5, column=2)

        listbox1 = Listbox(frame)
        for item in ['red', 'blue', 'green', 'yellow', 'black']:
            listbox1.insert(END, item)

        
        w = Scale ( master, option, ... )
        
        
    def convert(self):
        c = self.c_var.get()
        self.result_var.set(self.t_conv.convert(c))

root = Tk()
root.wm_title('Temp Converter')
app = App(root)
root.geometry("400x300+0+0")
root.mainloop()
              
        
