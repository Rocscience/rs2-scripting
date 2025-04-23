from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 

RS2Modeler.startApplication(port=60061)
modeler = RS2Modeler(port=60061)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

joint = model.getJointPropertyByName("Joint 1")

joint.setSlipCriterion(JointTypes.MOHR_COULOMB)
definedStageFactors = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()
newStageFactor = joint.MohrCoulomb.stageFactorInterface.createStageFactor(2)
definedStageFactors[2] = newStageFactor
joint.MohrCoulomb.stageFactorInterface.setDefinedStageFactors(definedStageFactors)

mohrCoulombFactors = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()
stage2mohrCoulombFactors = mohrCoulombFactors[2]

stage2mohrCoulombFactors.setNormalStiffnessFactor(3)
stage2mohrCoulombFactors.setShearStiffnessFactor(3) 
stage2mohrCoulombFactors.setTensileStrengthFactor(3) 
stage2mohrCoulombFactors.setPeakCohesionFactor(3)
stage2mohrCoulombFactors.setPeakFrictionAngleFactor(3) 
stage2mohrCoulombFactors.setResCohesionFactor(3) 
stage2mohrCoulombFactors.setResFrictionAngleFactor(3) 
stage2mohrCoulombFactors.setResTensileStrengthFactor(3) 
stage2mohrCoulombFactors.setAdditionalPressureInsideJointFactor(6)
stage2mohrCoulombFactors.setGroundwaterPressureFactor(6)

joint.setSlipCriterion(JointTypes.BARTON_BANDIS) 
bartonBandisfactors = joint.BartonBandis.stageFactorInterface.getDefinedStageFactors()
stage2bartonBandisFactors = bartonBandisfactors[2]

stage2bartonBandisFactors.setNormalStiffnessFactor(3)
stage2bartonBandisFactors.setShearStiffnessFactor(3) 
stage2bartonBandisFactors.setJRCFactor(3) 
stage2bartonBandisFactors.setJCSFactor(3) 
stage2bartonBandisFactors.setResidualFrictionAngleFactor(3)
stage2bartonBandisFactors.setAdditionalPressureInsideJointFactor(6)
stage2bartonBandisFactors.setGroundwaterPressureFactor(6)

model.close()
modeler.closeProgram()