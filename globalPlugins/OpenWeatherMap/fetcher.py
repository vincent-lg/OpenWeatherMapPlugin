# -*-coding:Utf-8 -*

"""Fetcher used to regularly retrieve information from the OWM API.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

import threading
import time

from logHandler import log
from tinyowm import Client

class Fetcher(threading.Thread):

	"""Thread that regularly retrieves information from the OWM API.

	It uses the tinyowm.Client class that is dedicated to connecting
	to the API and creating the useful objects depending on the API's
	answers.

	"""

	def __init__(self):
		threading.Thread.__init__(self)
		self.client = None

	def run(self):
		"""Run the thread.

		This method creates a new client each time, query the API and
		waits after the answer has been received.

		"""
		while True:
			self.query_API()
			time.sleep(900)

	def query_API(self):
		"""Query the API.

		This method creates a new client.

		"""
		log.info("Querying the API...")
		self.client = Client.queryWeather("Hanford,us")
