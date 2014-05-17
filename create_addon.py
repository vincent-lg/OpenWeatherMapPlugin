"""This script creates the addon file (.nvda-addon).

It should be called to create the nvda-addon file from the source
tree.  Are included:
  manifest.ini -- the file describing the add-on
  globalPlugins -- the path containing the global plugin itself

"""

import os
from zipfile import ZipFile

def recursiveWrite(archive, path):
	"""Write into the archive the path and its content."""
	archive.write(path)
	if os.path.isfile(path):
		return

	for subpath in os.listdir(path):
		subpath = "/".join((path, subpath))
		if not subpath.endswith(".pyc"):
			recursiveWrite(archive, subpath)

with ZipFile('OpenWeatherMapPlugin.nvda-addon', 'w') as archive:
	archive.write("manifest.ini")
	recursiveWrite(archive, "globalPlugins")
