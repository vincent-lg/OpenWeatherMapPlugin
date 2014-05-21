# -*-coding:Utf-8 -*

"""Module containing the unittest for the forecasts.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

import unittest

from tinyowm.tests.client import *
from tinyowm.forecast import Forecast

class TestForecast(unittest.TestCase):

	"""Unittests to check that the right informations are extracted."""

	def setUp(self):
		"""Setup all the forecasts."""
		self.forecasts = {}
		for name in WEATHER_CONDITIONS.keys():
			self.forecasts[name] = Client.queryWeather(name).forecast

	def testMainWeather(self):
		"""Test the main weather."""
		values = {
				"Milan,it": "Sky is Clear",
		}

		for name, value in values.items():
			self.assertEqual(self.forecasts[name].getMainWeather(), value)

	def testTemperature(self):
		"""Test the temperature."""
		values = {
				"Milan,it": 287.57,
		}

		for name, value in values.items():
			self.assertEqual(self.forecasts[name].getTemperature().kelvin,
					value)

	def testCloudiness(self):
		"""Test the cloudiness."""
		values = {
				"Milan,it": 0,
		}

		for name, value in values.items():
			self.assertEqual(self.forecasts[name].getCloudiness(), value)
