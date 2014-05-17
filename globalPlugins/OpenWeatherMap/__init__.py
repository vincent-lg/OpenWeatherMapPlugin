import globalPluginHandler
import os
import sys
import urllib
import ui

PLUGIN_DIR = os.path.dirname(__file__)

# Add bundled copy of PIL to module search path.
sys.path.append(PLUGIN_DIR)
import json
import urllib2
del sys.path[-1]

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_announceNVDAVersion(self, gesture):
		response = urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Hanford,us")
		content = response.read()
		ui.message(content)

	__gestures={
		"kb:NVDA+w": "announceNVDAVersion",
	}
