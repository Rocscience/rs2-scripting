from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")
liner = model.getLinerPropertyByName("Liner 1")
liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

liner.CableTruss.setStageCableProperties(True)

cableTrussFactors = liner.CableTruss.getStageFactors()

stage1CableTrussFactors = cableTrussFactors[0]
stage2CableTrussFactors = cableTrussFactors[1]

stage1CableTrussFactors.setYoungsModulusFactor(2)
print(stage1CableTrussFactors.getYoungsModulusFactor())