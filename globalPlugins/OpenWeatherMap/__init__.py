"""NVDA OpenWeatherMap plugin.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

import os
import sys

import globalPluginHandler
from logHandler import log
import ui

PLUGIN_DIR = os.path.dirname(__file__)

# Add bundled copy of PIL to module search path.
sys.path.append(PLUGIN_DIR)

from fetcher import Fetcher
from tinyowm import Client

del sys.path[-1]

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.fetcher = Fetcher()
		self.fetcher.start()

	def script_announceOWMForecast(self, gesture):
		if self.fetcher.client is None:
			ui.message("Loading, please wait and try again in a few seconds...")
			return

		client = self.fetcher.client
		if client.error:
			ui.message("{0} {1}".format(client.statusCode, client.errorReason))
		else:
			forecast = client.forecast
			message = forecast.getMessage()
			ui.message(message)
			log.info(message)

	__gestures={
		"kb:NVDA+w": "announceOWMForecast",
	}
