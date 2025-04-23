from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60062)
modeler = RS2Modeler(port=60062)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

linerList = model.getAllLinerProperties()
liner1 = linerList[0]
liner2 = linerList[1]
liner3 = linerList[2]

liner1.setLinerName("Example Liner 1")
liner1.setLinerType(LinerTypes.CABLE_TRUSS)
liner1.CableTruss.setYoungsModulus(250000)
liner1.CableTruss.setMaterialType(MaterialType.ELASTIC)
liner1.CableTruss.setStageCableProperties(False)

print(liner1.CableTruss.getYoungsModulus())
print(liner1.CableTruss.getMaterialType())
print(liner1.CableTruss.getMaterialType())

liner2.setLinerName("Example Liner 2")
liner2.setLinerType(LinerTypes.GEOSYNTHETIC)
liner2.Geosynthetic.setProperties(MaterialType=MaterialType.PLASTIC, TensileStrengthPeak=0.05, TensileStrengthResidual=0.025)

print(liner2.Geosynthetic.getProperties())

liner3.setLinerName("Example Liner 3")
liner3.setLinerType(LinerTypes.REINFORCED_CONCRETE)
liner3.ReinforcedConcrete.setProperties(IncludeWeightInStressAnalysis=False, Spacing=2.2, SlidingGap=False)
# Not all functions are accessible through the getProperties method. 
# Consult setProperties method definition in documentation to determine properties available.
liner3.ReinforcedConcrete.setStaticTemperatureGridToUse("Default Grid")

print(liner3.ReinforcedConcrete.getProperties())
# Not all functions are accessible through the getProperties method. 
# Consult getProperties method definition in documentation to determine properties available.
print(liner3.ReinforcedConcrete.getStaticTemperatureGridToUse())

model.close()
modeler.closeProgram()