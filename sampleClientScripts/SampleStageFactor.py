from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage_with_liner_factors.fez")


liner = model.getLinerPropertyByName("Liner 1")
liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)
print(liner.CableTruss.getDefineRelativeStageFactors())

cableTrussFactors = liner.CableTruss.getStageFactors()
stage1CableTrussFactors = cableTrussFactors[1]
stage2CableTrussFactors = cableTrussFactors[3]
stage3CableTrussFactors = cableTrussFactors[6]

stage1CableTrussFactors.setYoungsModulusFactor(2)
print(stage1CableTrussFactors.getYoungsModulusFactor())