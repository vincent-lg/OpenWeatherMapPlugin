"""Module containing the CityList class.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

import csv
import os

class CityList:

	"""Class containing the csv definition of the city list.

	An object from this class is created in the same module, so
	all you need to do to use it from a different module is:
	>>> from cityList import cityList

	With the standard configuration (see globalConfig.py), it is
	used to store specific information about the OpenWeatherMap
	globalPlugin.  Its purpose is merely to store the list of cities
	and locations in a CSV format.  In the configuration file, the
	location is selected through a simple ID that matches the line
	number in the CSV file.  For instance, if the csv file looks
	like this:
		ID;name;cityID;lat;lon
		1;Berlin;2950159;;
		2;New York city;5128581;;
	(the first line is not present.)
	And the ini file indicates:
		location=2
	Then the default location is New York.

	"""

	def __init__(self):
		self.path = "cityList.csv"
		self.cityList = []

	def retrieve(self):
		"""Retrieve the CSV configuration if the file exists.

		If the file doesn't exist, a defautl list of cities is created.

		Note that this method should be called when the 'path' attribute
		is configured.  This module does create a cityList object but
		doesn't call its 'retrieve' method.  The reason is that this
		file should be used in a separated context from the global
		plugin itself.  Therefore, when you want to access or write
		the NVDA configuration, you should first import the cityList
		object, then set its 'path' attribute, then call its
		'retrieve' method.

		"""
		if os.path.exists(self.path):
			with open(self.path, 'rb') as file:
				reader = csv.reader(file)
				for line in reader:
					self.cityList.append(line)
		else:
			self.cityList = [
				(1, "Berlin", 2950159, None, None),
				(2, "New York city",5128581, None, None),
			]

	def store(self):
		"""Write the CSV file."""
		with open(self.path, 'wb') as file:
			writer = csv.writer(file)
			writer.writerows(self.cityList)

cityList = CityList()
