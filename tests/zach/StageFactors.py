from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import random




random_number = random.randint(60050, 60150)

RS2Modeler.startApplication(port=random_number)

modeler = RS2Modeler(port=random_number)

model = modeler.openFile(r"C:\scriptingModels\testProjectDynamicPropertiesStaticGroundwater.fez")

#model.ResetProperties()

liner = model.getAllLinerProperties()[0]
joint = model.getAllJointProperties()[0]
pile = model.getAllPileProperties()[0]
material = model.getAllMaterialProperties()[0]


joint.MohrCoulomb.setApplyStageFactors(True)
pile.setStageForceDisplacement(True)
liner.StandardBeam.setStageLinerProperties(True)

material.StageFactors.setStageStrengthStiffnessStageFactors(True)
material.StageFactors.setStageThermalStageFactors(True)
material.StageFactors.setStageHydraulicStageFactor(True)



jsf = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()
psf = pile.ForceDisplacement.stageFactorInterface.getDefinedStageFactors()
lisf = liner.StandardBeam.stageFactorInterface.getDefinedStageFactors()
msf = material.Hydraulic.stageFactorInterface.getDefinedStageFactors()


'''
joint.MohrCoulomb.stageFactorInterface.createStageFactor(2)
pile.ForceDisplacement.stageFactorInterface.createStageFactor(2)
liner.StandardBeam.stageFactorInterface.createStageFactor(2)
material.StageFactors.createStageFactor(2)

hydro_sf = material.Hydraulic.stageFactorInterface.getDefinedStageFactors()[2]
thermal_sf = material.Thermal.stageFactorInterface.getDefinedStageFactors()[2]
strength_sf = material.Strength.stageFactorInterface.getDefinedStageFactors()[2]


liner_sf = liner.StandardBeam.stageFactorInterface.getDefinedStageFactors()[2]
liner.StandardBeam.stageFactorInterface.setDefinedStageFactors(StageFactorDefinitionMethod.ABSOLUTE_STAGE_FACTOR,  {3 : liner_sf})

joint_sf = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()[2]
joint.MohrCoulomb.stageFactorInterface.setDefinedStageFactors({3 : joint_sf})

pile_sf = pile.ForceDisplacement.stageFactorInterface.getDefinedStageFactors()[2]
pile.ForceDisplacement.stageFactorInterface.setDefinedStageFactors({3 : pile_sf})
'''

mat = model.getAllMaterialProperties()[0]
sfi = mat.StageFactors


mat.StageFactors.setStageStrengthStiffnessStageFactors(True)
mat.StageFactors.setStageHydraulicStageFactor(True)
mat.StageFactors.setStageThermalStageFactors(True)
mat.StageFactors.setStageDatumStageFactor(True)


dfs = sfi.getDefinedStageFactors()

fac1 = mat.Hydraulic.stageFactorInterface.getDefinedStageFactors()[1]
fac1.setMaterialBehaviourFactor(MaterialBehaviours.UNDRAINED)


mat.StageFactors.createStageFactor(2)
fac2 = mat.Hydraulic.stageFactorInterface.getDefinedStageFactors()[2]
fac2.setMaterialBehaviourFactor(MaterialBehaviours.DRAINED)


mat.Hydraulic.FEAGroundwater.stageFactorInterface.getDefinedStageFactors()[1].setMvFactor(1.1)
mat.Hydraulic.FEAGroundwater.stageFactorInterface.getDefinedStageFactors()[2].setMvFactor(1.2)



mat.Hydraulic.FEAGroundwater.stageFactorInterface.getDefinedStageFactors()[1].setAnisotropicSurfaceFactor("Anisotropic Surface 1")
mat.Hydraulic.FEAGroundwater.stageFactorInterface.getDefinedStageFactors()[2].setAnisotropicSurfaceFactor("Anisotropic Surface 4")

hydro_sf1 = mat.Hydraulic.FEAGroundwater.stageFactorInterface.getDefinedStageFactors()[1]
hydro_sf2 = mat.Hydraulic.StaticGroundwater.stageFactorInterface.getDefinedStageFactors()[2]

s1 = mat.Hydraulic.stageFactorInterface.getDefinedStageFactors()[1]
s2 = mat.Hydraulic.stageFactorInterface.getDefinedStageFactors()[2]

mat.Hydraulic.StaticGroundwater.stageFactorInterface.getDefinedStageFactors()[1].setPiezoToUse("1")
mat.Hydraulic.StaticGroundwater.stageFactorInterface.getDefinedStageFactors()[2].setPiezoToUse("2")


mat.Thermal.stageFactorInterface.getDefinedStageFactors()[1].setThermalGridFactor("Grid 7");
mat.Thermal.stageFactorInterface.getDefinedStageFactors()[2].setThermalGridFactor("Grid 11")


sf1 = mat.Datum.stageFactorInterface.getDefinedStageFactors()[1].getDatumYoungsStageFactor()
sf2 = mat.Datum.stageFactorInterface.getDefinedStageFactors()[1].getDatumCohesionStageFactor()
sf3 = mat.Datum.stageFactorInterface.getDefinedStageFactors()[1].getDatumFrictionStageFactor()

sf1.setDatum(1.1)
sf1.setChange(1.2)
sf1.setResidualChange(1.3)
sf1.setPeakCutoffValue(1.4)
sf1.setResidualCutoffValue(1.5)


sf2.setDatum(2.1)
sf2.setChange(2.2)
sf2.setResidualChange(2.3)
sf2.setPeakCutoffValue(2.4)
sf2.setResidualCutoffValue(2.5)

sf3.setDatum(3.1)
sf3.setChange(3.2)
sf3.setResidualChange(3.3)
sf3.setPeakCutoffValue(3.4)
sf3.setResidualCutoffValue(3.5)



dfs = sfi.getDefinedStageFactors()

sf1 = mat.Strength.stageFactorInterface.getDefinedStageFactors()[1]
sf2 = mat.Strength.stageFactorInterface.getDefinedStageFactors()[2]
mat.Strength.MohrCoulombStrength.stageFactorInterface.getDefinedStageFactors()[1].setPeakFrictionAngleFactor(1.123)

#sf.setResetYield(True)

mat.StageFactors.setStageStrengthStiffnessStageFactors(True)
mat.StageFactors.setStageDatumStageFactor(False)

sfi.setDefinedStageFactors({
2: (sf1, s1, dfs[1][2]),
3: (sf1, s1, dfs[2][2]),
5: (sf2, s2, dfs[1][2]),
7: (sf2, s2, dfs[2][2])
})



for a in range(1,7):
    sf = mat.StageFactors.getStageFactor(a)
    pass



pass