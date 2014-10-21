#!/usr/bin/python

import unittest
import model

class TestCalBus(unittest.TestCase):
	def setUp(self):
		self._bus = model.CalBus()
		self._bus.clear_bus()

	def testSingleton(self):
		bus2 = model.CalBus()
		self.assertEqual(self._bus, bus2)

	def testOneDigitalOperation(self):
		self.assertEqual("1", self._bus.send_user_input(1))
		self.assertEqual("1+", self._bus.send_user_input('+'))
		self.assertEqual("1+2", self._bus.send_user_input(2))
		self.assertEqual("3", self._bus.send_user_input('='))

	def testTwoDigitalOperation(self):
		self.assertEqual("1", self._bus.send_user_input(1))
		self.assertEqual("19", self._bus.send_user_input(9))
		self.assertEqual("19*", self._bus.send_user_input('*'))
		self.assertEqual("19*2", self._bus.send_user_input(2))
		self.assertEqual("38", self._bus.send_user_input('='))

	def testContinuesOperation(self):
		self.assertEqual("4", self._bus.send_user_input(4))
		self.assertEqual("45", self._bus.send_user_input(5))
		self.assertEqual("45*", self._bus.send_user_input('*'))
		self.assertEqual("45*2", self._bus.send_user_input(2))
		self.assertEqual("90", self._bus.send_user_input('='))
		self.assertEqual("90/", self._bus.send_user_input('/'))
		self.assertEqual("90/1", self._bus.send_user_input(1))
		self.assertEqual("90/10", self._bus.send_user_input(0))
		self.assertEqual("9", self._bus.send_user_input('='))

	def testLongExpression(self):
		self.assertEqual("1", self._bus.send_user_input(1))
		self.assertEqual("12", self._bus.send_user_input(2))
		self.assertEqual("12*", self._bus.send_user_input('*'))
		self.assertEqual("12*3", self._bus.send_user_input(3))
		self.assertEqual("12*3-", self._bus.send_user_input('-'))
		self.assertEqual("12*3-6", self._bus.send_user_input(6))
		self.assertEqual("12*3-6/", self._bus.send_user_input('/'))
		self.assertEqual("12*3-6/2", self._bus.send_user_input(2))
		self.assertEqual("33", self._bus.send_user_input('='))

	def testClearBus(self):
		self._bus.clear_bus()
		self.assertEqual("", self._bus._show_expression())
	

if __name__ == '__main__':
	unittest.main()
