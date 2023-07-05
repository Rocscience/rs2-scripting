from RS2Modeler import RS2Modeler

modeler = RS2Modeler()

document = modeler.openFile('C:/Intel/simple_3_stage.fez')
bolt = modeler.getFirstBolt()

bolt.setBoltType(bolt.BoltTypes.QUEENS_CABLE)
bolt.setAddBulges(True)

bolt.setBulgeLocations([26,63,82])
print(bolt.getBulgeLocations())