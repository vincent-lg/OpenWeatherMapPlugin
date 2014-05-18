# -*-coding:Utf-8 -*

"""Module containing the tinyowm.Temperature class.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

class Temperature:

	"""Class used to store a temperature.

	The temperature is available in three units:
		kalvin -- the temperature in kalvin
		fahrenheit -- the temperature in fahrenheit
		celsius -- the temperature in celsius.

	"""

	def __init__(self, kalvin, precision=2):
		self.kalvin = round(kalvin, precision)
		self.celsius = round(self.kalvinToCelsius(kalvin), precision)
		self.fahrenheit = round(self.kalvinToFahrenheit(kalvin), precision)

	def __str__(self):
		return "{0}oK {1}oC {2}oF".format(
				self.kalvin, self.celsius, self.fahrenheit)

	@staticmethod
	def kalvinToCelsius(kalvin):
		"""Return the celsius degrees corresponding to the kalvin degrees.

		It's quite easy: all you need is substracting 273.15 to the
		kalvin degrees.

		"""
		return kalvin - 273.15

	@staticmethod
	def kalvinToFahrenheit(kalvin):
		"""Return the fahrenheit degrees corresponding to the kalvin degrees.

		The formula is:
			° F = 9/5(K - 273.15) + 32

		"""
		return (9.0 / 5.0) * (kalvin - 273.15) + 32
