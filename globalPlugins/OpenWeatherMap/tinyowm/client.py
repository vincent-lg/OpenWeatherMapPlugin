"""Module containing the tinyowm.Client class.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

import json
import urllib
import urllib2

class Client:

	"""Tiny client used to connect to the OpenWeatherMap API.

	This client perofms basics operations such as:
		Querying the API on a specific URL
		Handling the urllib2 errors
		Decoding the JSON response from the API
		Creating a corresponding tinyowm.Response object.

	"""

	def __init__(self, url, data):
		self.url = url
		self.data = data
		self.error = False
		self.statusCode = 200
		self.errorReason = None

	@classmethod
	def query(cls, url, data):
		"""Query the specified URL.

		The specified data should be in a dictionary and will be encoded
		into the GET URL.

		"""
		client = cls(url, data)
		encoded = urllib.urlencode(data)
		url += "?" + encoded
		request = urllib2.Request(url)
		try:
			response = urllib2.urlopen(request)
		except urllib2.HTTPError as err:
			client.error = True
			client.statusCode = err.code
		except urllib2.URLError as err:
			client.error = True
			client.errorReason = err.reason
		else:
			content = response.read()

			# Try to parse the response
			decoded = json.loads(content)
			client.answer = decoded

		return client

	def get_temperature(self):
		"""Get the temperature."""
		answer = self.answer
		main = answer.get("main")
		if main:
			temp = main.get("temp")
			if temp:
				return temp

		return None
