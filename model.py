#!/usr/bin/python

import Tkinter
from operator import add, sub, mul, div

import view

def singleton(class_):
	instances = {}
	def getinstance(*args, **kwargs):
		if class_ not in instances:
			instances[class_] = class_(*args, **kwargs)
		return instances[class_]
	return getinstance

@singleton
class CalBus(object):
	def __init__(self):
		self.ops = {'+':add, '-':sub, '*':mul, '/':div}
		self.ops_allowed = "+-*/="
		self._bus = []

	def clear_bus(self):
		self._bus = []

	def _getValueFromBus(self):
		if not self._bus:
			return "0"
		else:
			if len(self._bus) == 1:
				return str(self._bus[0])
			else:
				return self._show_expression()
		
	def send_user_input(self, user_input):
		retvalue = None
		if user_input in range(0, 10) or user_input in self.ops_allowed:
			if user_input == '=':	# end of experssion
				ret = self._cal_result()
				self._bus = [ret]	
				retvalue = str(ret)
			else:
				if (len(self._bus)>0) and type(self._bus[-1]) is int \
					and user_input in range(0,10):
					self._bus[-1] = self._bus[-1]*10 + user_input
				else:
					self._bus.append(user_input)
				retvalue = self._getValueFromBus()
			return retvalue

	def _cal_result(self):
            if (len(self._bus) != 3 or not type(self._bus[0]) == int \
                        or not type(self._bus[2]) == int):
                return "Error"
            else:
		        return str(self.ops[self._bus[1]](self._bus[0], self._bus[2]))

	def _show_expression(self):
		newbus = [str(x) for x in self._bus]
		return "".join(newbus)
