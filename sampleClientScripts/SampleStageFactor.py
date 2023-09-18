from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage_with_liner_factors.fez")


liner = model.getLinerPropertyByName("Liner 1")
liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS) #modifies the liner in c++

cableTrussFactors = liner.CableTruss.getStageFactors()
stage1CableTrussFactors = cableTrussFactors[0]

stage1CableTrussFactors.setYoungsModulusFactor(2)#modifies the stage factor in c++
print(stage1CableTrussFactors.getYoungsModulusFactor())