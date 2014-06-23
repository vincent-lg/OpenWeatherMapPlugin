# -*-coding:Utf-8 -*

"""NVDA OpenWeatherMap plugin.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

import config
import os
import sys
import wx

import globalPluginHandler
import gui
from logHandler import log
import ui

PLUGIN_DIR = os.path.dirname(__file__)

# Add bundled copy of PIL to module search path.
sys.path.append(PLUGIN_DIR)

from interface.locationDialog import LocationDialog
from fetcher import Fetcher
from locationList import locationList
from pluginConfig import configFile
from tinyowm import Client

del sys.path[-1]

# Configuration de la configuration
locationList.path = os.path.join(config.getUserDefaultConfigPath(),
		"owm", "locations.csv")

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()

		# Creating the configuration directory
		configDir = os.path.join(config.getUserDefaultConfigPath(),
				"owm")
		if not os.path.exists(configDir):
			os.mkdir(configDir)

		# Add the settings in the NVDA menu
		self.prefsMenu = gui.mainFrame.sysTrayIcon.menu.GetMenuItems()[0].GetSubMenu()
		self.owmSettingsItem = self.prefsMenu.Append(wx.ID_ANY, "OWM Settings...", "Set OWM location")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onOWMSettings, self.owmSettingsItem)

		# Create the client to retrieve information from the API
		self.fetcher = Fetcher()
		self.fetcher.start()

	def script_announceOWMForecast(self, gesture):
		if self.fetcher.client is None:
			ui.message("Loading, please wait and try again in a few seconds...")
			return

		client = self.fetcher.client
		if client.error:
			ui.message("{0} {1}".format(client.statusCode, client.errorReason))
			self.fetcher.valid = False
			self.fetcher = Fetcher()
			self.fetcher.start()
		else:
			forecast = client.forecast
			message = forecast.getMessage()
			ui.message(message)
			log.info(message)

	def onOWMSettings(self, event):
		"""Pop a dialog with OWM settings."""
		locations = locationList.retrieve()
		selected = configFile['location']
		locationName = locationList.get(selected).name
		locationValues = {}
		for location in locations:
			locationValues[location.id] = (location.name, location.country)

		dialog = LocationDialog(gui.mainFrame, -1, "Select OWM Location",
				locationValues, locationName)
		gui.mainFrame.prePopup()
		ret = dialog.ShowModal()
		gui.mainFrame.postPopup()
		if ret == wx.ID_OK:
			log.info("Focused {0}, {1}".format(locationList.path,
					dialog.location.focusedLocationName))

	__gestures={
			"kb:NVDA+w": "announceOWMForecast",
	}
