# -*-coding:Utf-8 -*

"""Module that contains the plugin main configuration.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

Note that the plugin stores information in two files:

* A configuration file for the main informations
* A CSV file for the list of cities (see cityList).

"""

import config
import configobj
from cStringIO import StringIO
import os
import validate

# Configspec of the file
CONFIGSPEC = StringIO("""
# Location ID (refer to the owmCity.csv file)
location=integer(default=1)
""")

class ConfigFile:

	"""Wrapper around the configuration file.

	This class is instanciated in the same module.  Therefore, to
	access the configuration from somewhere in the plugin, all you
	need to do is:
	>>> from pluginConfig import configFile

	"""

	def __init__(self):
		path = os.path.join(config.getUserDefaultConfigPath(), "owm", "owm.ini")
		self.config = configobj.ConfigObj(path, configspec=CONFIGSPEC)
		val = validate.Validator()
		self.config.validate(val)

	def __getitem__(self, key):
		return self.config[key]

	def __setitem__(self, key, value):
		self.config[key] = value

configFile = ConfigFile()
