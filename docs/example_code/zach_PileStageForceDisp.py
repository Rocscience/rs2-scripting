from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\Pile\stageForceDisp_final.fez")

pileList = model.getAllPileProperties()
pile1 = pileList[0]

def test1():
	pile1.setStageForceDisplacement(True)
	sf_init = pile1.ForceDisplacement.stageFactorInterface.getDefinedStageFactors()
	sf1 = sf_init[1]
	sf2 = pile1.ForceDisplacement.stageFactorInterface.createStageFactor(2)
	sf3 = pile1.ForceDisplacement.stageFactorInterface.createStageFactor(3)
	sf4 = pile1.ForceDisplacement.stageFactorInterface.createStageFactor(4)


	sf1.setXFactor(1.1)
	sf1.setYFactor(1.2)

	sf2.setXFactor(1.3)
	sf2.setYFactor(1.4)

	sf3.setXFactor(1.5)
	sf3.setYFactor(1.6)

	sf4.setXFactor(1.7)
	sf4.setYFactor(1.8)

	pile1.ForceDisplacement.stageFactorInterface.setDefinedStageFactors({1:sf1,2:sf2,3:sf3,4:sf4})

test1()

model.save()

pass