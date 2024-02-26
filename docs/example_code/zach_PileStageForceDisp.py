from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\Pile\stageForceDisp_final.fez")

pileList = model.getAllPileProperties()
pile1 = pileList[0]

def test1():
	pile1.setStageForceDisplacement(True)
	sf_init = pile1.ForceDisplacement.stageFactorInterface.getDefinedStageFactors()
	sf2 = sf_init[1]
	sf4 = pile1.ForceDisplacement.stageFactorInterface.createStageFactor(4)

	sf2.setXFactor(1.1)
	sf2.setYFactor(1.2)

	sf4.setXFactor(1.3)
	sf4.setYFactor(1.4)

	pile1.ForceDisplacement.stageFactorInterface.setDefinedStageFactors({2:sf2,4:sf4})

	sf_dict = pile1.ForceDisplacement.stageFactorInterface.getDefinedStageFactors()

	sf1 = pile1.ForceDisplacement.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = pile1.ForceDisplacement.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getXFactor(),1)
	assert(sf1.getXFactor(),1)
	assert(sf2_fin.getXFactor(),1.1)
	assert(sf2_fin.getYFactor(), 1.2)
	assert(sf3.getXFactor(),1.1)
	assert(sf3.getYFactor(),1.2)
	assert(sf4_fin.getXFactor(),1.3)
	assert(sf4_fin.getYFactor(),1.4)

test1()

model.save()

pass