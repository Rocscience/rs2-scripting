from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Liner\linerStageFactors_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Liner\linerStageFactors_python.fez'

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

linerList = model.getAllLinerProperties()
liner1 = linerList[0]
liner2 = linerList[1]
liner3 = linerList[2]  
liner4 = linerList[3]
liner5 = linerList[4]
liner6 = linerList[5]
liner7 = linerList[6]
liner8 = linerList[7]
liner9 = linerList[8]
liner10 = linerList[9]
liner11 = linerList[10]
liner12 = linerList[11]
liner13 = linerList[12]
liner14 = linerList[13] 
liner15 = linerList[14]
liner16 = linerList[15]
liner17 = linerList[16]
liner18 = linerList[17]
liner19 = linerList[18]
liner20 = linerList[19]
liner21 = linerList[20]  
liner22 = linerList[21]

def test1():
	liner = liner1

	liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)
	liner.StandardBeam.setStageLinerProperties(True)

	liner.StandardBeam.setIncludeWeightInStressAnalysis(True)
	liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_AREA)
	liner.StandardBeam.setMaterialType(MaterialType.PLASTIC)
	liner.StandardBeam.setActivateThermal(True)
	liner.StandardBeam.setThermalExpansion(True)

	sf2 = liner.StandardBeam.stageFactorInterface.createStageFactor(2)
	sf4 = liner.StandardBeam.stageFactorInterface.createStageFactor(4)

	sf2.setAreaFactor(1.1)
	sf2.setMomentOfInertiaFactor(1.2)
	sf2.setYoungsModulusFactor(1.3)
	sf2.setPoissonsRatioFactor(1.4)
	sf2.setAxialStrainExpansionFactor(1.5)
	sf2.setCompressiveStrengthPeakFactor(1.6)
	sf2.setCompressiveStrengthResidualFactor(1.7)
	sf2.setTensileStrengthPeakFactor(1.8)
	sf2.setTensileStrengthResidualFactor(1.9)
	sf2.setUnitWeightFactor(1.11)
	sf2.setExpansionCoefficientFactor(1.12)
	sf2.setSpecificHeatCapacityFactor(1.13)

	sf4.setAreaFactor(1.14)
	sf4.setMomentOfInertiaFactor(1.15)
	sf4.setYoungsModulusFactor(1.16)
	sf4.setPoissonsRatioFactor(1.17)
	sf4.setAxialStrainExpansionFactor(1.18)
	sf4.setCompressiveStrengthPeakFactor(1.19)
	sf4.setCompressiveStrengthResidualFactor(1.21)
	sf4.setTensileStrengthPeakFactor(1.22)
	sf4.setTensileStrengthResidualFactor(1.23)
	sf4.setUnitWeightFactor(1.24)
	sf4.setExpansionCoefficientFactor(1.25)
	sf4.setSpecificHeatCapacityFactor(1.26)

	sf_dict = liner.StandardBeam.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.StandardBeam.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.StandardBeam.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getAreaFactor(), 1)
	assert(sf1.getMomentOfInertiaFactor(), 1)
	assert(sf1.getYoungsModulusFactor(), 1)
	assert(sf1.getPoissonsRatioFactor(), 1)
	assert(sf1.getAxialStrainExpansionFactor(), 1)
	assert(sf1.getCompressiveStrengthPeakFactor(), 1)
	assert(sf1.getCompressiveStrengthResidualFactor(), 1)
	assert(sf1.getTensileStrengthPeakFactor(), 1)
	assert(sf1.getTensileStrengthResidualFactor(), 1)
	assert(sf1.getUnitWeightFactor(), 1)
	assert(sf1.getExpansionCoefficientFactor(), 1)
	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getAreaFactor(), 1.1)
	assert(sf2_fin.getMomentOfInertiaFactor(), 1.2)
	assert(sf2_fin.getYoungsModulusFactor(), 1.3)
	assert(sf2_fin.getPoissonsRatioFactor(), 1.4)
	assert(sf2_fin.getAxialStrainExpansionFactor(), 1.5)
	assert(sf2_fin.getCompressiveStrengthPeakFactor(), 1.6)
	assert(sf2_fin.getCompressiveStrengthResidualFactor(), 1.7)
	assert(sf2_fin.getTensileStrengthPeakFactor(), 1.8)
	assert(sf2_fin.getTensileStrengthResidualFactor(), 1.9)
	assert(sf2_fin.getUnitWeightFactor(), 1.11)
	assert(sf2_fin.getExpansionCoefficientFactor(), 1.12)
	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.13)

	assert(sf3.getAreaFactor(), 1.1)
	assert(sf3.getMomentOfInertiaFactor(), 1.2)
	assert(sf3.getYoungsModulusFactor(), 1.3)
	assert(sf3.getPoissonsRatioFactor(), 1.4)
	assert(sf3.getAxialStrainExpansionFactor(), 1.5)
	assert(sf3.getCompressiveStrengthPeakFactor(), 1.6)
	assert(sf3.getCompressiveStrengthResidualFactor(), 1.7)
	assert(sf3.getTensileStrengthPeakFactor(), 1.8)
	assert(sf3.getTensileStrengthResidualFactor(), 1.9)
	assert(sf3.getUnitWeightFactor(), 1.11)
	assert(sf3.getExpansionCoefficientFactor(), 1.12)
	assert(sf3.getSpecificHeatCapacityFactor(), 1.13)

	assert(sf4_fin.getAreaFactor(), 1.14)
	assert(sf4_fin.getMomentOfInertiaFactor(), 1.15)
	assert(sf4_fin.getYoungsModulusFactor(), 1.16)
	assert(sf4_fin.getPoissonsRatioFactor(), 1.17)
	assert(sf4_fin.getAxialStrainExpansionFactor(), 1.18)
	assert(sf4_fin.getCompressiveStrengthPeakFactor(), 1.19)
	assert(sf4_fin.getCompressiveStrengthResidualFactor(), 1.21)
	assert(sf4_fin.getTensileStrengthPeakFactor(), 1.22)
	assert(sf4_fin.getTensileStrengthResidualFactor(), 1.23)
	assert(sf4_fin.getUnitWeightFactor(), 1.24)
	assert(sf4_fin.getExpansionCoefficientFactor(), 1.25)
	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.26)

def test2():
	liner = liner2

	liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)
	liner.StandardBeam.setStageLinerProperties(True)

	liner.StandardBeam.setIncludeWeightInStressAnalysis(True)
	liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_THICKNESS)
	liner.StandardBeam.setMaterialType(MaterialType.PLASTIC)
	liner.StandardBeam.setActivateThermal(True)
	liner.StandardBeam.setThermalExpansion(True)

	sf2 = liner.StandardBeam.stageFactorInterface.createStageFactor(2)
	sf4 = liner.StandardBeam.stageFactorInterface.createStageFactor(4)

	sf2.setThicknessFactor(1.1)
	sf2.setYoungsModulusFactor(1.3)
	sf2.setPoissonsRatioFactor(1.4)
	sf2.setAxialStrainExpansionFactor(1.5)
	sf2.setCompressiveStrengthPeakFactor(1.6)
	sf2.setCompressiveStrengthResidualFactor(1.7)
	sf2.setTensileStrengthPeakFactor(1.8)
	sf2.setTensileStrengthResidualFactor(1.9)
	sf2.setUnitWeightFactor(1.11)
	sf2.setExpansionCoefficientFactor(1.12)
	sf2.setSpecificHeatCapacityFactor(1.13)

	sf4.setThicknessFactor(1.14)
	sf4.setYoungsModulusFactor(1.16)
	sf4.setPoissonsRatioFactor(1.17)
	sf4.setAxialStrainExpansionFactor(1.18)
	sf4.setCompressiveStrengthPeakFactor(1.19)
	sf4.setCompressiveStrengthResidualFactor(1.21)
	sf4.setTensileStrengthPeakFactor(1.22)
	sf4.setTensileStrengthResidualFactor(1.23)
	sf4.setUnitWeightFactor(1.24)
	sf4.setExpansionCoefficientFactor(1.25)
	sf4.setSpecificHeatCapacityFactor(1.26)

	sf_dict = liner.StandardBeam.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.StandardBeam.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.StandardBeam.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getThicknessFactor(), 1)
	assert(sf1.getYoungsModulusFactor(), 1)
	assert(sf1.getPoissonsRatioFactor(), 1)
	assert(sf1.getAxialStrainExpansionFactor(), 1)
	assert(sf1.getCompressiveStrengthPeakFactor(), 1)
	assert(sf1.getCompressiveStrengthResidualFactor(), 1)
	assert(sf1.getTensileStrengthPeakFactor(), 1)
	assert(sf1.getTensileStrengthResidualFactor(), 1)
	assert(sf1.getUnitWeightFactor(), 1)
	assert(sf1.getExpansionCoefficientFactor(), 1)
	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getThicknessFactor(), 1.1)
	assert(sf2_fin.getYoungsModulusFactor(), 1.3)
	assert(sf2_fin.getPoissonsRatioFactor(), 1.4)
	assert(sf2_fin.getAxialStrainExpansionFactor(), 1.5)
	assert(sf2_fin.getCompressiveStrengthPeakFactor(), 1.6)
	assert(sf2_fin.getCompressiveStrengthResidualFactor(), 1.7)
	assert(sf2_fin.getTensileStrengthPeakFactor(), 1.8)
	assert(sf2_fin.getTensileStrengthResidualFactor(), 1.9)
	assert(sf2_fin.getUnitWeightFactor(), 1.11)
	assert(sf2_fin.getExpansionCoefficientFactor(), 1.12)
	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.13)

	assert(sf3.getThicknessFactor(), 1.1)
	assert(sf3.getYoungsModulusFactor(), 1.3)
	assert(sf3.getPoissonsRatioFactor(), 1.4)
	assert(sf3.getAxialStrainExpansionFactor(), 1.5)
	assert(sf3.getCompressiveStrengthPeakFactor(), 1.6)
	assert(sf3.getCompressiveStrengthResidualFactor(), 1.7)
	assert(sf3.getTensileStrengthPeakFactor(), 1.8)
	assert(sf3.getTensileStrengthResidualFactor(), 1.9)
	assert(sf3.getUnitWeightFactor(), 1.11)
	assert(sf3.getExpansionCoefficientFactor(), 1.12)
	assert(sf3.getSpecificHeatCapacityFactor(), 1.13)

	assert(sf4_fin.getThicknessFactor(), 1.14)
	assert(sf4_fin.getYoungsModulusFactor(), 1.16)
	assert(sf4_fin.getPoissonsRatioFactor(), 1.17)
	assert(sf4_fin.getAxialStrainExpansionFactor(), 1.18)
	assert(sf4_fin.getCompressiveStrengthPeakFactor(), 1.19)
	assert(sf4_fin.getCompressiveStrengthResidualFactor(), 1.21)
	assert(sf4_fin.getTensileStrengthPeakFactor(), 1.22)
	assert(sf4_fin.getTensileStrengthResidualFactor(), 1.23)
	assert(sf4_fin.getUnitWeightFactor(), 1.24)
	assert(sf4_fin.getExpansionCoefficientFactor(), 1.25)
	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.26)

def test3():
	liner = liner3

	liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)
	liner.StandardBeam.setStageLinerProperties(True)

	liner.StandardBeam.setIncludeWeightInStressAnalysis(True)
	liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_AREA)
	liner.StandardBeam.setMaterialType(MaterialType.ELASTIC)
	liner.StandardBeam.setActivateThermal(True)
	liner.StandardBeam.setThermalExpansion(True)

	sf2 = liner.StandardBeam.stageFactorInterface.createStageFactor(2)
	sf4 = liner.StandardBeam.stageFactorInterface.createStageFactor(4)

	sf2.setUnitWeightFactor(1.11)
	sf2.setExpansionCoefficientFactor(1.12)
	sf2.setSpecificHeatCapacityFactor(1.13)

	sf4.setUnitWeightFactor(1.24)
	sf4.setExpansionCoefficientFactor(1.25)
	sf4.setSpecificHeatCapacityFactor(1.26)

	sf_dict = liner.StandardBeam.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.StandardBeam.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.StandardBeam.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getUnitWeightFactor(), 1)
	assert(sf1.getExpansionCoefficientFactor(), 1)
	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getUnitWeightFactor(), 1.11)
	assert(sf2_fin.getExpansionCoefficientFactor(), 1.12)
	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.13)

	assert(sf3.getUnitWeightFactor(), 1.11)
	assert(sf3.getExpansionCoefficientFactor(), 1.12)
	assert(sf3.getSpecificHeatCapacityFactor(), 1.13)

	assert(sf4_fin.getUnitWeightFactor(), 1.24)
	assert(sf4_fin.getExpansionCoefficientFactor(), 1.25)
	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.26)

def test4():
	liner = liner4

	liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)
	liner.StandardBeam.setStageLinerProperties(True)

	liner.StandardBeam.setIncludeWeightInStressAnalysis(True)
	liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_THICKNESS)
	liner.StandardBeam.setMaterialType(MaterialType.ELASTIC)
	liner.StandardBeam.setActivateThermal(True)
	liner.StandardBeam.setThermalExpansion(True)

	sf2 = liner.StandardBeam.stageFactorInterface.createStageFactor(2)
	sf4 = liner.StandardBeam.stageFactorInterface.createStageFactor(4)

	sf2.setUnitWeightFactor(1.11)
	sf2.setExpansionCoefficientFactor(1.12)
	sf2.setSpecificHeatCapacityFactor(1.13)

	sf4.setUnitWeightFactor(1.24)
	sf4.setExpansionCoefficientFactor(1.25)
	sf4.setSpecificHeatCapacityFactor(1.26)

	sf_dict = liner.StandardBeam.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.StandardBeam.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.StandardBeam.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getUnitWeightFactor(), 1)
	assert(sf1.getExpansionCoefficientFactor(), 1)
	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getUnitWeightFactor(), 1.11)
	assert(sf2_fin.getExpansionCoefficientFactor(), 1.12)
	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.13)

	assert(sf3.getUnitWeightFactor(), 1.11)
	assert(sf3.getExpansionCoefficientFactor(), 1.12)
	assert(sf3.getSpecificHeatCapacityFactor(), 1.13)

	assert(sf4_fin.getUnitWeightFactor(), 1.24)
	assert(sf4_fin.getExpansionCoefficientFactor(), 1.25)
	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.26)

def test5():
	liner = liner5

	liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)
	liner.StandardBeam.setStageLinerProperties(True)

	liner.StandardBeam.setIncludeWeightInStressAnalysis(True)
	liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_AREA)
	liner.StandardBeam.setMaterialType(MaterialType.PLASTIC)
	liner.StandardBeam.setActivateThermal(True)
	liner.StandardBeam.setThermalExpansion(True)

	sf2 = liner.StandardBeam.stageFactorInterface.createStageFactor(2)
	sf4 = liner.StandardBeam.stageFactorInterface.createStageFactor(4)

	sf2.setAreaFactor(1.1)
	sf2.setMomentOfInertiaFactor(1.2)
	sf2.setYoungsModulusFactor(1.3)
	sf2.setPoissonsRatioFactor(1.4)
	sf2.setAxialStrainExpansionFactor(1.5)
	sf2.setCompressiveStrengthPeakFactor(1.6)
	sf2.setCompressiveStrengthResidualFactor(1.7)
	sf2.setTensileStrengthPeakFactor(1.8)
	sf2.setTensileStrengthResidualFactor(1.9)
	sf2.setUnitWeightFactor(1.11)
	sf2.setExpansionCoefficientFactor(1.12)
	sf2.setSpecificHeatCapacityFactor(1.13)

	sf4.setAreaFactor(1.14)
	sf4.setMomentOfInertiaFactor(1.15)
	sf4.setYoungsModulusFactor(1.16)
	sf4.setPoissonsRatioFactor(1.17)
	sf4.setAxialStrainExpansionFactor(1.18)
	sf4.setCompressiveStrengthPeakFactor(1.19)
	sf4.setCompressiveStrengthResidualFactor(1.21)
	sf4.setTensileStrengthPeakFactor(1.22)
	sf4.setTensileStrengthResidualFactor(1.23)
	sf4.setUnitWeightFactor(1.24)
	sf4.setExpansionCoefficientFactor(1.25)
	sf4.setSpecificHeatCapacityFactor(1.26)

	liner.StandardBeam.stageFactorInterface.setDefinedStageFactors(StageFactorDefinitionMethod.RELATIVE_STAGE_FACTOR, {2:sf2,4:sf4})

	sf_dict = liner.StandardBeam.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.StandardBeam.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.StandardBeam.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getAreaFactor(), 1)
	assert(sf1.getMomentOfInertiaFactor(), 1)
	assert(sf1.getYoungsModulusFactor(), 1)
	assert(sf1.getPoissonsRatioFactor(), 1)
	assert(sf1.getAxialStrainExpansionFactor(), 1)
	assert(sf1.getCompressiveStrengthPeakFactor(), 1)
	assert(sf1.getCompressiveStrengthResidualFactor(), 1)
	assert(sf1.getTensileStrengthPeakFactor(), 1)
	assert(sf1.getTensileStrengthResidualFactor(), 1)
	assert(sf1.getUnitWeightFactor(), 1)
	assert(sf1.getExpansionCoefficientFactor(), 1)
	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getAreaFactor(), 1.1)
	assert(sf2_fin.getMomentOfInertiaFactor(), 1.2)
	assert(sf2_fin.getYoungsModulusFactor(), 1.3)
	assert(sf2_fin.getPoissonsRatioFactor(), 1.4)
	assert(sf2_fin.getAxialStrainExpansionFactor(), 1.5)
	assert(sf2_fin.getCompressiveStrengthPeakFactor(), 1.6)
	assert(sf2_fin.getCompressiveStrengthResidualFactor(), 1.7)
	assert(sf2_fin.getTensileStrengthPeakFactor(), 1.8)
	assert(sf2_fin.getTensileStrengthResidualFactor(), 1.9)
	assert(sf2_fin.getUnitWeightFactor(), 1.11)
	assert(sf2_fin.getExpansionCoefficientFactor(), 1.12)
	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.13)

	assert(sf3.getAreaFactor(), 1.1)
	assert(sf3.getMomentOfInertiaFactor(), 1.2)
	assert(sf3.getYoungsModulusFactor(), 1.3)
	assert(sf3.getPoissonsRatioFactor(), 1.4)
	assert(sf3.getAxialStrainExpansionFactor(), 1.5)
	assert(sf3.getCompressiveStrengthPeakFactor(), 1.6)
	assert(sf3.getCompressiveStrengthResidualFactor(), 1.7)
	assert(sf3.getTensileStrengthPeakFactor(), 1.8)
	assert(sf3.getTensileStrengthResidualFactor(), 1.9)
	assert(sf3.getUnitWeightFactor(), 1.11)
	assert(sf3.getExpansionCoefficientFactor(), 1.12)
	assert(sf3.getSpecificHeatCapacityFactor(), 1.13)

	assert(sf4_fin.getAreaFactor(), 1.14)
	assert(sf4_fin.getMomentOfInertiaFactor(), 1.15)
	assert(sf4_fin.getYoungsModulusFactor(), 1.16)
	assert(sf4_fin.getPoissonsRatioFactor(), 1.17)
	assert(sf4_fin.getAxialStrainExpansionFactor(), 1.18)
	assert(sf4_fin.getCompressiveStrengthPeakFactor(), 1.19)
	assert(sf4_fin.getCompressiveStrengthResidualFactor(), 1.21)
	assert(sf4_fin.getTensileStrengthPeakFactor(), 1.22)
	assert(sf4_fin.getTensileStrengthResidualFactor(), 1.23)
	assert(sf4_fin.getUnitWeightFactor(), 1.24)
	assert(sf4_fin.getExpansionCoefficientFactor(), 1.25)
	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.26)

def test6():
	liner = liner6

	liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)
	liner.Geosynthetic.setStageGeosyntheticProperties(True)

	liner.Geosynthetic.setMaterialType(MaterialType.PLASTIC)
	liner.Geosynthetic.setActivateThermal(True)
	liner.Geosynthetic.setThermalExpansion(True)

	sf2 = liner.Geosynthetic.stageFactorInterface.createStageFactor(2)
	sf4 = liner.Geosynthetic.stageFactorInterface.createStageFactor(4)

	sf2.setTensileModulusFactor(1.1)
	sf2.setAxialStrainExpansionFactor(1.2)
	sf2.setTensileStrengthPeakFactor(1.3)
	sf2.setTensileStrengthResidualFactor(1.4)
	sf2.setGeosyntheticUnitWeightFactor(1.5)
	sf2.setExpansionCoefficientFactor(1.6)
	sf2.setSpecificHeatCapacityFactor(1.7)

	sf4.setTensileModulusFactor(1.8)
	sf4.setAxialStrainExpansionFactor(1.9)
	sf4.setTensileStrengthPeakFactor(1.11)
	sf4.setTensileStrengthResidualFactor(1.12)
	sf4.setGeosyntheticUnitWeightFactor(1.13)
	sf4.setExpansionCoefficientFactor(1.14)
	sf4.setSpecificHeatCapacityFactor(1.15)	

	sf_dict = liner.Geosynthetic.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.Geosynthetic.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.Geosynthetic.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getTensileModulusFactor(), 1)
	assert(sf1.getAxialStrainExpansionFactor(), 1)
	assert(sf1.getTensileStrengthPeakFactor(), 1)
	assert(sf1.getTensileStrengthResidualFactor(), 1)
	assert(sf1.getGeosyntheticUnitWeightFactor(), 1)
	assert(sf1.getExpansionCoefficientFactor(), 1)
	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getTensileModulusFactor(), 1.1)
	assert(sf2_fin.getAxialStrainExpansionFactor(), 1.2)
	assert(sf2_fin.getTensileStrengthPeakFactor(), 1.3)
	assert(sf2_fin.getTensileStrengthResidualFactor(), 1.4)
	assert(sf2_fin.getGeosyntheticUnitWeightFactor(), 1.5)
	assert(sf2_fin.getExpansionCoefficientFactor(), 1.6)
	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.7)

	assert(sf3.getTensileModulusFactor(), 1.1)
	assert(sf3.getAxialStrainExpansionFactor(), 1.2)
	assert(sf3.getTensileStrengthPeakFactor(), 1.3)
	assert(sf3.getTensileStrengthResidualFactor(), 1.4)
	assert(sf3.getGeosyntheticUnitWeightFactor(), 1.5)
	assert(sf3.getExpansionCoefficientFactor(), 1.6)
	assert(sf3.getSpecificHeatCapacityFactor(), 1.7)

	assert(sf4_fin.getTensileModulusFactor(), 1.8)
	assert(sf4_fin.getAxialStrainExpansionFactor(), 1.9)
	assert(sf4_fin.getTensileStrengthPeakFactor(), 1.11)
	assert(sf4_fin.getTensileStrengthResidualFactor(), 1.12)
	assert(sf4_fin.getGeosyntheticUnitWeightFactor(), 1.13)
	assert(sf4_fin.getExpansionCoefficientFactor(), 1.14)
	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.15)

def test7():
	liner = liner7

	liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)
	liner.Geosynthetic.setStageGeosyntheticProperties(True)

	liner.Geosynthetic.setMaterialType(MaterialType.ELASTIC)
	liner.Geosynthetic.setActivateThermal(True)
	liner.Geosynthetic.setThermalExpansion(True)

	sf2 = liner.Geosynthetic.stageFactorInterface.createStageFactor(2)
	sf4 = liner.Geosynthetic.stageFactorInterface.createStageFactor(4)

	sf2.setGeosyntheticUnitWeightFactor(1.5)
	sf2.setExpansionCoefficientFactor(1.6)
	sf2.setSpecificHeatCapacityFactor(1.7)

	sf4.setGeosyntheticUnitWeightFactor(1.13)
	sf4.setExpansionCoefficientFactor(1.14)
	sf4.setSpecificHeatCapacityFactor(1.15)	

	sf_dict = liner.Geosynthetic.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.Geosynthetic.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.Geosynthetic.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getGeosyntheticUnitWeightFactor(), 1)
	assert(sf1.getExpansionCoefficientFactor(), 1)
	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getGeosyntheticUnitWeightFactor(), 1.5)
	assert(sf2_fin.getExpansionCoefficientFactor(), 1.6)
	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.7)

	assert(sf3.getGeosyntheticUnitWeightFactor(), 1.5)
	assert(sf3.getExpansionCoefficientFactor(), 1.6)
	assert(sf3.getSpecificHeatCapacityFactor(), 1.7)

	assert(sf4_fin.getGeosyntheticUnitWeightFactor(), 1.13)
	assert(sf4_fin.getExpansionCoefficientFactor(), 1.14)
	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.15)

def test8():
	liner = liner8

	liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)
	liner.Geosynthetic.setStageGeosyntheticProperties(True)

	liner.Geosynthetic.setMaterialType(MaterialType.PLASTIC)
	liner.Geosynthetic.setActivateThermal(True)
	liner.Geosynthetic.setThermalExpansion(False)

	sf2 = liner.Geosynthetic.stageFactorInterface.createStageFactor(2)
	sf4 = liner.Geosynthetic.stageFactorInterface.createStageFactor(4)

	sf2.setSpecificHeatCapacityFactor(1.7)

	sf4.setSpecificHeatCapacityFactor(1.15)	

	sf_dict = liner.Geosynthetic.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.Geosynthetic.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.Geosynthetic.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.7)

	assert(sf3.getSpecificHeatCapacityFactor(), 1.7)

	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.15)

def test9():
	liner = liner9

	liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)
	liner.Geosynthetic.setStageGeosyntheticProperties(True)

	liner.Geosynthetic.setMaterialType(MaterialType.ELASTIC)
	liner.Geosynthetic.setActivateThermal(True)
	liner.Geosynthetic.setThermalExpansion(False)

	sf2 = liner.Geosynthetic.stageFactorInterface.createStageFactor(2)
	sf4 = liner.Geosynthetic.stageFactorInterface.createStageFactor(4)

	sf2.setSpecificHeatCapacityFactor(1.7)

	sf4.setSpecificHeatCapacityFactor(1.15)	

	sf_dict = liner.Geosynthetic.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.Geosynthetic.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.Geosynthetic.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.7)

	assert(sf3.getSpecificHeatCapacityFactor(), 1.7)

	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.15)

def test10():
	liner = liner10

	liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)
	liner.Geosynthetic.setStageGeosyntheticProperties(True)

	liner.Geosynthetic.setMaterialType(MaterialType.PLASTIC)
	liner.Geosynthetic.setActivateThermal(True)
	liner.Geosynthetic.setThermalExpansion(True)

	sf2 = liner.Geosynthetic.stageFactorInterface.createStageFactor(2)
	sf4 = liner.Geosynthetic.stageFactorInterface.createStageFactor(4)

	sf2.setTensileModulusFactor(1.1)
	sf2.setAxialStrainExpansionFactor(1.2)
	sf2.setTensileStrengthPeakFactor(1.3)
	sf2.setTensileStrengthResidualFactor(1.4)
	sf2.setGeosyntheticUnitWeightFactor(1.5)
	sf2.setExpansionCoefficientFactor(1.6)
	sf2.setSpecificHeatCapacityFactor(1.7)

	sf4.setTensileModulusFactor(1.8)
	sf4.setAxialStrainExpansionFactor(1.9)
	sf4.setTensileStrengthPeakFactor(1.11)
	sf4.setTensileStrengthResidualFactor(1.12)
	sf4.setGeosyntheticUnitWeightFactor(1.13)
	sf4.setExpansionCoefficientFactor(1.14)
	sf4.setSpecificHeatCapacityFactor(1.15)	

	liner.Geosynthetic.stageFactorInterface.setDefinedStageFactors(StageFactorDefinitionMethod.RELATIVE_STAGE_FACTOR, {2:sf2,4:sf4})

	sf_dict = liner.Geosynthetic.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.Geosynthetic.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.Geosynthetic.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getTensileModulusFactor(), 1)
	assert(sf1.getAxialStrainExpansionFactor(), 1)
	assert(sf1.getTensileStrengthPeakFactor(), 1)
	assert(sf1.getTensileStrengthResidualFactor(), 1)
	assert(sf1.getGeosyntheticUnitWeightFactor(), 1)
	assert(sf1.getExpansionCoefficientFactor(), 1)
	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getTensileModulusFactor(), 1.1)
	assert(sf2_fin.getAxialStrainExpansionFactor(), 1.2)
	assert(sf2_fin.getTensileStrengthPeakFactor(), 1.3)
	assert(sf2_fin.getTensileStrengthResidualFactor(), 1.4)
	assert(sf2_fin.getGeosyntheticUnitWeightFactor(), 1.5)
	assert(sf2_fin.getExpansionCoefficientFactor(), 1.6)
	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.7)

	assert(sf3.getTensileModulusFactor(), 1.1)
	assert(sf3.getAxialStrainExpansionFactor(), 1.2)
	assert(sf3.getTensileStrengthPeakFactor(), 1.3)
	assert(sf3.getTensileStrengthResidualFactor(), 1.4)
	assert(sf3.getGeosyntheticUnitWeightFactor(), 1.5)
	assert(sf3.getExpansionCoefficientFactor(), 1.6)
	assert(sf3.getSpecificHeatCapacityFactor(), 1.7)

	assert(sf4_fin.getTensileModulusFactor(), 1.8)
	assert(sf4_fin.getAxialStrainExpansionFactor(), 1.9)
	assert(sf4_fin.getTensileStrengthPeakFactor(), 1.11)
	assert(sf4_fin.getTensileStrengthResidualFactor(), 1.12)
	assert(sf4_fin.getGeosyntheticUnitWeightFactor(), 1.13)
	assert(sf4_fin.getExpansionCoefficientFactor(), 1.14)
	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.15)

def test11():
	liner = liner11

	liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)
	liner.ReinforcedConcrete.setStageConcreteProperties(True)

	liner.ReinforcedConcrete.setIncludeWeightInStressAnalysis(True)
	liner.ReinforcedConcrete.setReinforcement(True)
	liner.ReinforcedConcrete.setActivateThermal(True)
	liner.ReinforcedConcrete.setThermalExpansion(True)

	sf2 = liner.ReinforcedConcrete.stageFactorInterface.createStageFactor(2)
	sf4 = liner.ReinforcedConcrete.stageFactorInterface.createStageFactor(4)

	sf2.setThicknessFactor(1.1)
	sf2.setYoungsModulusFactor(1.2)
	sf2.setCompressiveStrengthFactor(1.3)
	sf2.setTensileStrengthFactor(1.4)
	sf2.setAxialStrainExpansionFactor(1.5)
	sf2.setConcreteUnitWeightFactor(1.6)
	sf2.setWeightFactor(1.7)
	sf2.setAreaFactor(1.8)
	sf2.setExpansionCoefficientFactor(1.9)
	sf2.setSpecificHeatCapacityFactor(1.11)

	sf4.setThicknessFactor(1.12)
	sf4.setYoungsModulusFactor(1.13)
	sf4.setCompressiveStrengthFactor(1.14)
	sf4.setTensileStrengthFactor(1.15)
	sf4.setAxialStrainExpansionFactor(1.16)
	sf4.setConcreteUnitWeightFactor(1.17)
	sf4.setWeightFactor(1.18)
	sf4.setAreaFactor(1.19)
	sf4.setExpansionCoefficientFactor(1.21)
	sf4.setSpecificHeatCapacityFactor(1.22)

	sf_dict = liner.ReinforcedConcrete.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.ReinforcedConcrete.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.ReinforcedConcrete.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getThicknessFactor(),1)
	assert(sf1.getYoungsModulusFactor(), 1)
	assert(sf1.getCompressiveStrengthFactor(), 1)
	assert(sf1.getTensileStrengthFactor(), 1)
	assert(sf1.getAxialStrainExpansionFactor(), 1)
	assert(sf1.getConcreteUnitWeightFactor(), 1)
	assert(sf1.getWeightFactor(), 1)
	assert(sf1.getAreaFactor(), 1)
	assert(sf1.getExpansionCoefficientFactor(), 1)
	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getThicknessFactor(),1.1)
	assert(sf2_fin.getYoungsModulusFactor(), 1.2)
	assert(sf2_fin.getCompressiveStrengthFactor(), 1.3)
	assert(sf2_fin.getTensileStrengthFactor(), 1.4)
	assert(sf2_fin.getAxialStrainExpansionFactor(), 1.5)
	assert(sf2_fin.getConcreteUnitWeightFactor(), 1.6)
	assert(sf2_fin.getWeightFactor(), 1.7)
	assert(sf2_fin.getAreaFactor(), 1.8)
	assert(sf2_fin.getExpansionCoefficientFactor(), 1.9)
	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.11)

	assert(sf3.getThicknessFactor(),1.1)
	assert(sf3.getYoungsModulusFactor(), 1.2)
	assert(sf3.getCompressiveStrengthFactor(), 1.3)
	assert(sf3.getTensileStrengthFactor(), 1.4)
	assert(sf3.getAxialStrainExpansionFactor(), 1.5)
	assert(sf3.getConcreteUnitWeightFactor(), 1.6)
	assert(sf3.getWeightFactor(), 1.7)
	assert(sf3.getAreaFactor(), 1.8)
	assert(sf3.getExpansionCoefficientFactor(), 1.9)
	assert(sf3.getSpecificHeatCapacityFactor(), 1.11)

	assert(sf4_fin.getThicknessFactor(),1.12)
	assert(sf4_fin.getYoungsModulusFactor(), 1.13)
	assert(sf4_fin.getCompressiveStrengthFactor(), 1.14)
	assert(sf4_fin.getTensileStrengthFactor(), 1.15)
	assert(sf4_fin.getAxialStrainExpansionFactor(), 1.16)
	assert(sf4_fin.getConcreteUnitWeightFactor(), 1.17)
	assert(sf4_fin.getWeightFactor(), 1.18)
	assert(sf4_fin.getAreaFactor(), 1.19)
	assert(sf4_fin.getExpansionCoefficientFactor(), 1.21)
	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.22)

def test12():
	liner = liner12

	liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)
	liner.ReinforcedConcrete.setStageConcreteProperties(True)

	liner.ReinforcedConcrete.setIncludeWeightInStressAnalysis(True)
	liner.ReinforcedConcrete.setReinforcement(False)
	liner.ReinforcedConcrete.setActivateThermal(True)
	liner.ReinforcedConcrete.setThermalExpansion(True)

	sf2 = liner.ReinforcedConcrete.stageFactorInterface.createStageFactor(2)
	sf4 = liner.ReinforcedConcrete.stageFactorInterface.createStageFactor(4)

	sf2.setExpansionCoefficientFactor(1.9)
	sf2.setSpecificHeatCapacityFactor(1.11)

	sf4.setExpansionCoefficientFactor(1.21)
	sf4.setSpecificHeatCapacityFactor(1.22)

	sf_dict = liner.ReinforcedConcrete.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.ReinforcedConcrete.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.ReinforcedConcrete.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getExpansionCoefficientFactor(), 1)
	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getExpansionCoefficientFactor(), 1.9)
	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.11)

	assert(sf3.getExpansionCoefficientFactor(), 1.9)
	assert(sf3.getSpecificHeatCapacityFactor(), 1.11)

	assert(sf4_fin.getExpansionCoefficientFactor(), 1.21)
	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.22)

def test13():
	liner = liner13

	liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)
	liner.ReinforcedConcrete.setStageConcreteProperties(True)

	liner.ReinforcedConcrete.setIncludeWeightInStressAnalysis(False)
	liner.ReinforcedConcrete.setReinforcement(True)
	liner.ReinforcedConcrete.setActivateThermal(False)

	sf2 = liner.ReinforcedConcrete.stageFactorInterface.createStageFactor(2)
	sf4 = liner.ReinforcedConcrete.stageFactorInterface.createStageFactor(4)

	sf2.setAreaFactor(1.8)

	sf4.setAreaFactor(1.19)
	
	sf_dict = liner.ReinforcedConcrete.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.ReinforcedConcrete.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.ReinforcedConcrete.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getAreaFactor(), 1)

	assert(sf2_fin.getAreaFactor(), 1.8)

	assert(sf3.getAreaFactor(), 1.8)

	assert(sf4_fin.getAreaFactor(), 1.19)

def test14():
	liner = liner14

	liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)
	liner.ReinforcedConcrete.setStageConcreteProperties(True)

	liner.ReinforcedConcrete.setIncludeWeightInStressAnalysis(True)
	liner.ReinforcedConcrete.setReinforcement(False)
	liner.ReinforcedConcrete.setActivateThermal(True)
	liner.ReinforcedConcrete.setThermalExpansion(False)

	sf2 = liner.ReinforcedConcrete.stageFactorInterface.createStageFactor(2)
	sf4 = liner.ReinforcedConcrete.stageFactorInterface.createStageFactor(4)

	sf2.setSpecificHeatCapacityFactor(1.11)

	sf4.setSpecificHeatCapacityFactor(1.22)

	sf_dict = liner.ReinforcedConcrete.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.ReinforcedConcrete.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.ReinforcedConcrete.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.11)

	assert(sf3.getSpecificHeatCapacityFactor(), 1.11)

	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.22)

def test15():
	liner = liner15

	liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)
	liner.ReinforcedConcrete.setStageConcreteProperties(True)

	liner.ReinforcedConcrete.setIncludeWeightInStressAnalysis(True)
	liner.ReinforcedConcrete.setReinforcement(True)
	liner.ReinforcedConcrete.setActivateThermal(True)
	liner.ReinforcedConcrete.setThermalExpansion(True)

	sf2 = liner.ReinforcedConcrete.stageFactorInterface.createStageFactor(2)
	sf4 = liner.ReinforcedConcrete.stageFactorInterface.createStageFactor(4)

	sf2.setThicknessFactor(1.1)
	sf2.setYoungsModulusFactor(1.2)
	sf2.setCompressiveStrengthFactor(1.3)
	sf2.setTensileStrengthFactor(1.4)
	sf2.setAxialStrainExpansionFactor(1.5)
	sf2.setConcreteUnitWeightFactor(1.6)
	sf2.setWeightFactor(1.7)
	sf2.setAreaFactor(1.8)
	sf2.setExpansionCoefficientFactor(1.9)
	sf2.setSpecificHeatCapacityFactor(1.11)

	sf4.setThicknessFactor(1.12)
	sf4.setYoungsModulusFactor(1.13)
	sf4.setCompressiveStrengthFactor(1.14)
	sf4.setTensileStrengthFactor(1.15)
	sf4.setAxialStrainExpansionFactor(1.16)
	sf4.setConcreteUnitWeightFactor(1.17)
	sf4.setWeightFactor(1.18)
	sf4.setAreaFactor(1.19)
	sf4.setExpansionCoefficientFactor(1.21)
	sf4.setSpecificHeatCapacityFactor(1.22)

	liner.ReinforcedConcrete.stageFactorInterface.setDefinedStageFactors(StageFactorDefinitionMethod.RELATIVE_STAGE_FACTOR, {2:sf2,4:sf4})

	sf_dict = liner.ReinforcedConcrete.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.ReinforcedConcrete.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.ReinforcedConcrete.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getThicknessFactor(),1)
	assert(sf1.getYoungsModulusFactor(), 1)
	assert(sf1.getCompressiveStrengthFactor(), 1)
	assert(sf1.getTensileStrengthFactor(), 1)
	assert(sf1.getAxialStrainExpansionFactor(), 1)
	assert(sf1.getConcreteUnitWeightFactor(), 1)
	assert(sf1.getWeightFactor(), 1)
	assert(sf1.getAreaFactor(), 1)
	assert(sf1.getExpansionCoefficientFactor(), 1)
	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getThicknessFactor(),1.1)
	assert(sf2_fin.getYoungsModulusFactor(), 1.2)
	assert(sf2_fin.getCompressiveStrengthFactor(), 1.3)
	assert(sf2_fin.getTensileStrengthFactor(), 1.4)
	assert(sf2_fin.getAxialStrainExpansionFactor(), 1.5)
	assert(sf2_fin.getConcreteUnitWeightFactor(), 1.6)
	assert(sf2_fin.getWeightFactor(), 1.7)
	assert(sf2_fin.getAreaFactor(), 1.8)
	assert(sf2_fin.getExpansionCoefficientFactor(), 1.9)
	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.11)

	assert(sf3.getThicknessFactor(),1.1)
	assert(sf3.getYoungsModulusFactor(), 1.2)
	assert(sf3.getCompressiveStrengthFactor(), 1.3)
	assert(sf3.getTensileStrengthFactor(), 1.4)
	assert(sf3.getAxialStrainExpansionFactor(), 1.5)
	assert(sf3.getConcreteUnitWeightFactor(), 1.6)
	assert(sf3.getWeightFactor(), 1.7)
	assert(sf3.getAreaFactor(), 1.8)
	assert(sf3.getExpansionCoefficientFactor(), 1.9)
	assert(sf3.getSpecificHeatCapacityFactor(), 1.11)

	assert(sf4_fin.getThicknessFactor(),1.12)
	assert(sf4_fin.getYoungsModulusFactor(), 1.13)
	assert(sf4_fin.getCompressiveStrengthFactor(), 1.14)
	assert(sf4_fin.getTensileStrengthFactor(), 1.15)
	assert(sf4_fin.getAxialStrainExpansionFactor(), 1.16)
	assert(sf4_fin.getConcreteUnitWeightFactor(), 1.17)
	assert(sf4_fin.getWeightFactor(), 1.18)
	assert(sf4_fin.getAreaFactor(), 1.19)
	assert(sf4_fin.getExpansionCoefficientFactor(), 1.21)
	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.22)

def test16():
	liner = liner16

	liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)
	liner.CableTruss.setStageCableProperties(True)

	liner.CableTruss.setMaterialType(MaterialType.PLASTIC)
	liner.CableTruss.setActivateThermal(True)
	liner.CableTruss.setThermalExpansion(True)

	sf2 = liner.CableTruss.stageFactorInterface.createStageFactor(2)
	sf4 = liner.CableTruss.stageFactorInterface.createStageFactor(4)

	sf2.setYoungsModulusFactor(1.1)
	sf2.setAxialStrainExpansionFactor(1.2)
	sf2.setTensileStrengthPeakFactor(1.3)
	sf2.setTensileStrengthResidualFactor(1.4)
	sf2.setUnitWeightFactor(1.5)
	sf2.setCableDiameterFactor(1.6)
	sf2.setExpansionCoefficientFactor(1.7)
	sf2.setSpecificHeatCapacityFactor(1.8)

	sf4.setYoungsModulusFactor(1.9)
	sf4.setAxialStrainExpansionFactor(1.11)
	sf4.setTensileStrengthPeakFactor(1.12)
	sf4.setTensileStrengthResidualFactor(1.13)
	sf4.setUnitWeightFactor(1.14)
	sf4.setCableDiameterFactor(1.15)
	sf4.setExpansionCoefficientFactor(1.16)
	sf4.setSpecificHeatCapacityFactor(1.17)

	sf_dict = liner.CableTruss.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.CableTruss.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.CableTruss.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getYoungsModulusFactor(), 1)
	assert(sf1.getAxialStrainExpansionFactor(), 1) 
	assert(sf1.getTensileStrengthPeakFactor(), 1)
	assert(sf1.getTensileStrengthResidualFactor(), 1)
	assert(sf1.getUnitWeightFactor(), 1)
	assert(sf1.getCableDiameterFactor(), 1)
	assert(sf1.getExpansionCoefficientFactor(), 1)
	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getYoungsModulusFactor(), 1.1)
	assert(sf2_fin.getAxialStrainExpansionFactor(), 1.2)
	assert(sf2_fin.getTensileStrengthPeakFactor(), 1.3)
	assert(sf2_fin.getTensileStrengthResidualFactor(), 1.4)
	assert(sf2_fin.getUnitWeightFactor(), 1.5)
	assert(sf2_fin.getCableDiameterFactor(), 1.6)
	assert(sf2_fin.getExpansionCoefficientFactor(), 1.7)
	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.8)

	assert(sf3.getYoungsModulusFactor(), 1.1)
	assert(sf3.getAxialStrainExpansionFactor(), 1.2)
	assert(sf3.getTensileStrengthPeakFactor(), 1.3)
	assert(sf3.getTensileStrengthResidualFactor(), 1.4)
	assert(sf3.getUnitWeightFactor(), 1.5)
	assert(sf3.getCableDiameterFactor(), 1.6)
	assert(sf3.getExpansionCoefficientFactor(), 1.7)
	assert(sf3.getSpecificHeatCapacityFactor(), 1.8)

	assert(sf4_fin.getYoungsModulusFactor(), 1.9)
	assert(sf4_fin.getAxialStrainExpansionFactor(), 1.11)
	assert(sf4_fin.getTensileStrengthPeakFactor(), 1.12)
	assert(sf4_fin.getTensileStrengthResidualFactor(), 1.13)
	assert(sf4_fin.getUnitWeightFactor(), 1.14)
	assert(sf4_fin.getCableDiameterFactor(), 1.15)  
	assert(sf4_fin.getExpansionCoefficientFactor(), 1.16)
	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.17)

def test17():
	liner = liner17

	liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)
	liner.CableTruss.setStageCableProperties(True)

	liner.CableTruss.setMaterialType(MaterialType.ELASTIC)
	liner.CableTruss.setActivateThermal(True)
	liner.CableTruss.setThermalExpansion(True)

	sf2 = liner.CableTruss.stageFactorInterface.createStageFactor(2)
	sf4 = liner.CableTruss.stageFactorInterface.createStageFactor(4)

	sf2.setUnitWeightFactor(1.5)
	sf2.setCableDiameterFactor(1.6)
	sf2.setExpansionCoefficientFactor(1.7)
	sf2.setSpecificHeatCapacityFactor(1.8)

	sf4.setUnitWeightFactor(1.14)
	sf4.setCableDiameterFactor(1.15)
	sf4.setExpansionCoefficientFactor(1.16)
	sf4.setSpecificHeatCapacityFactor(1.17)

	sf_dict = liner.CableTruss.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.CableTruss.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.CableTruss.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getUnitWeightFactor(), 1)
	assert(sf1.getCableDiameterFactor(), 1)
	assert(sf1.getExpansionCoefficientFactor(), 1)
	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getUnitWeightFactor(), 1.5)
	assert(sf2_fin.getCableDiameterFactor(), 1.6)
	assert(sf2_fin.getExpansionCoefficientFactor(), 1.7)
	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.8)

	assert(sf3.getUnitWeightFactor(), 1.5)
	assert(sf3.getCableDiameterFactor(), 1.6)
	assert(sf3.getExpansionCoefficientFactor(), 1.7)
	assert(sf3.getSpecificHeatCapacityFactor(), 1.8)

	assert(sf4_fin.getUnitWeightFactor(), 1.14)
	assert(sf4_fin.getCableDiameterFactor(), 1.15)  
	assert(sf4_fin.getExpansionCoefficientFactor(), 1.16)
	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.17)

def test18():
	liner = liner18

	liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)
	liner.CableTruss.setStageCableProperties(True)

	liner.CableTruss.setMaterialType(MaterialType.PLASTIC)
	liner.CableTruss.setActivateThermal(False)

	sf2 = liner.CableTruss.stageFactorInterface.createStageFactor(2)
	sf4 = liner.CableTruss.stageFactorInterface.createStageFactor(4)

	sf2.setCableDiameterFactor(1.6)

	sf4.setCableDiameterFactor(1.15)

	sf_dict = liner.CableTruss.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.CableTruss.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.CableTruss.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getCableDiameterFactor(), 1)

	assert(sf2_fin.getCableDiameterFactor(), 1.6)

	assert(sf3.getCableDiameterFactor(), 1.6)

	assert(sf4_fin.getCableDiameterFactor(), 1.15)
	
def test19():
	liner = liner19

	liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)
	liner.CableTruss.setStageCableProperties(True)

	liner.CableTruss.setMaterialType(MaterialType.ELASTIC)
	liner.CableTruss.setActivateThermal(False)

	sf2 = liner.CableTruss.stageFactorInterface.createStageFactor(2)
	sf4 = liner.CableTruss.stageFactorInterface.createStageFactor(4)

	sf2.setCableDiameterFactor(1.6)

	sf4.setCableDiameterFactor(1.15)

	sf_dict = liner.CableTruss.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.CableTruss.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.CableTruss.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getCableDiameterFactor(), 1)

	assert(sf2_fin.getCableDiameterFactor(), 1.6)

	assert(sf3.getCableDiameterFactor(), 1.6)

	assert(sf4_fin.getCableDiameterFactor(), 1.15)  

def test20():
	liner = liner20

	liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)
	liner.CableTruss.setStageCableProperties(True)

	liner.CableTruss.setMaterialType(MaterialType.PLASTIC)
	liner.CableTruss.setActivateThermal(True)
	liner.CableTruss.setThermalExpansion(False)

	sf2 = liner.CableTruss.stageFactorInterface.createStageFactor(2)
	sf4 = liner.CableTruss.stageFactorInterface.createStageFactor(4)

	sf2.setSpecificHeatCapacityFactor(1.8)

	sf4.setSpecificHeatCapacityFactor(1.17)

	sf_dict = liner.CableTruss.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.CableTruss.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.CableTruss.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.8)

	assert(sf3.getSpecificHeatCapacityFactor(), 1.8)

	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.17)

def test21():
	liner = liner21

	liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)
	liner.CableTruss.setStageCableProperties(True)

	liner.CableTruss.setMaterialType(MaterialType.ELASTIC)
	liner.CableTruss.setActivateThermal(True)
	liner.CableTruss.setThermalExpansion(False)

	sf2 = liner.CableTruss.stageFactorInterface.createStageFactor(2)
	sf4 = liner.CableTruss.stageFactorInterface.createStageFactor(4)

	sf2.setSpecificHeatCapacityFactor(1.8)

	sf4.setSpecificHeatCapacityFactor(1.17)

	sf_dict = liner.CableTruss.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.CableTruss.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.CableTruss.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.8)

	assert(sf3.getSpecificHeatCapacityFactor(), 1.8)

	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.17)

def test22():
	liner = liner22

	liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)
	liner.CableTruss.setStageCableProperties(True)

	liner.CableTruss.setMaterialType(MaterialType.PLASTIC)
	liner.CableTruss.setActivateThermal(True)
	liner.CableTruss.setThermalExpansion(True)

	sf2 = liner.CableTruss.stageFactorInterface.createStageFactor(2)
	sf4 = liner.CableTruss.stageFactorInterface.createStageFactor(4)

	sf2.setYoungsModulusFactor(1.1)
	sf2.setAxialStrainExpansionFactor(1.2)
	sf2.setTensileStrengthPeakFactor(1.3)
	sf2.setTensileStrengthResidualFactor(1.4)
	sf2.setUnitWeightFactor(1.5)
	sf2.setCableDiameterFactor(1.6)
	sf2.setExpansionCoefficientFactor(1.7)
	sf2.setSpecificHeatCapacityFactor(1.8)

	sf4.setYoungsModulusFactor(1.9)
	sf4.setAxialStrainExpansionFactor(1.11)
	sf4.setTensileStrengthPeakFactor(1.12)
	sf4.setTensileStrengthResidualFactor(1.13)
	sf4.setUnitWeightFactor(1.14)
	sf4.setCableDiameterFactor(1.15)
	sf4.setExpansionCoefficientFactor(1.16)
	sf4.setSpecificHeatCapacityFactor(1.17)

	liner.CableTruss.stageFactorInterface.setDefinedStageFactors(StageFactorDefinitionMethod.RELATIVE_STAGE_FACTOR, {2:sf2,4:sf4})

	sf_dict = liner.CableTruss.stageFactorInterface.getDefinedStageFactors()

	sf1 = liner.CableTruss.stageFactorInterface.getStageFactor(1)
	sf2_fin = sf_dict[2]
	sf3 = liner.CableTruss.stageFactorInterface.getStageFactor(3)
	sf4_fin = sf_dict[4]

	assert(sf1.getYoungsModulusFactor(), 1)
	assert(sf1.getAxialStrainExpansionFactor(), 1) 
	assert(sf1.getTensileStrengthPeakFactor(), 1)
	assert(sf1.getTensileStrengthResidualFactor(), 1)
	assert(sf1.getUnitWeightFactor(), 1)
	assert(sf1.getCableDiameterFactor(), 1)
	assert(sf1.getExpansionCoefficientFactor(), 1)
	assert(sf1.getSpecificHeatCapacityFactor(), 1)

	assert(sf2_fin.getYoungsModulusFactor(), 1.1)
	assert(sf2_fin.getAxialStrainExpansionFactor(), 1.2)
	assert(sf2_fin.getTensileStrengthPeakFactor(), 1.3)
	assert(sf2_fin.getTensileStrengthResidualFactor(), 1.4)
	assert(sf2_fin.getUnitWeightFactor(), 1.5)
	assert(sf2_fin.getCableDiameterFactor(), 1.6)
	assert(sf2_fin.getExpansionCoefficientFactor(), 1.7)
	assert(sf2_fin.getSpecificHeatCapacityFactor(), 1.8)

	assert(sf3.getYoungsModulusFactor(), 1.1)
	assert(sf3.getAxialStrainExpansionFactor(), 1.2)
	assert(sf3.getTensileStrengthPeakFactor(), 1.3)
	assert(sf3.getTensileStrengthResidualFactor(), 1.4)
	assert(sf3.getUnitWeightFactor(), 1.5)
	assert(sf3.getCableDiameterFactor(), 1.6)
	assert(sf3.getExpansionCoefficientFactor(), 1.7)
	assert(sf3.getSpecificHeatCapacityFactor(), 1.8)

	assert(sf4_fin.getYoungsModulusFactor(), 1.9)
	assert(sf4_fin.getAxialStrainExpansionFactor(), 1.11)
	assert(sf4_fin.getTensileStrengthPeakFactor(), 1.12)
	assert(sf4_fin.getTensileStrengthResidualFactor(), 1.13)
	assert(sf4_fin.getUnitWeightFactor(), 1.14)
	assert(sf4_fin.getCableDiameterFactor(), 1.15)  
	assert(sf4_fin.getExpansionCoefficientFactor(), 1.16)
	assert(sf4_fin.getSpecificHeatCapacityFactor(), 1.17)

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

model.save()

pass