# -*-coding:Utf-8 -*

"""Module containing the unittest for temperature.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

import unittest

from tinyowm.temperature import Temperature

class TestTemperature(unittest.TestCase):

	"""Unittests for the temperature and the different conversions."""

	def setUp(self):
		"""Setup a default temperature."""
		self.temperature = Temperature(330)

	def testCelsius(self):
		"""Check that the kelvin to celsius convertion works."""
		self.assertEqual(self.temperature.celsius, 56.85)

	def testFahrenheit(self):
		"""Check that the kelvin to cfahrenheit conversion works."""
		self.assertEqual(self.temperature.fahrenheit, 134.33)
