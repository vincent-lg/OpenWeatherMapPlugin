"""Module containing the Location class.

@author: Vincent Le Goff <vincent.legoff.srs@gmail.com>
@copyright: 2014 LE GOFF Vincent
@license: GNU General Public License version 2.0

"""

class Location:

	"""Class defining a location.

	A location is characterized by its name.  The name should be a unique
	identifier (that is, in the CSV file, only one location should
	correspond to a name).  If the location is a city (recognized by
	the OpenWeatherMap API), then it should indicate a cityID.
	Otherwise, its latitude and longitude should be indicated.  The name
	of the country could be specified too, but this data is not strictly
	necessary to the OpenWeatherMap API.

	"""

	def __init__(self, id=None, name=None, country=None, cityID=None,
			lat=None, lon=None):
		self.id = id
		self.name = name
		self.country = country
		self.cityID = cityID
		self.lat = lat
		self.lon = lon

	@property
	def tuple(self):
		"""Return a tuple of information to store."""
		return (self.id, self.name, self.country, self.cityID,
				self.lat, self.lon)
