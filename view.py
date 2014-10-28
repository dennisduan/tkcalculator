#!/usr/bin/python

import Tkinter
from functools import partial
import model

class CalView(object):
    def __init__(self):
        self._bus = model.CalBus()
        
    	self.root = Tkinter.Tk()
    	v = Tkinter.StringVar()
    	self._label = v
    	ResultLabel = Tkinter.Label(self.root, textvariable=self._label, font="Times 16 bold")
    	ResultLabel.grid(row=0, column=0)

    	controls = []

    	#create digital buttons
    	for i in range(0,10):
    		btn = Tkinter.Button(self.root, text=str(i), command=partial(self.basic_cmd, i))
    		controls.append(btn)
    	#create operators buttons
    	for c in '+-*/=C':
    		btn = Tkinter.Button(self.root, text=c, command=partial(self.basic_cmd, c))
    		controls.append(btn)
    	#create clear button
        #btn = Tkinter.Button(self.root, text="C", command=self.clearResult)
        #controls.append(btn)
	
    	#align controls and pack them
    	for i in range(0, 4):
    		for j in range(0, 4):
    			if i*4+j >= len(controls):
    				 break
    			controls[i*4+j].grid(row=i+1, column=j)

    def show(self):
    	#main loop
    	self.root.mainloop()

    # DI, allow insert a new instance to mock the real bus instance
    def setCalBus(self, bus):
        self._bus = bus
        
    def clearResult(self):
    	self._bus.clear_bus()
    	self._label.set("")

    def basic_cmd(self, inp):
    	self._label.set(self._bus.send_user_input(inp))
