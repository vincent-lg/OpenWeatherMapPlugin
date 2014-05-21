# -*-coding:Utf-8 -*

"""Module containing the tinyowm.Temperature class.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

class Temperature:

	"""Class used to store a temperature.

	The temperature is available in three units:
		kelvin -- the temperature in kelvin
		fahrenheit -- the temperature in fahrenheit
		celsius -- the temperature in celsius.

	"""

	def __init__(self, kelvin, precision=2):
		self.kelvin = round(kelvin, precision)
		self.celsius = round(self.kelvinToCelsius(kelvin), precision)
		self.fahrenheit = round(self.kelvinToFahrenheit(kelvin), precision)

	def __str__(self):
		return "{0}oK {1}oC {2}oF".format(
				self.kelvin, self.celsius, self.fahrenheit)

	@staticmethod
	def kelvinToCelsius(kelvin):
		"""Return the celsius degrees corresponding to the kelvin degrees.

		It's quite easy: all you need is substracting 273.15 to the
		kelvin degrees.

		"""
		return kelvin - 273.15

	@staticmethod
	def kelvinToFahrenheit(kelvin):
		"""Return the fahrenheit degrees corresponding to the kelvin degrees.

		The formula is:
			° F = 9/5(K - 273.15) + 32

		"""
		return (9.0 / 5.0) * (kelvin - 273.15) + 32
