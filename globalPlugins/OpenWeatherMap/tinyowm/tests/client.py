# -*-coding:Utf-8 -*

"""Module containing the modified client.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

from tinyowm.client import Client as OriginalClient
from tinyowm.forecast import Forecast

class Client(OriginalClient):

	"""This class is used to create a kind of mock client.

	This client doesn't really query the API, though it still returns
	information that can be used by other modules.  For instance, you
	can ask this mock client to retrieve the weather in Milan, Italy.
	The client will return fake weather conditions that can be used
	for testing.

	"""

	@classmethod
	def queryWeather(cls, cityName):
		"""Mock for querying the API to get the weather condition in a city."""
		client = cls(None, {"q": cityName})
		content = WEATHER_CONDITIONS[cityName]
		client.forecast = Forecast.buildFromJSON(content)

		return client

# Constants for the client
WEATHER_CONDITIONS = {
	"Milan,it": """{
		"coord":{
			"lon":9.18,
			"lat":45.47
		},
		"sys":{
			"message":0.0132,
			"country":"Italy",
			"sunrise":1400643951,
			"sunset":1400698436
		},
		"weather":[
			{"id":800,"main":"Clear","description":"Sky is Clear","icon":"01d"}
		],
		"base":"cmc stations",
		"main":{
			"temp":287.57,
			"pressure":1019,
			"humidity":82,
			"temp_min":285.15,
			"temp_max":290.37
		},
		"wind":{
			"speed":1.86,
			"deg":41.0032
		},
		"clouds":{"all":0},
		"dt":1400647108,
		"id":3173435,
		"name":"Milan",
		"cod":200
	}""",
}