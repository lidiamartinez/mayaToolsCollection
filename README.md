# mayaToolsCollection
Virtual Method Studio's small scripts for Maya.
Find more information about us here:
http://www.virtualmethodstudio.com

============================================================
How to install in Windows for not experienced users 
============================================================

Since there is no automatic way to install these for now, you can install them by hand this way. But stay tuned, because there will be ways to do this faster and safer with new tools in the future:

- Download the mayaToolsCollection folder using the button available in gitHub in https://github.com/lidiamartinez/mayaToolsCollection/
- This will download a ZIP file that you will have to unzip somewhere in your harddrive.
- You will have a folder like this:  mayaToolsCollection/*scriptFolder*/*scriptName*.py
- Copy that folder into your scripts folder under maya installation:   C:/users/*yourUser*/maya/*versionNumer*/scripts/
- Make sure that the folder is NOT  .../scripts/mayaToolsCollection/mayaToolsCollection/*scriptFolder*...  There must be just one mayaToolsCollection folder level.
- In Maya, open the Script Editor window under Windows -> General Editors (or find how on Maya's Official Documentation)
- Copy and paste this on a Python tab in the lower part of the editor, changing "nameOfTheScript" with the script you are trying to add to Maya:


import mayaToolsCollection.nameOfTheScript

mayaToolsCollection.nameOfTheScript.run()



- Then, you can, either:
  A) In the script editor, go to File -> Save script to shelf. That will add the script as a button in your current active shelf.
  B) Select that code, copy it, and create a Runtime Command assigned to a Hotkey using the Hotkey Editor. Read how to do it in the official documentation (Searching for "Create a runtime command")

============================================================
Advanced Tear Off Copy Panel 
============================================================
  
Used to replace viewport's option: Panels -> Tear Off Copy...    which creates a new window with a more restricted version of a viewport. This scripts enhances this viewport window by adding the same options as a regular viewport (including the possibility to select from which camera it looks through, which is not available on a regular torn off copied panel).
This script doesn't replace the original behaviour. You will have to assign this to a hotkey in order to use it using the Hotkey Editor.

============================================================
Simple Follow Camera 
============================================================

Select an object with translation attributes (tx, ty, tz) and execute this script to create a new perspective camera inside a group on the outliner which will follow the given object in position using a position constraint, not rotation or scale. So you can rotate and place it and it will follow the object staying in that position.
Useful in situations where, for example, you have facial animation and the character moves a lot and you need a view of the facial animation at the same time as the full animation. Or you need several views of the same object during animation.
You can use this script in combination with Advanced Tear Off Copy Panel script. You execute this one first and then the other one so you get a nice viewport window looking through this new view.
