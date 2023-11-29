from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage_with_liner_factors.fez")


liner = model.getLinerPropertyByName("Liner 1")
liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

print(liner.CableTruss.getDefineRelativeStageFactors())

cableTrussFactors = liner.CableTruss.getDefinedStageFactors()
for stage, factor in cableTrussFactors.items():
    print(stage)
    factor.setYoungsModulusFactor(stage)
    print(factor.getYoungsModulusFactor())