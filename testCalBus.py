#!/usr/bin/python

import unittest
import tkcal

class TestCalBus(unittest.TestCase):
	def setUp(self):
		self._bus = tkcal.CalBus()

	def testSingleton(self):
		bus2 = tkcal.CalBus()
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

if __name__ == '__main__':
	unittest.main()
