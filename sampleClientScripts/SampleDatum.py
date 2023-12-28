from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *
#keepme
modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")
material = model.getMaterialPropertyByName("Material 1")
material.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

material.Datum.setUsingDatum(True)

youngDatum = material.Datum.getDatumYoungsModulus()
youngDatum.setUsing(True)

frictionDatum = material.Datum.getDatumFriction()
frictionDatum.setUsing(True)

youngDatum.setType(DatumType.DATUM_TYPE_RADIAL)
youngDatum.setCenter(5,6)
youngDatum.setUseCutoff(True)
youngDatum.setChange(0.11)
youngDatum.setCutoff(0.22)

print(youngDatum.getType())
print(youngDatum.getCenter())
print(youngDatum.getUseCutoff())
print(youngDatum.getChange())
print(youngDatum.getCutoff())

frictionDatum.setType(DatumType.DATUM_TYPE_DEPTH)
frictionDatum.setDatum(5)
frictionDatum.setPeakChange(1)
frictionDatum.setUsePeakCutoff(True)
frictionDatum.setPeakCutoffValue(44)
frictionDatum.setResidualChange(0.5)
frictionDatum.setUseResidualCutoff(True)
frictionDatum.setResidualCutoffValue(45)

print(frictionDatum.getType())
print(frictionDatum.getDatum())
print(frictionDatum.getPeakChange())
print(frictionDatum.getUsePeakCutoff())
print(frictionDatum.getPeakCutoffValue())
print(frictionDatum.getResidualChange())
print(frictionDatum.getUseResidualCutoff())
print(frictionDatum.getResidualCutoffValue())
