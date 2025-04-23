from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60064)
modeler = RS2Modeler(port=60064)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

material = model.getAllMaterialProperties()[0]

# Make sure to set Material Stiffness Type to Isotropic before changing Datum Dependency Properties
material.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
material.Datum.setUsingDatum(True)

youngDatum = material.Datum.getDatumYoungsModulus()
youngDatum.setUsing(True)
youngDatum.setType(DatumType.DATUM_TYPE_DEPTH)
youngDatum.setDatum(5)
youngDatum.setType(DatumType.DATUM_TYPE_RADIAL)
youngDatum.setCenter(3.5,2)
youngDatum.setUseCutoff(True)
youngDatum.setChange(0.5)
youngDatum.setCutoff(0.8)

print("\nYoungs Modulus Datum Dependent Type:")
print(f"Datum Type = {youngDatum.getType()}, Datum Value = {youngDatum.getDatum()}, Center = {youngDatum.getCenter()}")
print(f"Use Cutoff = {youngDatum.getUseCutoff()}, Datum Change = {youngDatum.getChange()}, Cutoff = {youngDatum.getCutoff()}\n")

# Set Material Strength failure criterion to Mohr-Coulomb and material type to Plastic
# This allows to specify properties for Friction and Cohesion Datum Dependent Types
material.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
material.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

frictionDatum = material.Datum.getDatumFrictionAngle()
frictionDatum.setUsing(True)
frictionDatum.setType(DatumType.DATUM_TYPE_DEPTH)
frictionDatum.setDatum(5)
frictionDatum.setType(DatumType.DATUM_TYPE_DEPTH)
frictionDatum.setCenter(5, 6)
frictionDatum.setPeakChange(1)
frictionDatum.setUsePeakCutoff(True)
frictionDatum.setPeakCutoffValue(44)
frictionDatum.setResidualChange(0.5)
frictionDatum.setUseResidualCutoff(True)
frictionDatum.setResidualCutoffValue(45)

print("\nFriction Datum Dependent Type:")
print(f"Datum Type = {frictionDatum.getType()}, Datum Value = {frictionDatum.getDatum()}, Center = {frictionDatum.getCenter()}")
print(f"Use Peak Cutoff = {frictionDatum.getUsePeakCutoff()}, Peak Change = {frictionDatum.getPeakChange()}, Peak Cutoff = {frictionDatum.getPeakCutoffValue()}")
print(f"Use Residual Cutoff = {frictionDatum.getUseResidualCutoff()}, Residual Cutoff Value = {frictionDatum.getResidualCutoffValue()}\n")

cohesion = material.Datum.getDatumCohesion()
cohesion.setType(DatumType.DATUM_TYPE_DEPTH)
cohesion.setDatum(5)
cohesion.setType(DatumType.DATUM_TYPE_RADIAL)
cohesion.setCenter(5, 6)
cohesion.setPeakChange(1)
cohesion.setUsePeakCutoff(True)
cohesion.setPeakCutoffValue(44)
cohesion.setResidualChange(0.5)
cohesion.setUseResidualCutoff(True)
cohesion.setResidualCutoffValue(45)

print("\nCohesion Datum Dependent Type:")
print(f"Datum Type = {cohesion.getType()}, Datum Value = {cohesion.getDatum()}, Center = {cohesion.getCenter()}")
print(f"Use Peak Cutoff = {cohesion.getUsePeakCutoff()}, Peak Change = {cohesion.getPeakChange()}, Peak Cutoff = {cohesion.getPeakCutoffValue()}")
print(f"Use Residual Cutoff = {cohesion.getUseResidualCutoff()}, Residual Cutoff Value = {cohesion.getResidualCutoffValue()}\n")

# Manipulation of Datum Stage Factor Properties for stage 2

# Make sure to stage Datum Stage Factor option before manipulating any factor properties
material.StageFactors.setStageDatumStageFactor(True)
definedStageFactors = material.StageFactors.getDefinedStageFactors()
newStageFactor = material.StageFactors.createStageFactor(2)
definedStageFactors[2] = newStageFactor
material.StageFactors.setDefinedStageFactors(definedStageFactors)
datumStageFactor = material.Datum.stageFactorInterface.getDefinedStageFactors()[2]

datumYoungStageFactor = datumStageFactor.getDatumYoungsStageFactor()
datumYoungStageFactor.setChange(0.2)
datumYoungStageFactor.setDatum(3)
datumYoungStageFactor.setPeakCutoffValue(4.42)

print(f"Change Factor = {datumYoungStageFactor.getChange()}, Datum Factor Value= {datumYoungStageFactor.getDatum()}, Peak Cutoff Value Factor = {datumYoungStageFactor.getPeakCutoffValue()}")

model.close()
modeler.closeProgram()