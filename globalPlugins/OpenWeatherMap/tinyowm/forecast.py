# -*-coding:Utf-8 -*

"""Module containing the tinyowm.Forecast class.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

from datetime import datetime
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

	def getCityName(self):
		"""Return the city name."""
		return self.data.get("name")

	def getLastUpdated(self):
		"""Return the datetime.datetime of the last updated time (dt)."""
		dt = self.data.get("dt")
		if dt:
			return datetime.fromtimestamp(dt)

		return None

	def getCloudiness(self):
		"""Return the cloudiness in percent."""
		clouds = self.data.get("clouds")
		if clouds:
			cloudiness = clouds.get("all")
			if cloudiness is not None:
				return cloudiness

		return None

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

	def getMainWeather(self):
		"""Return the first weather."""
		weather = self.data.get("weather")
		if weather:
			weather = weather[0]
			return weather.get("description")

		return None

	def getMessage(self):
		"""Return the message (temporary method)."""
		msg = u"{cityName}, {weather}, {temperature}°C, " \
				u"cloudiness={cloudiness}%, last updated {lastUpdated}"
		return msg.format(cityName=self.getCityName(), weather=self.getMainWeather(),
		temperature=self.getTemperature().celsius, cloudiness=self.getCloudiness(),
		lastUpdated=self.getLastUpdated())
