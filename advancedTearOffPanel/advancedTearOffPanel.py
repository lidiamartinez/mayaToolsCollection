__author__ = "Lidia Martinez Prado"
__copyright__ = "Copyright (C) 2017 Virtual Method Studio"
__license__ = "Public Domain"
__version__ = "1.0"
__doc__ = "Tear Off Viewport option in Maya does not allow to which camera the viewport uses. This one will create an advanced viewport window."


import maya.cmds as cmds
import time

global tearOffPanel
tearOffPanel = None

def main():
	# Grab the global variable
	global tearOffPanel

	# If it exists, show it instead of creating a new one
	if tearOffPanel and cmds.window(tearOffPanel, query=True, exists=True):
		cmds.showWindow(tearOffPanel)
		return

	# Generate a new name. This sometimes returns errors because maya was unable
	# to generate a unique name. That is why I use the time module.
	newName = 'tearOffPanel{}'.format(str(time.time()).split('.')[0])
	
	# Use Maya native UI commands to create a modelPanel with advanced controls and a menuBar
	tearOffPanel = cmds.window(newName, title='Advanced Tear Off', widthHeight=(600,500))
	cmds.paneLayout()
	cmds.modelPanel(tearOffPanel, menuBarVisible=True)
	cmds.showWindow(tearOffPanel)