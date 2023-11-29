from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage_with_liner_factors.fez")

liner = model.getLinerPropertyByName("Liner 1")
liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)
cableTrussFactors = liner.CableTruss.getDefinedStageFactors()


print(f"Using relative stage? {liner.CableTruss.getDefineRelativeStageFactors()}")

for stage in cableTrussFactors:
    print(stage)

liner.CableTruss.setDefineRelativeStageFactors(True) # resets the stages from absolute 1,3,6 to relative 1,2,3
cableTrussFactors = liner.CableTruss.getDefinedStageFactors()

print(f"Using relative stage? {liner.CableTruss.getDefineRelativeStageFactors()}")

for stage in cableTrussFactors:
    print(stage)

CableTrussFactors1 = cableTrussFactors[1]
CableTrussFactors2 = cableTrussFactors[2]
CableTrussFactors3 = cableTrussFactors[3]

CableTrussFactors1.setStagesAfterInstallation(2)
CableTrussFactors2.setStagesAfterInstallation(4)
CableTrussFactors3.setStagesAfterInstallation(5)
print("After change:")
print(CableTrussFactors1.getStagesAfterInstallation())
print(CableTrussFactors2.getStagesAfterInstallation())
print(CableTrussFactors3.getStagesAfterInstallation())