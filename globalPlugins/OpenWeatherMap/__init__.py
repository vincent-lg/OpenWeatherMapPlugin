"""NVDA OpenWeatherMap plugin.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

import globalPluginHandler
import os
import sys
import ui

PLUGIN_DIR = os.path.dirname(__file__)

# Add bundled copy of PIL to module search path.
sys.path.append(PLUGIN_DIR)

from tinyowm import Client

del sys.path[-1]

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_announceOWMForecast(self, gesture):
		client = Client.query("http://api.openweathermap.org/data/2.5/weather", {
			"q": "Hanford,us",
		})
		temperature = client.get_temperature()
		ui.message("Temperatature: " + str(temperature))

	__gestures={
		"kb:NVDA+w": "announceOWMForecast",
	}
