from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage_with_liner_relative_stage_factors.fez")

liner = model.getLinerPropertyByName("Liner 1")
liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)
liner.CableTruss.setDefineRelativeStageFactors(True)
print(liner.CableTruss.getDefineRelativeStageFactors())

cableTrussFactors = liner.CableTruss.getStageFactors()
CableTrussFactors1 = cableTrussFactors[0]
CableTrussFactors2 = cableTrussFactors[1]
CableTrussFactors3 = cableTrussFactors[2]
print(CableTrussFactors1.getStagesAfterInstallation())
print(CableTrussFactors2.getStagesAfterInstallation())
print(CableTrussFactors3.getStagesAfterInstallation())


CableTrussFactors1.setStagesAfterInstallation(2)
CableTrussFactors2.setStagesAfterInstallation(4)
CableTrussFactors3.setStagesAfterInstallation(6)
print(CableTrussFactors1.getStagesAfterInstallation())
print(CableTrussFactors2.getStagesAfterInstallation())
print(CableTrussFactors3.getStagesAfterInstallation())

CableTrussFactors1.setYoungsModulusFactor(2)
print(CableTrussFactors1.getYoungsModulusFactor())

