from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\example_rs2_file.fez")

linerList = model.getAllLinerProperties()
liner1 = linerList[0]

liner1.setPoissonsRatio(0.49)
print(liner1.getPoissonsRatio())

liner1.setLinerType(liner1.LinerTypes.P2_LINER_STANDARD_BEAM)
print(liner1.getLinerType())

liner1.setMethod(liner1.GeometryChoice.LNP_USE_THICKNESS)
print(liner1.getMethod())

liner1.setThickness(20)
print(liner1.getThickness())

liner1.setYoungsModulus(0.3)
print(liner1.getYoungsModulus())

liner1.setPoissonsRatio(0.35)
print(liner1.getPoissonsRatio())

liner1.setMaterialType(liner1.MaterialType.ELASTIC)
