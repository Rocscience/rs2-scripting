import automate_screenshot
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
modeler = RS2Modeler()
file_path = os.path.join(current_dir, "Screenshot.fez")
print(file_path)
model = modeler.openFile(file_path)

# RS2 window name
window_name = 'RS2 - [Screenshot.fez - CAD View - Registered to Rocscience Inc., Toronto Office]'


bolt1 = model.getBoltPropertyByName("Bolt 1")
window_title = 'Define Bolt Properties'
# save screenshots
bolt1.setBoltType(BoltTypes.FULLY_BONDED)
# automate_screenshot.get_screenshot(window_title, window_name, 'bolt_fully_bonded.png')
bolt1.setBoltType(BoltTypes.PLAIN_STRAND_CABLE)
automate_screenshot.get_screenshot(window_title, window_name, 'bolt_plain_strand_cable.png')
# bolt1.setBoltType(BoltTypes.END_ANCHORED)
# automate_screenshot.get_screenshot(window_title, window_name, 'bolt_properties.png')
# bolt1.setBoltType(BoltTypes.SWELLEX)
# automate_screenshot.get_screenshot(window_title, window_name, 'bolt_swellex.png')
# bolt1.setBoltType(BoltTypes.TIEBACK)
# automate_screenshot.get_screenshot(window_title, window_name, 'bolt_tieback.png')

