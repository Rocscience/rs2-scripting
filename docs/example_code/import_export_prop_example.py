from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60095)
modeler = RS2Modeler(port=60095)
model1FilePath = rf"{current_dir}\example_models\ExampleModel.fez"
model2FilePath = rf"{current_dir}\example_models\EmptyExampleModel_start.fez"
model2FileSavePath = rf"{current_dir}\example_models\EmptyExampleModel_final.fez"

model1 = modeler.openFile(model1FilePath)
model2 = modeler.openFile(model2FilePath)

model1Till = model1.getMaterialPropertyByName("Till")
model2Till = model2.getMaterialPropertyByName("till")

# Not all functions are accessible through the setProperties and getProperties methods. 
# Consult setProperties and getProperties method definition in documentation to determine properties available.

model1_initial_conditions = model1Till.InitialConditions.getProperties()
model2Till.InitialConditions.setProperties(**model1_initial_conditions)

print("Model 2 Till Initial Conditions")
print(model2Till.InitialConditions.getProperties())

model1_stiffness = model1Till.Stiffness.Isotropic.getProperties()
model2Till.Stiffness.Isotropic.setProperties(**model1_stiffness)

print("\nModel 2 Till Stiffness")
print(model2Till.Stiffness.Isotropic.getProperties())

model1_strength = model1Till.Strength.MohrCoulombStrength.getProperties()
model2Till.Strength.MohrCoulombStrength.setProperties(**model1_strength)

print("\nModel 2 Till Strength")
print(model2Till.Strength.MohrCoulombStrength.getProperties())

model1_hydraulic = model1Till.Hydraulic.StaticGroundwater.getProperties()
model2Till.Hydraulic.StaticGroundwater.setProperties(**model1_hydraulic)

print("\nModel 2 Till Hydraulic")
print(model2Till.Hydraulic.StaticGroundwater.getProperties())

model1_thermal_conductivity = model1Till.Thermal.Conductivity.ConstantConductivity.getProperties()
model2Till.Thermal.Conductivity.ConstantConductivity.setProperties(**model1_thermal_conductivity)

print("\nModel 2 Till Thermal Conductivity")
print(model2Till.Thermal.Conductivity.ConstantConductivity.getProperties())

model1_thermal_heat_capacity = model1Till.Thermal.HeatCapacity.ConstantHeatCapacity.getProperties()
model2Till.Thermal.HeatCapacity.ConstantHeatCapacity.setProperties(**model1_thermal_heat_capacity)

print("\nModel 2 Till Thermal Heat Capactiy")
print(model2Till.Thermal.HeatCapacity.ConstantHeatCapacity.getProperties())

model1_bolt = model1.getAllBoltProperties()[0]
model2_bolt = model2.getAllBoltProperties()[0]

model1_bolt_properties = model1_bolt.Swellex.getProperties()
model2_bolt.setBoltType(BoltTypes.SWELLEX)
model2_bolt.Swellex.setProperties(**model1_bolt_properties)

print("\nModel 2 Bolt Properties")
print(model2_bolt.Swellex.getProperties())

model1_liner = model1.getAllLinerProperties()[0]
model2_liner = model2.getAllLinerProperties()[0]

model1_liner_properties = model1_liner.ReinforcedConcrete.getProperties()
model2_liner.setLinerType(LinerTypes.REINFORCED_CONCRETE)
model2_liner.ReinforcedConcrete.setProperties(**model1_liner_properties)

print("\nModel 2 Liner Properties")
print(model2_liner.ReinforcedConcrete.getProperties())

model1_joint = model1.getAllJointProperties()[0]
model2_joint = model2.getAllJointProperties()[0]

model1_joint_properties = model1_joint.MaterialDependent.getProperties()
model2_joint.setSlipCriterion(JointTypes.MATERIAL_DEPENDENT)
model2_joint.MaterialDependent.setProperties(**model1_joint_properties)

print("\nModel 2 Joint Properties")
print(model2_joint.MaterialDependent.getProperties())

model1_pile = model1.getAllPileProperties()[0]
model2_pile = model2.getAllPileProperties()[0]

model1_pile_interface_properties = model1_pile.MohrCoulombPile.getProperties()
model2_pile.MohrCoulombPile.setProperties(**model1_pile_interface_properties)

model1_pile_force_displacement_properties = model1_pile.ForceDisplacement.getProperties()
model2_pile.ForceDisplacement.setProperties(**model1_pile_force_displacement_properties)

print("\nModel 2 Pile Interface Properties")
print(model2_pile.MohrCoulombPile.getProperties())
print("\nModel 2 Pile Force Displacement Properties")
print(model2_pile.ForceDisplacement.getProperties())

model2.saveAs(model2FileSavePath)
modeler.closeProgram()