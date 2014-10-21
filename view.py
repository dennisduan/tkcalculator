#!/usr/bin/python

import Tkinter
from functools import partial
import model

class CalView(object):
    def __init__(self):
        
    	root = Tkinter.Tk()
    	v = Tkinter.StringVar()
    	self._label = v
    	ResultLabel = Tkinter.Label(root, textvariable=self._label, font="Times 16 bold")
    	ResultLabel.grid(row=0, column=0)

    	controls = []

    	#create digital buttons
    	for i in range(0,10):
    		btn = Tkinter.Button(root, text=str(i), command=partial(self.basic_cmd, i))
    		controls.append(btn)
    	#create operators buttons
    	for c in '+-*/=':
    		btn = Tkinter.Button(root, text=c, command=partial(self.basic_cmd, c))
    		controls.append(btn)
    	#create clear button
    	btn = Tkinter.Button(root, text="C", command=self.clearResult)
    	controls.append(btn)
	
    	#align controls and pack them
    	for i in range(0, 4):
    		for j in range(0, 4):
    			if i*4+j >= len(controls):
    				 break
    			controls[i*4+j].grid(row=i+1, column=j)

    	#main loop
    	root.mainloop()
        
    def clearResult(self):
    	model.CalBus().clear_bus()
    	self._label.set("")


    def basic_cmd(self, inp):
    	self._label.set(model.CalBus().send_user_input(inp))
