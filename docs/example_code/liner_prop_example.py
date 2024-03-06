from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

linerList = model.getAllLinerProperties()
liner1 = linerList[0]
liner2 = linerList[1]
liner3 = linerList[2]

#Assigning liner1 properties individually
liner1.setLinerName("Example Liner 1")
liner1.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)
liner1.CableTruss.setYoungsModulus(250000)
liner1.CableTruss.setMaterialType(MaterialType.ELASTIC)
liner1.CableTruss.setStageCableProperties(False)

#Retrieving liner1 properties individiually
print(liner1.CableTruss.getYoungsModulus())
print(liner1.CableTruss.getMaterialType())
print(liner1.CableTruss.getMaterialType())

#Bulk assignment of liner2 properties
liner2.setLinerName("Example Liner 2")
liner2.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)
liner2.Geosynthetic.setProperties(MaterialType=MaterialType.PLASTIC, TensileStrengthPeak=0.05, TensileStrengthResidual=0.025)

#Bulk retrieval of liner2 properties
print(liner2.Geosynthetic.getProperties())

#Assignment of liner3 properties
liner3.setLinerName("Example Liner 3")
liner3.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)
liner3.ReinforcedConcrete.setProperties(IncludeWeightInStressAnalysis=False, Spacing=2.2, SlidingGap=False)
#Consult setProperties method definition in documentation to determine properties available.
liner3.ReinforcedConcrete.setStaticTemperatureGridToUse("Default Grid")

#Retrieval of liner2 properties
print(liner3.ReinforcedConcrete.getProperties())
#Not all functions are accesible through the getProperties method. 
#Consult getProperties method definition in documentation to determine properties available.
print(liner3.ReinforcedConcrete.getStaticTemperatureGridToUse())

model.close()