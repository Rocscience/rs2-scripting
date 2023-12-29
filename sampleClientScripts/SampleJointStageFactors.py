from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez")

joint = model.getJointPropertyByName("Joint 1")
joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
mohrCoulombFactors = joint.MohrCoulomb.getStageFactors()
stage1mohrCoulombFactors = mohrCoulombFactors[0]
# Update the stage factor fields for the project
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

joint.setSlipCriterion(JointTypes.JOINT_BARTON_BANDIS) 

bartonBandisfactors = joint.BartonBandis.getStageFactors()
stage1bartonBandisFactors = bartonBandisfactors[0]
# Update the stage factor fields for the project
stage1bartonBandisFactors.setNormalStiffnessFactor(3)
stage1bartonBandisFactors.setShearStiffnessFactor(3) 
stage1bartonBandisFactors.setJRCFactor(3) 
stage1bartonBandisFactors.setJCSFactor(3) 
stage1bartonBandisFactors.setResidualFrictionAngleFactor(3)
stage1bartonBandisFactors.setAdditionalPressureInsideJointFactor(6)
stage1bartonBandisFactors.setGroundwaterPressureFactor(6)

joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SIMPLE)

geoSynfactors = joint.GeosyntheticHyperbolic.getStageFactors()
stage1geoSynFactors = geoSynfactors[0]
# Update the stage factor fields for the project
stage1geoSynFactors.setNormalStiffnessFactor(3) 
stage1geoSynFactors.setShearStiffnessFactor(3)
stage1geoSynFactors.setPeakAdhesionAtSigninfFactor(3)
stage1geoSynFactors.setPeakFrictionAngleAtSign0Factor(3) 
stage1geoSynFactors.setResAdhesionAtSigninfFactor(3)
stage1geoSynFactors.setResFrictionAngleAtSign0Factor(3)
stage1geoSynFactors.setAdditionalPressureInsideJointFactor(6)
stage1geoSynFactors.setGroundwaterPressureFactor(6)

joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SOFTENING)

hyperbolicSoftFactors = joint.HyperbolicSoftening.getStageFactors()
stage1hyperbolicSoftFactors = hyperbolicSoftFactors[0]
# Update the stage factor fields for the project
stage1hyperbolicSoftFactors.setNormalStiffnessFactor(3)
stage1hyperbolicSoftFactors.setShearStiffnessFactor(3)
stage1hyperbolicSoftFactors.setPeakCohesionFactor(3)
stage1hyperbolicSoftFactors.setPeakFrictionFactor(3)
stage1hyperbolicSoftFactors.setResCohesionFactor(3)
stage1hyperbolicSoftFactors.setResFrictionFactor(3)
stage1hyperbolicSoftFactors.setTensileStrengthFactor(3)
stage1hyperbolicSoftFactors.setResTensileStrengthFactor(3)
stage1hyperbolicSoftFactors.setDeltaRFactor(3)
stage1hyperbolicSoftFactors.setInitialSlopeFactor(3)
stage1hyperbolicSoftFactors.setWorkSofteningFactor(False)
stage1hyperbolicSoftFactors.setAdditionalPressureInsideJointFactor(6)
stage1hyperbolicSoftFactors.setGroundwaterPressureFactor(6)

joint.setSlipCriterion(JointTypes.JOINT_MATERIAL_DEPENDENT) 

matDepfactors = joint.MaterialDependent.getStageFactors()
stage1MatDepFactors = matDepfactors[0]
# Update the stage factor fields for the project
stage1MatDepFactors.setNormalStiffnessFactor(3)
stage1MatDepFactors.setShearStiffnessFactor(3) 
stage1MatDepFactors.setInterfaceCoefficientFactor(3) 
stage1MatDepFactors.setAdditionalPressureInsideJointFactor(6)
stage1MatDepFactors.setGroundwaterPressureFactor(6)

joint.setSlipCriterion(JointTypes.JOINT_DISPLACEMENT_DEPENDENT)

DispDepfactors = joint.DisplacementDependent.getStageFactors()
stage1DisDepnFactors = DispDepfactors[0]
# Update the stage factor fields for the project
stage1DisDepnFactors.setNormalStiffnessFactor(3)
stage1DisDepnFactors.setShearStiffnessFactor(3)
stage1DisDepnFactors.setShearDisplacementFactor(3)
stage1DisDepnFactors.setCohesionFactor(3)
stage1DisDepnFactors.setFrictionAngleFactor(3)
stage1DisDepnFactors.setTensileStrengthFactor(3)
stage1DisDepnFactors.setAdditionalPressureInsideJointFactor(6)
stage1DisDepnFactors.setGroundwaterPressureFactor(6)

print("Successfully updated stage factor values")