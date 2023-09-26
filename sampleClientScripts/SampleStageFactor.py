from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage_with_liner_factors.fez")


liner = model.getLinerPropertyByName("Liner 1")
liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)
liner.CableTruss.setDefineRelativeStageFactors(True)
print(liner.CableTruss.getDefineRelativeStageFactors())

cableTrussFactors = liner.CableTruss.getStageFactors()
stage1CableTrussFactors = cableTrussFactors[0]
stage2CableTrussFactors = cableTrussFactors[1]
stage3CableTrussFactors = cableTrussFactors[2]

stage1CableTrussFactors.setStagesAfterInstallation(1)
stage2CableTrussFactors.setStagesAfterInstallation(2)
stage3CableTrussFactors.setStagesAfterInstallation(3)
print(stage1CableTrussFactors.getStagesAfterInstallation())
print(stage2CableTrussFactors.getStagesAfterInstallation())
print(stage3CableTrussFactors.getStagesAfterInstallation())

stage1CableTrussFactors.setYoungsModulusFactor(2)
print(stage1CableTrussFactors.getYoungsModulusFactor())