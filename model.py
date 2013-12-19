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

	def clearBus(self):
		self._bus = []

	def getValueFromBus(self):
		if not self._bus:
			return "0"
		else:
			if len(self._bus) == 1:
				return self._bus[0]
			else:
				return self.show_expression()
		
	def send_user_input(self, user_input):
		if user_input in range(0, 10) or user_input in self.ops_allowed:
			if user_input == '=':	# end of experssion
				ret = int(self.cal_result())
				self._bus = [ret]	# clear _bus after calculation
				return ret
			else:
				if (len(self._bus)>0) and (self._bus[-1] in range(0, 10) \
					and user_input in range(0,10)):
					self._bus[-1] = self._bus[-1]*10 + user_input
				else:
					self._bus.append(user_input)
				return self.getValueFromBus()

	def cal_result(self):
		return str(self.ops[self._bus[1]](self._bus[0], self._bus[2]))

	def show_expression(self):
		newbus = [str(x) for x in self._bus]
		return "".join(newbus)



