"""Module containing the tinyowm.Forecast class.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

import json

from tinyowm.temperature import Temperature

class Forecast:

	"""Tiny forecast class used to represent a simple forecast.

	It usually proceeds from a JSON object so the way to create it is
	to use the 'buildFromJSON' class method and not the constructor
	itself.  Several methods can be used to retrieve specific information
	such as the temperature, the wind direction, the main condition,
	and so on.

	"""

	def __init__(self, data):
		self.data = data

	@classmethod
	def buildFromJSON(cls, json_data):
		"""Build the forecast from the specified JSON."""
		# Try to parse the response
		data = json.loads(json_data)
		forecast = cls(data)
		return forecast

	def getTemperature(self):
		"""Get the temperature.

		It returns a Temperature object with the current temperature in three
		units: kalvin, fahrenheit and celsius.

		"""
		main = self.data.get("main")
		if main:
			temp = main.get("temp")
			if temp:
				return Temperature(temp)

		return None
