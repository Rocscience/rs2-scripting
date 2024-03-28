from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 

modeler = RS2Modeler()
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

joint = model.getJointPropertyByName("Joint 1")

joint.setSlipCriterion(JointTypes.MOHR_COULOMB)
mohrCoulombFactors = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()
stage1mohrCoulombFactors = mohrCoulombFactors[1]

stage1mohrCoulombFactors.setNormalStiffnessFactor(3)
stage1mohrCoulombFactors.setShearStiffnessFactor(3) 
stage1mohrCoulombFactors.setTensileStrengthFactor(3) 
stage1mohrCoulombFactors.setPeakCohesionFactor(3)
stage1mohrCoulombFactors.setPeakFrictionAngleFactor(3) 
stage1mohrCoulombFactors.setResCohesionFactor(3) 
stage1mohrCoulombFactors.setResFrictionAngleFactor(3) 
stage1mohrCoulombFactors.setResTensileStrengthFactor(3) 
stage1mohrCoulombFactors.setAdditionalPressureInsideJointFactor(6)
stage1mohrCoulombFactors.setGroundwaterPressureFactor(6)


joint.setSlipCriterion(JointTypes.BARTON_BANDIS) 
bartonBandisfactors = joint.BartonBandis.stageFactorInterface.getDefinedStageFactors()

stage1bartonBandisFactors = bartonBandisfactors[1]

stage1bartonBandisFactors.setNormalStiffnessFactor(3)
stage1bartonBandisFactors.setShearStiffnessFactor(3) 
stage1bartonBandisFactors.setJRCFactor(3) 
stage1bartonBandisFactors.setJCSFactor(3) 
stage1bartonBandisFactors.setResidualFrictionAngleFactor(3)
stage1bartonBandisFactors.setAdditionalPressureInsideJointFactor(6)
stage1bartonBandisFactors.setGroundwaterPressureFactor(6)

model.close()