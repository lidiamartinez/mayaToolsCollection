__author__ = "Lidia Martinez Prado"
__copyright__ = "Copyright (C) 2017 Virtual Method Studio"
__license__ = "Public Domain"
__version__ = "1.0"
__doc__ = "Select any transform node (object) in the scene, and this will add a group with a new perspective camera, constrained to the original object"

import maya.cmds as cmds

def main():
	sel = cmds.ls(selection=True)
	if len(sel) != 1:
		cmds.confirmDialog(message="Please, select only ONE objet to follow.\nA perspective camera will be created following it")
	obj = sel[0]
	objFixedName = obj.replace(':','_')
	newCam = cmds.duplicate('persp', rr=True)[0]
	newCam = cmds.rename(newCam, name='FOLLOW_GROUP_{}_#'.format(objFixedName))
	cmds.showHidden(newCamGroup, below=True)
	cmds.parentConstraint(obj, newCamGroup, mo=True, skipRotate=('x','y','z'), weight=1.0, maintainOffset=True)
	msg = "A new camera was created: {0} under group {1}.\nIt follows the object {2} (only translation)."
	cmds.confirmDialog(message=msg.format(newCam, newCamGroup,obj))