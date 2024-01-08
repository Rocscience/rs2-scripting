from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *
from rs2.ColorPicker import ColorPicker

modeler = RS2Modeler()

model = modeler.openFile(r"S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez")
joint = model.getJointPropertyByName("Joint 1")

# Get/Set Color
color =  joint.getJointColor()
print("Joint color = ", color)
r, g, b = ColorPicker.getRGBFromColor(color)
print("RGB Values from the Getter color = ", (r, g, b))

new_color = ColorPicker.getColorFromRGB(42, 60, 91)
joint.setJointColor(new_color)
# joint.setJointColor(ColorPicker.Tan)