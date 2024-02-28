from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_Joint.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Joint\jointStageFactors_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Joint\jointStageFactors_python.fez'

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

jointList = model.getAllJointProperties()
joint1 = jointList[0]
joint2 = jointList[1]
joint3 = jointList[2]  
joint4 = jointList[3]
joint5 = jointList[4]
joint6 = jointList[5]
joint7 = jointList[6]
joint8 = jointList[7]
joint9 = jointList[8]
joint10 = jointList[9]
joint11 = jointList[10]
joint12 = jointList[11]
joint13 = jointList[12]
joint14 = jointList[13] 
joint15 = jointList[14]
joint16 = jointList[15]
joint17 = jointList[16]
joint18 = jointList[17]
joint19 = jointList[18]
joint20 = jointList[19]
joint21 = jointList[20]  
joint22 = jointList[21]
joint23 = jointList[22]
joint24 = jointList[23]
joint25 = jointList[24]
joint26 = jointList[25]
joint27 = jointList[26]
joint28 = jointList[27]
joint29 = jointList[28]
joint30 = jointList[29]
joint31 = jointList[30]
joint32 = jointList[31]
joint33 = jointList[32]

def test1():
	joint1.setSlipCriterion(JointTypes.JOINT_NONE)

	# Additional pressure properties are changed in order to test all stage factor combinations. Additional pressure checkboxes themselves are tested exhaustively in zach_JointAdditionalPressure.py
	joint1.MohrCoulomb.setApplyPorePressure(True) 
	joint1.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)

	joint1.MohrCoulomb.setApplyStageFactors(True)

	sf2 = joint1.MohrCoulomb.stageFactorInterface.createStageFactor(2)
	sf4 = joint1.MohrCoulomb.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setAdditionalPressureInsideJointFactor(1.3)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setAdditionalPressureInsideJointFactor(1.7)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint1.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint1.MohrCoulomb.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint1.MohrCoulomb.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(),1.3)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getAdditionalPressureInsideJointFactor(),1.3)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test2():
	joint2.setSlipCriterion(JointTypes.JOINT_NONE)

	joint2.MohrCoulomb.setApplyPorePressure(False)
	joint2.MohrCoulomb.setApplyAdditionalPressureInsideJoint(False)

	joint2.MohrCoulomb.setApplyStageFactors(True)

	sf2 = joint2.MohrCoulomb.stageFactorInterface.createStageFactor(2)
	sf4 = joint2.MohrCoulomb.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)

	sf_dict = joint2.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint2.MohrCoulomb.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint2.MohrCoulomb.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)

def test3():
	joint3.setSlipCriterion(JointTypes.JOINT_NONE)
		 
	joint3.MohrCoulomb.setApplyPorePressure(True)
	joint3.MohrCoulomb.setApplyAdditionalPressureInsideJoint(False)
		 
	joint3.MohrCoulomb.setApplyStageFactors(True)

	sf2 = joint3.MohrCoulomb.stageFactorInterface.createStageFactor(2)
	sf4 = joint3.MohrCoulomb.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint3.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint3.MohrCoulomb.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint3.MohrCoulomb.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test4():
	joint4.setSlipCriterion(JointTypes.JOINT_NONE)
		 
	joint4.MohrCoulomb.setApplyPorePressure(False)
	joint4.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)
		 
	joint4.MohrCoulomb.setApplyStageFactors(True)

	sf2 = joint4.MohrCoulomb.stageFactorInterface.createStageFactor(2)
	sf4 = joint4.MohrCoulomb.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setAdditionalPressureInsideJointFactor(1.3)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setAdditionalPressureInsideJointFactor(1.7)

	sf_dict = joint4.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint4.MohrCoulomb.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint4.MohrCoulomb.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(),1.3)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getAdditionalPressureInsideJointFactor(),1.3)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)

def test5():
	joint = joint5

	joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
	joint.MohrCoulomb.setResidualStrength(True)
		 
	joint.MohrCoulomb.setApplyPorePressure(True)
	joint.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)
		 
	joint.MohrCoulomb.setApplyStageFactors(True)

	sf2 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(2)
	sf4 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setTensileStrengthFactor(1.9)
	sf2.setPeakCohesionFactor(1.11)
	sf2.setPeakFrictionAngleFactor(1.12)
	sf2.setResCohesionFactor(1.13)
	sf2.setResFrictionAngleFactor(1.14)
	sf2.setResTensileStrengthFactor(1.15)
	sf2.setAdditionalPressureInsideJointFactor(1.3)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setTensileStrengthFactor(1.16)
	sf4.setPeakCohesionFactor(1.17)
	sf4.setPeakFrictionAngleFactor(1.18)
	sf4.setResCohesionFactor(1.19)
	sf4.setResFrictionAngleFactor(1.21)
	sf4.setResTensileStrengthFactor(1.22)
	sf4.setAdditionalPressureInsideJointFactor(1.7)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getTensileStrengthFactor(),1)
	assert(sf1.getPeakCohesionFactor(),1)
	assert(sf1.getPeakFrictionAngleFactor(),1)
	assert(sf1.getResCohesionFactor(),1)
	assert(sf1.getResFrictionAngleFactor(),1)
	assert(sf1.getResTensileStrengthFactor(),1)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getTensileStrengthFactor(),1.9)
	assert(sf2_fin.getPeakCohesionFactor(),1.11)
	assert(sf2_fin.getPeakFrictionAngleFactor(),1.12)
	assert(sf2_fin.getResCohesionFactor(),1.13)
	assert(sf2_fin.getResFrictionAngleFactor(),1.14)
	assert(sf2_fin.getResTensileStrengthFactor(),1.15)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(),1.3)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getTensileStrengthFactor(),1.9)
	assert(sf3.getPeakCohesionFactor(),1.11)
	assert(sf3.getPeakFrictionAngleFactor(),1.12)
	assert(sf3.getResCohesionFactor(),1.13)
	assert(sf3.getResFrictionAngleFactor(),1.14)
	assert(sf3.getResTensileStrengthFactor(),1.15)
	assert(sf3.getAdditionalPressureInsideJointFactor(),1.3)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getTensileStrengthFactor(),1.16)
	assert(sf4_fin.getPeakCohesionFactor(),1.17)
	assert(sf4_fin.getPeakFrictionAngleFactor(),1.18)
	assert(sf4_fin.getResCohesionFactor(),1.19)
	assert(sf4_fin.getResFrictionAngleFactor(),1.21)
	assert(sf4_fin.getResTensileStrengthFactor(),1.22)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test6():
	joint = joint6

	joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
	joint.MohrCoulomb.setResidualStrength(False)
		 
	joint.MohrCoulomb.setApplyPorePressure(True)
	joint.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)
		 
	joint.MohrCoulomb.setApplyStageFactors(True)

	sf2 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(2)
	sf4 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setTensileStrengthFactor(1.9)
	sf2.setPeakCohesionFactor(1.11)
	sf2.setPeakFrictionAngleFactor(1.12)
	sf2.setAdditionalPressureInsideJointFactor(1.3)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setTensileStrengthFactor(1.16)
	sf4.setPeakCohesionFactor(1.17)
	sf4.setPeakFrictionAngleFactor(1.18)
	sf4.setAdditionalPressureInsideJointFactor(1.7)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getTensileStrengthFactor(),1)
	assert(sf1.getPeakCohesionFactor(),1)
	assert(sf1.getPeakFrictionAngleFactor(),1)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getTensileStrengthFactor(),1.9)
	assert(sf2_fin.getPeakCohesionFactor(),1.11)
	assert(sf2_fin.getPeakFrictionAngleFactor(),1.12)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(),1.3)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getTensileStrengthFactor(),1.9)
	assert(sf3.getPeakCohesionFactor(),1.11)
	assert(sf3.getPeakFrictionAngleFactor(),1.12)
	assert(sf3.getAdditionalPressureInsideJointFactor(),1.3)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getTensileStrengthFactor(),1.16)
	assert(sf4_fin.getPeakCohesionFactor(),1.17)
	assert(sf4_fin.getPeakFrictionAngleFactor(),1.18)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test7():
	joint = joint7

	joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
	joint.MohrCoulomb.setResidualStrength(True)
		 
	joint.MohrCoulomb.setApplyPorePressure(False)
	joint.MohrCoulomb.setApplyAdditionalPressureInsideJoint(False)
		 
	joint.MohrCoulomb.setApplyStageFactors(True)

	sf2 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(2)
	sf4 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setTensileStrengthFactor(1.9)
	sf2.setPeakCohesionFactor(1.11)
	sf2.setPeakFrictionAngleFactor(1.12)
	sf2.setResCohesionFactor(1.13)
	sf2.setResFrictionAngleFactor(1.14)
	sf2.setResTensileStrengthFactor(1.15)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setTensileStrengthFactor(1.16)
	sf4.setPeakCohesionFactor(1.17)
	sf4.setPeakFrictionAngleFactor(1.18)
	sf4.setResCohesionFactor(1.19)
	sf4.setResFrictionAngleFactor(1.21)
	sf4.setResTensileStrengthFactor(1.22)

	sf_dict = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getTensileStrengthFactor(),1)
	assert(sf1.getPeakCohesionFactor(),1)
	assert(sf1.getPeakFrictionAngleFactor(),1)
	assert(sf1.getResCohesionFactor(),1)
	assert(sf1.getResFrictionAngleFactor(),1)
	assert(sf1.getResTensileStrengthFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getTensileStrengthFactor(),1.9)
	assert(sf2_fin.getPeakCohesionFactor(),1.11)
	assert(sf2_fin.getPeakFrictionAngleFactor(),1.12)
	assert(sf2_fin.getResCohesionFactor(),1.13)
	assert(sf2_fin.getResFrictionAngleFactor(),1.14)
	assert(sf2_fin.getResTensileStrengthFactor(),1.15)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getTensileStrengthFactor(),1.9)
	assert(sf3.getPeakCohesionFactor(),1.11)
	assert(sf3.getPeakFrictionAngleFactor(),1.12)
	assert(sf3.getResCohesionFactor(),1.13)
	assert(sf3.getResFrictionAngleFactor(),1.14)
	assert(sf3.getResTensileStrengthFactor(),1.15)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getTensileStrengthFactor(),1.16)
	assert(sf4_fin.getPeakCohesionFactor(),1.17)
	assert(sf4_fin.getPeakFrictionAngleFactor(),1.18)
	assert(sf4_fin.getResCohesionFactor(),1.19)
	assert(sf4_fin.getResFrictionAngleFactor(),1.21)
	assert(sf4_fin.getResTensileStrengthFactor(),1.22)

def test8():
	joint = joint8

	joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
	joint.MohrCoulomb.setResidualStrength(False)
		 
	joint.MohrCoulomb.setApplyPorePressure(False)
	joint.MohrCoulomb.setApplyAdditionalPressureInsideJoint(False)
		 
	joint.MohrCoulomb.setApplyStageFactors(True)

	sf2 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(2)
	sf4 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setTensileStrengthFactor(1.9)
	sf2.setPeakCohesionFactor(1.11)
	sf2.setPeakFrictionAngleFactor(1.12)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setTensileStrengthFactor(1.16)
	sf4.setPeakCohesionFactor(1.17)
	sf4.setPeakFrictionAngleFactor(1.18)

	sf_dict = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getTensileStrengthFactor(),1)
	assert(sf1.getPeakCohesionFactor(),1)
	assert(sf1.getPeakFrictionAngleFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getTensileStrengthFactor(),1.9)
	assert(sf2_fin.getPeakCohesionFactor(),1.11)
	assert(sf2_fin.getPeakFrictionAngleFactor(),1.12)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getTensileStrengthFactor(),1.9)
	assert(sf3.getPeakCohesionFactor(),1.11)
	assert(sf3.getPeakFrictionAngleFactor(),1.12)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getTensileStrengthFactor(),1.16)
	assert(sf4_fin.getPeakCohesionFactor(),1.17)
	assert(sf4_fin.getPeakFrictionAngleFactor(),1.18)

def test9():
	joint = joint9

	joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
	joint.MohrCoulomb.setResidualStrength(True)
		 
	joint.MohrCoulomb.setApplyPorePressure(True)
	joint.MohrCoulomb.setApplyAdditionalPressureInsideJoint(False)
		 
	joint.MohrCoulomb.setApplyStageFactors(True)

	sf2 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(2)
	sf4 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setTensileStrengthFactor(1.9)
	sf2.setPeakCohesionFactor(1.11)
	sf2.setPeakFrictionAngleFactor(1.12)
	sf2.setResCohesionFactor(1.13)
	sf2.setResFrictionAngleFactor(1.14)
	sf2.setResTensileStrengthFactor(1.15)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setTensileStrengthFactor(1.16)
	sf4.setPeakCohesionFactor(1.17)
	sf4.setPeakFrictionAngleFactor(1.18)
	sf4.setResCohesionFactor(1.19)
	sf4.setResFrictionAngleFactor(1.21)
	sf4.setResTensileStrengthFactor(1.22)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getTensileStrengthFactor(),1)
	assert(sf1.getPeakCohesionFactor(),1)
	assert(sf1.getPeakFrictionAngleFactor(),1)
	assert(sf1.getResCohesionFactor(),1)
	assert(sf1.getResFrictionAngleFactor(),1)
	assert(sf1.getResTensileStrengthFactor(),1)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getTensileStrengthFactor(),1.9)
	assert(sf2_fin.getPeakCohesionFactor(),1.11)
	assert(sf2_fin.getPeakFrictionAngleFactor(),1.12)
	assert(sf2_fin.getResCohesionFactor(),1.13)
	assert(sf2_fin.getResFrictionAngleFactor(),1.14)
	assert(sf2_fin.getResTensileStrengthFactor(),1.15)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getTensileStrengthFactor(),1.9)
	assert(sf3.getPeakCohesionFactor(),1.11)
	assert(sf3.getPeakFrictionAngleFactor(),1.12)
	assert(sf3.getResCohesionFactor(),1.13)
	assert(sf3.getResFrictionAngleFactor(),1.14)
	assert(sf3.getResTensileStrengthFactor(),1.15)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getTensileStrengthFactor(),1.16)
	assert(sf4_fin.getPeakCohesionFactor(),1.17)
	assert(sf4_fin.getPeakFrictionAngleFactor(),1.18)
	assert(sf4_fin.getResCohesionFactor(),1.19)
	assert(sf4_fin.getResFrictionAngleFactor(),1.21)
	assert(sf4_fin.getResTensileStrengthFactor(),1.22)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test10():
	joint = joint10

	joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
	joint.MohrCoulomb.setResidualStrength(False)
		 
	joint.MohrCoulomb.setApplyPorePressure(True)
	joint.MohrCoulomb.setApplyAdditionalPressureInsideJoint(False)
		 
	joint.MohrCoulomb.setApplyStageFactors(True)

	sf2 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(2)
	sf4 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setTensileStrengthFactor(1.9)
	sf2.setPeakCohesionFactor(1.11)
	sf2.setPeakFrictionAngleFactor(1.12)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setTensileStrengthFactor(1.16)
	sf4.setPeakCohesionFactor(1.17)
	sf4.setPeakFrictionAngleFactor(1.18)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getTensileStrengthFactor(),1)
	assert(sf1.getPeakCohesionFactor(),1)
	assert(sf1.getPeakFrictionAngleFactor(),1)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getTensileStrengthFactor(),1.9)
	assert(sf2_fin.getPeakCohesionFactor(),1.11)
	assert(sf2_fin.getPeakFrictionAngleFactor(),1.12)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getTensileStrengthFactor(),1.9)
	assert(sf3.getPeakCohesionFactor(),1.11)
	assert(sf3.getPeakFrictionAngleFactor(),1.12)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getTensileStrengthFactor(),1.16)
	assert(sf4_fin.getPeakCohesionFactor(),1.17)
	assert(sf4_fin.getPeakFrictionAngleFactor(),1.18)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test11():
	joint = joint11

	joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
	joint.MohrCoulomb.setResidualStrength(True)
		 
	joint.MohrCoulomb.setApplyPorePressure(False)
	joint.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)
		 
	joint.MohrCoulomb.setApplyStageFactors(True)

	sf2 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(2)
	sf4 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setTensileStrengthFactor(1.9)
	sf2.setPeakCohesionFactor(1.11)
	sf2.setPeakFrictionAngleFactor(1.12)
	sf2.setResCohesionFactor(1.13)
	sf2.setResFrictionAngleFactor(1.14)
	sf2.setResTensileStrengthFactor(1.15)
	sf2.setAdditionalPressureInsideJointFactor(1.3)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setTensileStrengthFactor(1.16)
	sf4.setPeakCohesionFactor(1.17)
	sf4.setPeakFrictionAngleFactor(1.18)
	sf4.setResCohesionFactor(1.19)
	sf4.setResFrictionAngleFactor(1.21)
	sf4.setResTensileStrengthFactor(1.22)
	sf4.setAdditionalPressureInsideJointFactor(1.7)

	sf_dict = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getTensileStrengthFactor(),1)
	assert(sf1.getPeakCohesionFactor(),1)
	assert(sf1.getPeakFrictionAngleFactor(),1)
	assert(sf1.getResCohesionFactor(),1)
	assert(sf1.getResFrictionAngleFactor(),1)
	assert(sf1.getResTensileStrengthFactor(),1)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getTensileStrengthFactor(),1.9)
	assert(sf2_fin.getPeakCohesionFactor(),1.11)
	assert(sf2_fin.getPeakFrictionAngleFactor(),1.12)
	assert(sf2_fin.getResCohesionFactor(),1.13)
	assert(sf2_fin.getResFrictionAngleFactor(),1.14)
	assert(sf2_fin.getResTensileStrengthFactor(),1.15)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(),1.3)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getTensileStrengthFactor(),1.9)
	assert(sf3.getPeakCohesionFactor(),1.11)
	assert(sf3.getPeakFrictionAngleFactor(),1.12)
	assert(sf3.getResCohesionFactor(),1.13)
	assert(sf3.getResFrictionAngleFactor(),1.14)
	assert(sf3.getResTensileStrengthFactor(),1.15)
	assert(sf3.getAdditionalPressureInsideJointFactor(),1.3)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getTensileStrengthFactor(),1.16)
	assert(sf4_fin.getPeakCohesionFactor(),1.17)
	assert(sf4_fin.getPeakFrictionAngleFactor(),1.18)
	assert(sf4_fin.getResCohesionFactor(),1.19)
	assert(sf4_fin.getResFrictionAngleFactor(),1.21)
	assert(sf4_fin.getResTensileStrengthFactor(),1.22)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)

def test12():
	joint = joint12

	joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
	joint.MohrCoulomb.setResidualStrength(True)
		 
	joint.MohrCoulomb.setApplyPorePressure(False)
	joint.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)
		 
	joint.MohrCoulomb.setApplyStageFactors(True)

	sf2 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(2)
	sf4 = joint.MohrCoulomb.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setTensileStrengthFactor(1.9)
	sf2.setPeakCohesionFactor(1.11)
	sf2.setPeakFrictionAngleFactor(1.12)
	sf2.setAdditionalPressureInsideJointFactor(1.3)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setTensileStrengthFactor(1.16)
	sf4.setPeakCohesionFactor(1.17)
	sf4.setPeakFrictionAngleFactor(1.18)
	sf4.setAdditionalPressureInsideJointFactor(1.7)

	sf_dict = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.MohrCoulomb.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getTensileStrengthFactor(),1)
	assert(sf1.getPeakCohesionFactor(),1)
	assert(sf1.getPeakFrictionAngleFactor(),1)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getTensileStrengthFactor(),1.9)
	assert(sf2_fin.getPeakCohesionFactor(),1.11)
	assert(sf2_fin.getPeakFrictionAngleFactor(),1.12)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(),1.3)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getTensileStrengthFactor(),1.9)
	assert(sf3.getPeakCohesionFactor(),1.11)
	assert(sf3.getPeakFrictionAngleFactor(),1.12)
	assert(sf3.getAdditionalPressureInsideJointFactor(),1.3)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getTensileStrengthFactor(),1.16)
	assert(sf4_fin.getPeakCohesionFactor(),1.17)
	assert(sf4_fin.getPeakFrictionAngleFactor(),1.18)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)

def test13():
	joint = joint13

	joint.setSlipCriterion(JointTypes.JOINT_BARTON_BANDIS)
		 
	joint.BartonBandis.setApplyPorePressure(True)
	joint.BartonBandis.setApplyAdditionalPressureInsideJoint(True)

	joint.BartonBandis.setApplyStageFactors(True)

	sf2 = joint.BartonBandis.stageFactorInterface.createStageFactor(2)
	sf4 = joint.BartonBandis.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setJCSFactor(1.9)
	sf2.setJRCFactor(1.11)
	sf2.setResidualFrictionAngleFactor(1.12)
	sf2.setAdditionalPressureInsideJointFactor(1.3)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setJCSFactor(1.13)
	sf4.setJRCFactor(1.14)
	sf4.setResidualFrictionAngleFactor(1.15)
	sf4.setAdditionalPressureInsideJointFactor(1.7)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint.BartonBandis.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.BartonBandis.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.BartonBandis.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getJCSFactor(), 1)
	assert(sf1.getJRCFactor(), 1)
	assert(sf1.getResidualFrictionAngleFactor(), 1)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getJCSFactor(), 1.9)
	assert(sf2_fin.getJRCFactor(), 1.11)
	assert(sf2_fin.getResidualFrictionAngleFactor(), 1.12)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(),1.3)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getJCSFactor(), 1.9)
	assert(sf3.getJRCFactor(), 1.11)
	assert(sf3.getResidualFrictionAngleFactor(), 1.12)
	assert(sf3.getAdditionalPressureInsideJointFactor(),1.3)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getJCSFactor(), 1.13)
	assert(sf4_fin.getJRCFactor(), 1.14)
	assert(sf4_fin.getResidualFrictionAngleFactor(), 1.15)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test14():
	joint = joint14

	joint.setSlipCriterion(JointTypes.JOINT_BARTON_BANDIS)
		 
	joint.BartonBandis.setApplyPorePressure(False)
	joint.BartonBandis.setApplyAdditionalPressureInsideJoint(False)

	joint.BartonBandis.setApplyStageFactors(True)

	sf2 = joint.BartonBandis.stageFactorInterface.createStageFactor(2)
	sf4 = joint.BartonBandis.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setJCSFactor(1.9)
	sf2.setJRCFactor(1.11)
	sf2.setResidualFrictionAngleFactor(1.12)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setJCSFactor(1.13)
	sf4.setJRCFactor(1.14)
	sf4.setResidualFrictionAngleFactor(1.15)

	sf_dict = joint.BartonBandis.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.BartonBandis.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.BartonBandis.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getJCSFactor(), 1)
	assert(sf1.getJRCFactor(), 1)
	assert(sf1.getResidualFrictionAngleFactor(), 1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getJCSFactor(), 1.9)
	assert(sf2_fin.getJRCFactor(), 1.11)
	assert(sf2_fin.getResidualFrictionAngleFactor(), 1.12)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getJCSFactor(), 1.9)
	assert(sf3.getJRCFactor(), 1.11)
	assert(sf3.getResidualFrictionAngleFactor(), 1.12)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getJCSFactor(), 1.13)
	assert(sf4_fin.getJRCFactor(), 1.14)
	assert(sf4_fin.getResidualFrictionAngleFactor(), 1.15)

def test15():
	joint = joint15

	joint.setSlipCriterion(JointTypes.JOINT_BARTON_BANDIS)
		 
	joint.BartonBandis.setApplyPorePressure(True)
	joint.BartonBandis.setApplyAdditionalPressureInsideJoint(False)

	joint.BartonBandis.setApplyStageFactors(True)

	sf2 = joint.BartonBandis.stageFactorInterface.createStageFactor(2)
	sf4 = joint.BartonBandis.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setJCSFactor(1.9)
	sf2.setJRCFactor(1.11)
	sf2.setResidualFrictionAngleFactor(1.12)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setJCSFactor(1.13)
	sf4.setJRCFactor(1.14)
	sf4.setResidualFrictionAngleFactor(1.15)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint.BartonBandis.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.BartonBandis.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.BartonBandis.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getJCSFactor(), 1)
	assert(sf1.getJRCFactor(), 1)
	assert(sf1.getResidualFrictionAngleFactor(), 1)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getJCSFactor(), 1.9)
	assert(sf2_fin.getJRCFactor(), 1.11)
	assert(sf2_fin.getResidualFrictionAngleFactor(), 1.12)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getJCSFactor(), 1.9)
	assert(sf3.getJRCFactor(), 1.11)
	assert(sf3.getResidualFrictionAngleFactor(), 1.12)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getJCSFactor(), 1.13)
	assert(sf4_fin.getJRCFactor(), 1.14)
	assert(sf4_fin.getResidualFrictionAngleFactor(), 1.15)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test16():
	joint = joint16

	joint.setSlipCriterion(JointTypes.JOINT_BARTON_BANDIS)
		 
	joint.BartonBandis.setApplyPorePressure(False)
	joint.BartonBandis.setApplyAdditionalPressureInsideJoint(True)

	joint.BartonBandis.setApplyStageFactors(True)

	sf2 = joint.BartonBandis.stageFactorInterface.createStageFactor(2)
	sf4 = joint.BartonBandis.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setJCSFactor(1.9)
	sf2.setJRCFactor(1.11)
	sf2.setResidualFrictionAngleFactor(1.12)
	sf2.setAdditionalPressureInsideJointFactor(1.3)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setJCSFactor(1.13)
	sf4.setJRCFactor(1.14)
	sf4.setResidualFrictionAngleFactor(1.15)
	sf4.setAdditionalPressureInsideJointFactor(1.7)

	sf_dict = joint.BartonBandis.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.BartonBandis.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.BartonBandis.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getJCSFactor(), 1)
	assert(sf1.getJRCFactor(), 1)
	assert(sf1.getResidualFrictionAngleFactor(), 1)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getJCSFactor(), 1.9)
	assert(sf2_fin.getJRCFactor(), 1.11)
	assert(sf2_fin.getResidualFrictionAngleFactor(), 1.12)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(),1.3)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getJCSFactor(), 1.9)
	assert(sf3.getJRCFactor(), 1.11)
	assert(sf3.getResidualFrictionAngleFactor(), 1.12)
	assert(sf3.getAdditionalPressureInsideJointFactor(),1.3)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getJCSFactor(), 1.13)
	assert(sf4_fin.getJRCFactor(), 1.14)
	assert(sf4_fin.getResidualFrictionAngleFactor(), 1.15)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)

def test17():
	joint = joint17

	joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SIMPLE)
		 
	joint.GeosyntheticHyperbolic.setApplyPorePressure(True)
	joint.GeosyntheticHyperbolic.setApplyAdditionalPressureInsideJoint(True)

	joint.GeosyntheticHyperbolic.setApplyStageFactors(True)

	sf2 = joint.GeosyntheticHyperbolic.stageFactorInterface.createStageFactor(2)
	sf4 = joint.GeosyntheticHyperbolic.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setPeakAdhesionAtSigninfFactor(1.9)
	sf2.setPeakFrictionAngleAtSign0Factor(1.11)
	sf2.setResAdhesionAtSigninfFactor(1.12)
	sf2.setResFrictionAngleAtSign0Factor(1.13)
	sf2.setAdditionalPressureInsideJointFactor(1.3)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setPeakAdhesionAtSigninfFactor(1.14)
	sf4.setPeakFrictionAngleAtSign0Factor(1.15)
	sf4.setResAdhesionAtSigninfFactor(1.16)
	sf4.setResFrictionAngleAtSign0Factor(1.17)
	sf4.setAdditionalPressureInsideJointFactor(1.7)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint.GeosyntheticHyperbolic.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.GeosyntheticHyperbolic.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.GeosyntheticHyperbolic.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getPeakAdhesionAtSigninfFactor(), 1)
	assert(sf1.getPeakFrictionAngleAtSign0Factor(), 1)
	assert(sf1.getResAdhesionAtSigninfFactor(), 1)
	assert(sf1.getResFrictionAngleAtSign0Factor(), 1)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getPeakAdhesionAtSigninfFactor(), 1.9)
	assert(sf2_fin.getPeakFrictionAngleAtSign0Factor(), 1.11)
	assert(sf2_fin.getResAdhesionAtSigninfFactor(), 1.12)
	assert(sf2_fin.getResFrictionAngleAtSign0Factor(), 1.13)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(), 1.3)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getPeakAdhesionAtSigninfFactor(), 1.9)
	assert(sf3.getPeakFrictionAngleAtSign0Factor(), 1.11)
	assert(sf3.getResAdhesionAtSigninfFactor(), 1.12)
	assert(sf3.getResFrictionAngleAtSign0Factor(), 1.13)
	assert(sf3.getAdditionalPressureInsideJointFactor(), 1.3)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getPeakAdhesionAtSigninfFactor(), 1.14)
	assert(sf4_fin.getPeakFrictionAngleAtSign0Factor(), 1.15)
	assert(sf4_fin.getResAdhesionAtSigninfFactor(), 1.16)
	assert(sf4_fin.getResFrictionAngleAtSign0Factor(), 1.17)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test18():
	joint = joint18

	joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SIMPLE)
		 
	joint.GeosyntheticHyperbolic.setApplyPorePressure(False)
	joint.GeosyntheticHyperbolic.setApplyAdditionalPressureInsideJoint(False)

	joint.GeosyntheticHyperbolic.setApplyStageFactors(True)

	sf2 = joint.GeosyntheticHyperbolic.stageFactorInterface.createStageFactor(2)
	sf4 = joint.GeosyntheticHyperbolic.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setPeakAdhesionAtSigninfFactor(1.9)
	sf2.setPeakFrictionAngleAtSign0Factor(1.11)
	sf2.setResAdhesionAtSigninfFactor(1.12)
	sf2.setResFrictionAngleAtSign0Factor(1.13)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setPeakAdhesionAtSigninfFactor(1.14)
	sf4.setPeakFrictionAngleAtSign0Factor(1.15)
	sf4.setResAdhesionAtSigninfFactor(1.16)
	sf4.setResFrictionAngleAtSign0Factor(1.17)

	sf_dict = joint.GeosyntheticHyperbolic.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.GeosyntheticHyperbolic.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.GeosyntheticHyperbolic.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getPeakAdhesionAtSigninfFactor(), 1)
	assert(sf1.getPeakFrictionAngleAtSign0Factor(), 1)
	assert(sf1.getResAdhesionAtSigninfFactor(), 1)
	assert(sf1.getResFrictionAngleAtSign0Factor(), 1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getPeakAdhesionAtSigninfFactor(), 1.9)
	assert(sf2_fin.getPeakFrictionAngleAtSign0Factor(), 1.11)
	assert(sf2_fin.getResAdhesionAtSigninfFactor(), 1.12)
	assert(sf2_fin.getResFrictionAngleAtSign0Factor(), 1.13)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getPeakAdhesionAtSigninfFactor(), 1.9)
	assert(sf3.getPeakFrictionAngleAtSign0Factor(), 1.11)
	assert(sf3.getResAdhesionAtSigninfFactor(), 1.12)
	assert(sf3.getResFrictionAngleAtSign0Factor(), 1.13)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getPeakAdhesionAtSigninfFactor(), 1.14)
	assert(sf4_fin.getPeakFrictionAngleAtSign0Factor(), 1.15)
	assert(sf4_fin.getResAdhesionAtSigninfFactor(), 1.16)
	assert(sf4_fin.getResFrictionAngleAtSign0Factor(), 1.17)

def test19():
	joint = joint19

	joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SIMPLE)
		 
	joint.GeosyntheticHyperbolic.setApplyPorePressure(True)
	joint.GeosyntheticHyperbolic.setApplyAdditionalPressureInsideJoint(False)

	joint.GeosyntheticHyperbolic.setApplyStageFactors(True)

	sf2 = joint.GeosyntheticHyperbolic.stageFactorInterface.createStageFactor(2)
	sf4 = joint.GeosyntheticHyperbolic.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setPeakAdhesionAtSigninfFactor(1.9)
	sf2.setPeakFrictionAngleAtSign0Factor(1.11)
	sf2.setResAdhesionAtSigninfFactor(1.12)
	sf2.setResFrictionAngleAtSign0Factor(1.13)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setPeakAdhesionAtSigninfFactor(1.14)
	sf4.setPeakFrictionAngleAtSign0Factor(1.15)
	sf4.setResAdhesionAtSigninfFactor(1.16)
	sf4.setResFrictionAngleAtSign0Factor(1.17)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint.GeosyntheticHyperbolic.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.GeosyntheticHyperbolic.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.GeosyntheticHyperbolic.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getPeakAdhesionAtSigninfFactor(), 1)
	assert(sf1.getPeakFrictionAngleAtSign0Factor(), 1)
	assert(sf1.getResAdhesionAtSigninfFactor(), 1)
	assert(sf1.getResFrictionAngleAtSign0Factor(), 1)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getPeakAdhesionAtSigninfFactor(), 1.9)
	assert(sf2_fin.getPeakFrictionAngleAtSign0Factor(), 1.11)
	assert(sf2_fin.getResAdhesionAtSigninfFactor(), 1.12)
	assert(sf2_fin.getResFrictionAngleAtSign0Factor(), 1.13)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getPeakAdhesionAtSigninfFactor(), 1.9)
	assert(sf3.getPeakFrictionAngleAtSign0Factor(), 1.11)
	assert(sf3.getResAdhesionAtSigninfFactor(), 1.12)
	assert(sf3.getResFrictionAngleAtSign0Factor(), 1.13)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getPeakAdhesionAtSigninfFactor(), 1.14)
	assert(sf4_fin.getPeakFrictionAngleAtSign0Factor(), 1.15)
	assert(sf4_fin.getResAdhesionAtSigninfFactor(), 1.16)
	assert(sf4_fin.getResFrictionAngleAtSign0Factor(), 1.17)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test20():
	joint = joint20

	joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SIMPLE)
		 
	joint.GeosyntheticHyperbolic.setApplyPorePressure(False)
	joint.GeosyntheticHyperbolic.setApplyAdditionalPressureInsideJoint(True)

	joint.GeosyntheticHyperbolic.setApplyStageFactors(True)

	sf2 = joint.GeosyntheticHyperbolic.stageFactorInterface.createStageFactor(2)
	sf4 = joint.GeosyntheticHyperbolic.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setPeakAdhesionAtSigninfFactor(1.9)
	sf2.setPeakFrictionAngleAtSign0Factor(1.11)
	sf2.setResAdhesionAtSigninfFactor(1.12)
	sf2.setResFrictionAngleAtSign0Factor(1.13)
	sf2.setAdditionalPressureInsideJointFactor(1.3)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setPeakAdhesionAtSigninfFactor(1.14)
	sf4.setPeakFrictionAngleAtSign0Factor(1.15)
	sf4.setResAdhesionAtSigninfFactor(1.16)
	sf4.setResFrictionAngleAtSign0Factor(1.17)
	sf4.setAdditionalPressureInsideJointFactor(1.7)

	sf_dict = joint.GeosyntheticHyperbolic.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.GeosyntheticHyperbolic.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.GeosyntheticHyperbolic.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getPeakAdhesionAtSigninfFactor(), 1)
	assert(sf1.getPeakFrictionAngleAtSign0Factor(), 1)
	assert(sf1.getResAdhesionAtSigninfFactor(), 1)
	assert(sf1.getResFrictionAngleAtSign0Factor(), 1)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getPeakAdhesionAtSigninfFactor(), 1.9)
	assert(sf2_fin.getPeakFrictionAngleAtSign0Factor(), 1.11)
	assert(sf2_fin.getResAdhesionAtSigninfFactor(), 1.12)
	assert(sf2_fin.getResFrictionAngleAtSign0Factor(), 1.13)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(), 1.3)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getPeakAdhesionAtSigninfFactor(), 1.9)
	assert(sf3.getPeakFrictionAngleAtSign0Factor(), 1.11)
	assert(sf3.getResAdhesionAtSigninfFactor(), 1.12)
	assert(sf3.getResFrictionAngleAtSign0Factor(), 1.13)
	assert(sf3.getAdditionalPressureInsideJointFactor(), 1.3)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getPeakAdhesionAtSigninfFactor(), 1.14)
	assert(sf4_fin.getPeakFrictionAngleAtSign0Factor(), 1.15)
	assert(sf4_fin.getResAdhesionAtSigninfFactor(), 1.16)
	assert(sf4_fin.getResFrictionAngleAtSign0Factor(), 1.17)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)

def test21():
	joint = joint21

	joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SOFTENING)
		 
	joint.HyperbolicSoftening.setApplyPorePressure(True)
	joint.HyperbolicSoftening.setApplyAdditionalPressureInsideJoint(True)

	joint.HyperbolicSoftening.setApplyStageFactors(True)

	sf2 = joint.HyperbolicSoftening.stageFactorInterface.createStageFactor(2)
	sf4 = joint.HyperbolicSoftening.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setPeakCohesionFactor(1.9)
	sf2.setPeakFrictionFactor(1.11)
	sf2.setResCohesionFactor(1.12)
	sf2.setResFrictionFactor(1.13)
	sf2.setTensileStrengthFactor(1.14)
	sf2.setResTensileStrengthFactor(1.15)
	sf2.setDeltaRFactor(1.16)
	sf2.setInitialSlopeFactor(1.17)
	sf2.setWorkSofteningFactor(False)
	sf2.setAdditionalPressureInsideJointFactor(1.3)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setPeakCohesionFactor(1.18)
	sf4.setPeakFrictionFactor(1.19)
	sf4.setResCohesionFactor(1.21)
	sf4.setResFrictionFactor(1.22)
	sf4.setTensileStrengthFactor(1.23)
	sf4.setResTensileStrengthFactor(1.24)
	sf4.setDeltaRFactor(1.25)
	sf4.setInitialSlopeFactor(1.26)
	sf4.setWorkSofteningFactor(True)
	sf4.setAdditionalPressureInsideJointFactor(1.7)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint.HyperbolicSoftening.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.HyperbolicSoftening.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.HyperbolicSoftening.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getPeakCohesionFactor(), 1)
	assert(sf1.getPeakFrictionFactor(), 1)
	assert(sf1.getResCohesionFactor(), 1)
	assert(sf1.getResFrictionFactor(), 1)
	assert(sf1.getTensileStrengthFactor(), 1)
	assert(sf1.getResTensileStrengthFactor(), 1)
	assert(sf1.getDeltaRFactor(), 1)
	assert(sf1.getInitialSlopeFactor(), 1)
	assert(sf1.getWorkSofteningFactor(), True)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getPeakCohesionFactor(), 1.9)
	assert(sf2_fin.getPeakFrictionFactor(), 1.11)
	assert(sf2_fin.getResCohesionFactor(), 1.12)
	assert(sf2_fin.getResFrictionFactor(), 1.13)
	assert(sf2_fin.getTensileStrengthFactor(), 1.14)
	assert(sf2_fin.getResTensileStrengthFactor(), 1.15)
	assert(sf2_fin.getDeltaRFactor(), 1.16)
	assert(sf2_fin.getInitialSlopeFactor(), 1.17)
	assert(sf2_fin.getWorkSofteningFactor(), False)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(), 1.3)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getPeakCohesionFactor(), 1.9)
	assert(sf3.getPeakFrictionFactor(), 1.11)
	assert(sf3.getResCohesionFactor(), 1.12)
	assert(sf3.getResFrictionFactor(), 1.13)
	assert(sf3.getTensileStrengthFactor(), 1.14)
	assert(sf3.getResTensileStrengthFactor(), 1.15)
	assert(sf3.getDeltaRFactor(), 1.16)
	assert(sf3.getInitialSlopeFactor(), 1.17)
	assert(sf3.getWorkSofteningFactor(), False)
	assert(sf3.getAdditionalPressureInsideJointFactor(), 1.3)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getPeakCohesionFactor(), 1.18)
	assert(sf4_fin.getPeakFrictionFactor(), 1.19)
	assert(sf4_fin.getResCohesionFactor(), 1.21)
	assert(sf4_fin.getResFrictionFactor(), 1.22)
	assert(sf4_fin.getTensileStrengthFactor(), 1.23)
	assert(sf4_fin.getResTensileStrengthFactor(), 1.24)
	assert(sf4_fin.getDeltaRFactor(), 1.25)
	assert(sf4_fin.getInitialSlopeFactor(), 1.26)
	assert(sf4_fin.getWorkSofteningFactor(), True)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test22():
	joint = joint22

	joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SOFTENING)
		 
	joint.HyperbolicSoftening.setApplyPorePressure(False)
	joint.HyperbolicSoftening.setApplyAdditionalPressureInsideJoint(False)

	joint.HyperbolicSoftening.setApplyStageFactors(True)

	sf2 = joint.HyperbolicSoftening.stageFactorInterface.createStageFactor(2)
	sf4 = joint.HyperbolicSoftening.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setPeakCohesionFactor(1.9)
	sf2.setPeakFrictionFactor(1.11)
	sf2.setResCohesionFactor(1.12)
	sf2.setResFrictionFactor(1.13)
	sf2.setTensileStrengthFactor(1.14)
	sf2.setResTensileStrengthFactor(1.15)
	sf2.setDeltaRFactor(1.16)
	sf2.setInitialSlopeFactor(1.17)
	sf2.setWorkSofteningFactor(False)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setPeakCohesionFactor(1.18)
	sf4.setPeakFrictionFactor(1.19)
	sf4.setResCohesionFactor(1.21)
	sf4.setResFrictionFactor(1.22)
	sf4.setTensileStrengthFactor(1.23)
	sf4.setResTensileStrengthFactor(1.24)
	sf4.setDeltaRFactor(1.25)
	sf4.setInitialSlopeFactor(1.26)
	sf4.setWorkSofteningFactor(True)

	sf_dict = joint.HyperbolicSoftening.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.HyperbolicSoftening.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.HyperbolicSoftening.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getPeakCohesionFactor(), 1)
	assert(sf1.getPeakFrictionFactor(), 1)
	assert(sf1.getResCohesionFactor(), 1)
	assert(sf1.getResFrictionFactor(), 1)
	assert(sf1.getTensileStrengthFactor(), 1)
	assert(sf1.getResTensileStrengthFactor(), 1)
	assert(sf1.getDeltaRFactor(), 1)
	assert(sf1.getInitialSlopeFactor(), 1)
	assert(sf1.getWorkSofteningFactor(), True)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getPeakCohesionFactor(), 1.9)
	assert(sf2_fin.getPeakFrictionFactor(), 1.11)
	assert(sf2_fin.getResCohesionFactor(), 1.12)
	assert(sf2_fin.getResFrictionFactor(), 1.13)
	assert(sf2_fin.getTensileStrengthFactor(), 1.14)
	assert(sf2_fin.getResTensileStrengthFactor(), 1.15)
	assert(sf2_fin.getDeltaRFactor(), 1.16)
	assert(sf2_fin.getInitialSlopeFactor(), 1.17)
	assert(sf2_fin.getWorkSofteningFactor(), False)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getPeakCohesionFactor(), 1.9)
	assert(sf3.getPeakFrictionFactor(), 1.11)
	assert(sf3.getResCohesionFactor(), 1.12)
	assert(sf3.getResFrictionFactor(), 1.13)
	assert(sf3.getTensileStrengthFactor(), 1.14)
	assert(sf3.getResTensileStrengthFactor(), 1.15)
	assert(sf3.getDeltaRFactor(), 1.16)
	assert(sf3.getInitialSlopeFactor(), 1.17)
	assert(sf3.getWorkSofteningFactor(), False)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getPeakCohesionFactor(), 1.18)
	assert(sf4_fin.getPeakFrictionFactor(), 1.19)
	assert(sf4_fin.getResCohesionFactor(), 1.21)
	assert(sf4_fin.getResFrictionFactor(), 1.22)
	assert(sf4_fin.getTensileStrengthFactor(), 1.23)
	assert(sf4_fin.getResTensileStrengthFactor(), 1.24)
	assert(sf4_fin.getDeltaRFactor(), 1.25)
	assert(sf4_fin.getInitialSlopeFactor(), 1.26)
	assert(sf4_fin.getWorkSofteningFactor(), True)

def test23():
	joint = joint23

	joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SOFTENING)
		 
	joint.HyperbolicSoftening.setApplyPorePressure(True)
	joint.HyperbolicSoftening.setApplyAdditionalPressureInsideJoint(False)

	joint.HyperbolicSoftening.setApplyStageFactors(True)

	sf2 = joint.HyperbolicSoftening.stageFactorInterface.createStageFactor(2)
	sf4 = joint.HyperbolicSoftening.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setPeakCohesionFactor(1.9)
	sf2.setPeakFrictionFactor(1.11)
	sf2.setResCohesionFactor(1.12)
	sf2.setResFrictionFactor(1.13)
	sf2.setTensileStrengthFactor(1.14)
	sf2.setResTensileStrengthFactor(1.15)
	sf2.setDeltaRFactor(1.16)
	sf2.setInitialSlopeFactor(1.17)
	sf2.setWorkSofteningFactor(False)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setPeakCohesionFactor(1.18)
	sf4.setPeakFrictionFactor(1.19)
	sf4.setResCohesionFactor(1.21)
	sf4.setResFrictionFactor(1.22)
	sf4.setTensileStrengthFactor(1.23)
	sf4.setResTensileStrengthFactor(1.24)
	sf4.setDeltaRFactor(1.25)
	sf4.setInitialSlopeFactor(1.26)
	sf4.setWorkSofteningFactor(True)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint.HyperbolicSoftening.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.HyperbolicSoftening.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.HyperbolicSoftening.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getPeakCohesionFactor(), 1)
	assert(sf1.getPeakFrictionFactor(), 1)
	assert(sf1.getResCohesionFactor(), 1)
	assert(sf1.getResFrictionFactor(), 1)
	assert(sf1.getTensileStrengthFactor(), 1)
	assert(sf1.getResTensileStrengthFactor(), 1)
	assert(sf1.getDeltaRFactor(), 1)
	assert(sf1.getInitialSlopeFactor(), 1)
	assert(sf1.getWorkSofteningFactor(), True)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getPeakCohesionFactor(), 1.9)
	assert(sf2_fin.getPeakFrictionFactor(), 1.11)
	assert(sf2_fin.getResCohesionFactor(), 1.12)
	assert(sf2_fin.getResFrictionFactor(), 1.13)
	assert(sf2_fin.getTensileStrengthFactor(), 1.14)
	assert(sf2_fin.getResTensileStrengthFactor(), 1.15)
	assert(sf2_fin.getDeltaRFactor(), 1.16)
	assert(sf2_fin.getInitialSlopeFactor(), 1.17)
	assert(sf2_fin.getWorkSofteningFactor(), False)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getPeakCohesionFactor(), 1.9)
	assert(sf3.getPeakFrictionFactor(), 1.11)
	assert(sf3.getResCohesionFactor(), 1.12)
	assert(sf3.getResFrictionFactor(), 1.13)
	assert(sf3.getTensileStrengthFactor(), 1.14)
	assert(sf3.getResTensileStrengthFactor(), 1.15)
	assert(sf3.getDeltaRFactor(), 1.16)
	assert(sf3.getInitialSlopeFactor(), 1.17)
	assert(sf3.getWorkSofteningFactor(), False)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getPeakCohesionFactor(), 1.18)
	assert(sf4_fin.getPeakFrictionFactor(), 1.19)
	assert(sf4_fin.getResCohesionFactor(), 1.21)
	assert(sf4_fin.getResFrictionFactor(), 1.22)
	assert(sf4_fin.getTensileStrengthFactor(), 1.23)
	assert(sf4_fin.getResTensileStrengthFactor(), 1.24)
	assert(sf4_fin.getDeltaRFactor(), 1.25)
	assert(sf4_fin.getInitialSlopeFactor(), 1.26)
	assert(sf4_fin.getWorkSofteningFactor(), True)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test24():
	joint = joint24

	joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SOFTENING)
		 
	joint.HyperbolicSoftening.setApplyPorePressure(False)
	joint.HyperbolicSoftening.setApplyAdditionalPressureInsideJoint(True)

	joint.HyperbolicSoftening.setApplyStageFactors(True)

	sf2 = joint.HyperbolicSoftening.stageFactorInterface.createStageFactor(2)
	sf4 = joint.HyperbolicSoftening.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setPeakCohesionFactor(1.9)
	sf2.setPeakFrictionFactor(1.11)
	sf2.setResCohesionFactor(1.12)
	sf2.setResFrictionFactor(1.13)
	sf2.setTensileStrengthFactor(1.14)
	sf2.setResTensileStrengthFactor(1.15)
	sf2.setDeltaRFactor(1.16)
	sf2.setInitialSlopeFactor(1.17)
	sf2.setWorkSofteningFactor(False)
	sf2.setAdditionalPressureInsideJointFactor(1.3)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setPeakCohesionFactor(1.18)
	sf4.setPeakFrictionFactor(1.19)
	sf4.setResCohesionFactor(1.21)
	sf4.setResFrictionFactor(1.22)
	sf4.setTensileStrengthFactor(1.23)
	sf4.setResTensileStrengthFactor(1.24)
	sf4.setDeltaRFactor(1.25)
	sf4.setInitialSlopeFactor(1.26)
	sf4.setWorkSofteningFactor(True)
	sf4.setAdditionalPressureInsideJointFactor(1.7)

	sf_dict = joint.HyperbolicSoftening.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.HyperbolicSoftening.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.HyperbolicSoftening.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getPeakCohesionFactor(), 1)
	assert(sf1.getPeakFrictionFactor(), 1)
	assert(sf1.getResCohesionFactor(), 1)
	assert(sf1.getResFrictionFactor(), 1)
	assert(sf1.getTensileStrengthFactor(), 1)
	assert(sf1.getResTensileStrengthFactor(), 1)
	assert(sf1.getDeltaRFactor(), 1)
	assert(sf1.getInitialSlopeFactor(), 1)
	assert(sf1.getWorkSofteningFactor(), True)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getPeakCohesionFactor(), 1.9)
	assert(sf2_fin.getPeakFrictionFactor(), 1.11)
	assert(sf2_fin.getResCohesionFactor(), 1.12)
	assert(sf2_fin.getResFrictionFactor(), 1.13)
	assert(sf2_fin.getTensileStrengthFactor(), 1.14)
	assert(sf2_fin.getResTensileStrengthFactor(), 1.15)
	assert(sf2_fin.getDeltaRFactor(), 1.16)
	assert(sf2_fin.getInitialSlopeFactor(), 1.17)
	assert(sf2_fin.getWorkSofteningFactor(), False)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(), 1.3)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getPeakCohesionFactor(), 1.9)
	assert(sf3.getPeakFrictionFactor(), 1.11)
	assert(sf3.getResCohesionFactor(), 1.12)
	assert(sf3.getResFrictionFactor(), 1.13)
	assert(sf3.getTensileStrengthFactor(), 1.14)
	assert(sf3.getResTensileStrengthFactor(), 1.15)
	assert(sf3.getDeltaRFactor(), 1.16)
	assert(sf3.getInitialSlopeFactor(), 1.17)
	assert(sf3.getWorkSofteningFactor(), False)
	assert(sf3.getAdditionalPressureInsideJointFactor(), 1.3)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getPeakCohesionFactor(), 1.18)
	assert(sf4_fin.getPeakFrictionFactor(), 1.19)
	assert(sf4_fin.getResCohesionFactor(), 1.21)
	assert(sf4_fin.getResFrictionFactor(), 1.22)
	assert(sf4_fin.getTensileStrengthFactor(), 1.23)
	assert(sf4_fin.getResTensileStrengthFactor(), 1.24)
	assert(sf4_fin.getDeltaRFactor(), 1.25)
	assert(sf4_fin.getInitialSlopeFactor(), 1.26)
	assert(sf4_fin.getWorkSofteningFactor(), True)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)

def test25():
	joint = joint25

	joint.setSlipCriterion(JointTypes.JOINT_MATERIAL_DEPENDENT)
		 
	joint.MaterialDependent.setApplyPorePressure(True)
	joint.MaterialDependent.setApplyAdditionalPressureInsideJoint(True)

	joint.MaterialDependent.setApplyStageFactors(True)

	sf2 = joint.MaterialDependent.stageFactorInterface.createStageFactor(2)
	sf4 = joint.MaterialDependent.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setInterfaceCoefficientFactor(1.9)
	sf2.setAdditionalPressureInsideJointFactor(1.3)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setInterfaceCoefficientFactor(1.11)
	sf4.setAdditionalPressureInsideJointFactor(1.7)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint.MaterialDependent.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.MaterialDependent.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.MaterialDependent.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getInterfaceCoefficientFactor(), 1)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getInterfaceCoefficientFactor(), 1.9)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(), 1.3)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getInterfaceCoefficientFactor(), 1.9)
	assert(sf3.getAdditionalPressureInsideJointFactor(), 1.3)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getInterfaceCoefficientFactor(), 1.11)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test26():
	joint = joint26

	joint.setSlipCriterion(JointTypes.JOINT_MATERIAL_DEPENDENT)
		 
	joint.MaterialDependent.setApplyPorePressure(False)
	joint.MaterialDependent.setApplyAdditionalPressureInsideJoint(False)

	joint.MaterialDependent.setApplyStageFactors(True)

	sf2 = joint.MaterialDependent.stageFactorInterface.createStageFactor(2)
	sf4 = joint.MaterialDependent.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setInterfaceCoefficientFactor(1.9)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setInterfaceCoefficientFactor(1.11)

	sf_dict = joint.MaterialDependent.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.MaterialDependent.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.MaterialDependent.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getInterfaceCoefficientFactor(), 1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getInterfaceCoefficientFactor(), 1.9)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getInterfaceCoefficientFactor(), 1.9)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getInterfaceCoefficientFactor(), 1.11)

def test27():
	joint = joint27

	joint.setSlipCriterion(JointTypes.JOINT_MATERIAL_DEPENDENT)
		 
	joint.MaterialDependent.setApplyPorePressure(True)
	joint.MaterialDependent.setApplyAdditionalPressureInsideJoint(False)

	joint.MaterialDependent.setApplyStageFactors(True)

	sf2 = joint.MaterialDependent.stageFactorInterface.createStageFactor(2)
	sf4 = joint.MaterialDependent.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setInterfaceCoefficientFactor(1.9)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setInterfaceCoefficientFactor(1.11)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint.MaterialDependent.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.MaterialDependent.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.MaterialDependent.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getInterfaceCoefficientFactor(), 1)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getInterfaceCoefficientFactor(), 1.9)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getInterfaceCoefficientFactor(), 1.9)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getInterfaceCoefficientFactor(), 1.11)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test28():
	joint = joint28

	joint.setSlipCriterion(JointTypes.JOINT_MATERIAL_DEPENDENT)
		 
	joint.MaterialDependent.setApplyPorePressure(False)
	joint.MaterialDependent.setApplyAdditionalPressureInsideJoint(True)

	joint.MaterialDependent.setApplyStageFactors(True)

	sf2 = joint.MaterialDependent.stageFactorInterface.createStageFactor(2)
	sf4 = joint.MaterialDependent.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setInterfaceCoefficientFactor(1.9)
	sf2.setAdditionalPressureInsideJointFactor(1.3)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setInterfaceCoefficientFactor(1.11)
	sf4.setAdditionalPressureInsideJointFactor(1.7)

	sf_dict = joint.MaterialDependent.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.MaterialDependent.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.MaterialDependent.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getInterfaceCoefficientFactor(), 1)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getInterfaceCoefficientFactor(), 1.9)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(), 1.3)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getInterfaceCoefficientFactor(), 1.9)
	assert(sf3.getAdditionalPressureInsideJointFactor(), 1.3)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getInterfaceCoefficientFactor(), 1.11)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)

def test29():
	joint = joint29

	joint.setSlipCriterion(JointTypes.JOINT_DISPLACEMENT_DEPENDENT)
	joint.DisplacementDependent.setDisplacementDependentTable([[1,1,1,1],[2,2,2,2]])
		 
	joint.DisplacementDependent.setApplyPorePressure(True)
	joint.DisplacementDependent.setApplyAdditionalPressureInsideJoint(True)

	joint.DisplacementDependent.setApplyStageFactors(True)

	sf2 = joint.DisplacementDependent.stageFactorInterface.createStageFactor(2)
	sf4 = joint.DisplacementDependent.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setShearDisplacementFactor(1.9)
	sf2.setCohesionFactor(1.11)
	sf2.setFrictionAngleFactor(1.12)
	sf2.setTensileStrengthFactor(1.13)
	sf2.setAdditionalPressureInsideJointFactor(1.3)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setShearDisplacementFactor(1.14)
	sf4.setCohesionFactor(1.15)
	sf4.setFrictionAngleFactor(1.16)
	sf4.setTensileStrengthFactor(1.17)
	sf4.setAdditionalPressureInsideJointFactor(1.7)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint.DisplacementDependent.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.DisplacementDependent.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.DisplacementDependent.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getShearDisplacementFactor(), 1)
	assert(sf1.getCohesionFactor(), 1)
	assert(sf1.getFrictionAngleFactor(), 1)
	assert(sf1.getTensileStrengthFactor(), 1)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getShearDisplacementFactor(), 1.9)
	assert(sf2_fin.getCohesionFactor(), 1.11)
	assert(sf2_fin.getFrictionAngleFactor(), 1.12)
	assert(sf2_fin.getTensileStrengthFactor(), 1.13)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(), 1.3)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getShearDisplacementFactor(), 1.9)
	assert(sf3.getCohesionFactor(), 1.11)
	assert(sf3.getFrictionAngleFactor(), 1.12)
	assert(sf3.getTensileStrengthFactor(), 1.13)
	assert(sf3.getAdditionalPressureInsideJointFactor(), 1.3)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getShearDisplacementFactor(), 1.14)
	assert(sf4_fin.getCohesionFactor(), 1.15)
	assert(sf4_fin.getFrictionAngleFactor(), 1.16)
	assert(sf4_fin.getTensileStrengthFactor(), 1.17)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test30():
	joint = joint30

	joint.setSlipCriterion(JointTypes.JOINT_DISPLACEMENT_DEPENDENT)
	joint.DisplacementDependent.setDisplacementDependentTable([[1,1,1,1],[2,2,2,2]])
		 
	joint.DisplacementDependent.setApplyPorePressure(False)
	joint.DisplacementDependent.setApplyAdditionalPressureInsideJoint(False)

	joint.DisplacementDependent.setApplyStageFactors(True)

	sf2 = joint.DisplacementDependent.stageFactorInterface.createStageFactor(2)
	sf4 = joint.DisplacementDependent.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setShearDisplacementFactor(1.9)
	sf2.setCohesionFactor(1.11)
	sf2.setFrictionAngleFactor(1.12)
	sf2.setTensileStrengthFactor(1.13)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setShearDisplacementFactor(1.14)
	sf4.setCohesionFactor(1.15)
	sf4.setFrictionAngleFactor(1.16)
	sf4.setTensileStrengthFactor(1.17)

	sf_dict = joint.DisplacementDependent.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.DisplacementDependent.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.DisplacementDependent.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getShearDisplacementFactor(), 1)
	assert(sf1.getCohesionFactor(), 1)
	assert(sf1.getFrictionAngleFactor(), 1)
	assert(sf1.getTensileStrengthFactor(), 1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getShearDisplacementFactor(), 1.9)
	assert(sf2_fin.getCohesionFactor(), 1.11)
	assert(sf2_fin.getFrictionAngleFactor(), 1.12)
	assert(sf2_fin.getTensileStrengthFactor(), 1.13)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getShearDisplacementFactor(), 1.9)
	assert(sf3.getCohesionFactor(), 1.11)
	assert(sf3.getFrictionAngleFactor(), 1.12)
	assert(sf3.getTensileStrengthFactor(), 1.13)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getShearDisplacementFactor(), 1.14)
	assert(sf4_fin.getCohesionFactor(), 1.15)
	assert(sf4_fin.getFrictionAngleFactor(), 1.16)
	assert(sf4_fin.getTensileStrengthFactor(), 1.17)

def test31():
	joint = joint31

	joint.setSlipCriterion(JointTypes.JOINT_DISPLACEMENT_DEPENDENT)
	joint.DisplacementDependent.setDisplacementDependentTable([[1,1,1,1],[2,2,2,2]])
		 
	joint.DisplacementDependent.setApplyPorePressure(True)
	joint.DisplacementDependent.setApplyAdditionalPressureInsideJoint(False)

	joint.DisplacementDependent.setApplyStageFactors(True)

	sf2 = joint.DisplacementDependent.stageFactorInterface.createStageFactor(2)
	sf4 = joint.DisplacementDependent.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setShearDisplacementFactor(1.9)
	sf2.setCohesionFactor(1.11)
	sf2.setFrictionAngleFactor(1.12)
	sf2.setTensileStrengthFactor(1.13)
	sf2.setGroundwaterPressureFactor(1.4)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setShearDisplacementFactor(1.14)
	sf4.setCohesionFactor(1.15)
	sf4.setFrictionAngleFactor(1.16)
	sf4.setTensileStrengthFactor(1.17)
	sf4.setGroundwaterPressureFactor(1.8)

	sf_dict = joint.DisplacementDependent.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.DisplacementDependent.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.DisplacementDependent.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getShearDisplacementFactor(), 1)
	assert(sf1.getCohesionFactor(), 1)
	assert(sf1.getFrictionAngleFactor(), 1)
	assert(sf1.getTensileStrengthFactor(), 1)
	assert(sf1.getGroundwaterPressureFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getShearDisplacementFactor(), 1.9)
	assert(sf2_fin.getCohesionFactor(), 1.11)
	assert(sf2_fin.getFrictionAngleFactor(), 1.12)
	assert(sf2_fin.getTensileStrengthFactor(), 1.13)
	assert(sf2_fin.getGroundwaterPressureFactor(),1.4)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getShearDisplacementFactor(), 1.9)
	assert(sf3.getCohesionFactor(), 1.11)
	assert(sf3.getFrictionAngleFactor(), 1.12)
	assert(sf3.getTensileStrengthFactor(), 1.13)
	assert(sf3.getGroundwaterPressureFactor(),1.4)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getShearDisplacementFactor(), 1.14)
	assert(sf4_fin.getCohesionFactor(), 1.15)
	assert(sf4_fin.getFrictionAngleFactor(), 1.16)
	assert(sf4_fin.getTensileStrengthFactor(), 1.17)
	assert(sf4_fin.getGroundwaterPressureFactor(),1.8)

def test32():
	joint = joint32

	joint.setSlipCriterion(JointTypes.JOINT_DISPLACEMENT_DEPENDENT)
	joint.DisplacementDependent.setDisplacementDependentTable([[1,1,1,1],[2,2,2,2]])
		 
	joint.DisplacementDependent.setApplyPorePressure(False)
	joint.DisplacementDependent.setApplyAdditionalPressureInsideJoint(True)

	joint.DisplacementDependent.setApplyStageFactors(True)

	sf2 = joint.DisplacementDependent.stageFactorInterface.createStageFactor(2)
	sf4 = joint.DisplacementDependent.stageFactorInterface.createStageFactor(4)

	sf2.setNormalStiffnessFactor(1.1)
	sf2.setShearStiffnessFactor(1.2)
	sf2.setJointPermeableFactor(True)
	sf2.setShearDisplacementFactor(1.9)
	sf2.setCohesionFactor(1.11)
	sf2.setFrictionAngleFactor(1.12)
	sf2.setTensileStrengthFactor(1.13)
	sf2.setAdditionalPressureInsideJointFactor(1.3)

	sf4.setNormalStiffnessFactor(1.5)
	sf4.setShearStiffnessFactor(1.6)
	sf4.setJointPermeableFactor(False)
	sf4.setShearDisplacementFactor(1.14)
	sf4.setCohesionFactor(1.15)
	sf4.setFrictionAngleFactor(1.16)
	sf4.setTensileStrengthFactor(1.17)
	sf4.setAdditionalPressureInsideJointFactor(1.7)

	sf_dict = joint.DisplacementDependent.stageFactorInterface.getDefinedStageFactors()

	sf1 = joint.DisplacementDependent.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = joint.DisplacementDependent.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getNormalStiffnessFactor(),1)
	assert(sf1.getShearStiffnessFactor(),1)
	assert(sf1.getJointPermeableFactor(),True)
	assert(sf1.getShearDisplacementFactor(), 1)
	assert(sf1.getCohesionFactor(), 1)
	assert(sf1.getFrictionAngleFactor(), 1)
	assert(sf1.getTensileStrengthFactor(), 1)
	assert(sf1.getAdditionalPressureInsideJointFactor(),1)

	assert(sf2_fin.getNormalStiffnessFactor(),1.1)
	assert(sf2_fin.getShearStiffnessFactor(),1.2)
	assert(sf2_fin.getJointPermeableFactor(),True)
	assert(sf2_fin.getShearDisplacementFactor(), 1.9)
	assert(sf2_fin.getCohesionFactor(), 1.11)
	assert(sf2_fin.getFrictionAngleFactor(), 1.12)
	assert(sf2_fin.getTensileStrengthFactor(), 1.13)
	assert(sf2_fin.getAdditionalPressureInsideJointFactor(), 1.3)

	assert(sf3.getNormalStiffnessFactor(),1.1)
	assert(sf3.getShearStiffnessFactor(),1.2)
	assert(sf3.getJointPermeableFactor(),True)
	assert(sf3.getShearDisplacementFactor(), 1.9)
	assert(sf3.getCohesionFactor(), 1.11)
	assert(sf3.getFrictionAngleFactor(), 1.12)
	assert(sf3.getTensileStrengthFactor(), 1.13)
	assert(sf3.getAdditionalPressureInsideJointFactor(), 1.3)

	assert(sf4_fin.getNormalStiffnessFactor(),1.5)
	assert(sf4_fin.getShearStiffnessFactor(),1.6)
	assert(sf4_fin.getJointPermeableFactor(),False)
	assert(sf4_fin.getShearDisplacementFactor(), 1.14)
	assert(sf4_fin.getCohesionFactor(), 1.15)
	assert(sf4_fin.getFrictionAngleFactor(), 1.16)
	assert(sf4_fin.getTensileStrengthFactor(), 1.17)
	assert(sf4_fin.getAdditionalPressureInsideJointFactor(),1.7)

def test33():
	joint = joint33

	joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)

	joint.MohrCoulomb.setApplyStageFactors(True)
	joint.SetAllowSlipStartFromStage(2)

	assert(joint.MohrCoulomb.getApplyStageFactors(), True)
	assert(joint.GetAllowSlipStartFromStage(), 2)




test1()
test2()
test3()
test4()
test5()
test6()
test7() 
test8()
test9()
test10()
test11()
test12()
test13()
test14()
test15()
test16()
test17()
test18()
test19()
test20()
test21()
test22()
test23()
test24()
test25()
test26()
test27()
test28()
test29()
test30()
test31()
test32()
test33()

model.save()

pass