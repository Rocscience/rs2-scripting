from rs2.ProxyObject import ProxyObject
from enum import Enum
from rs2.Client import Client
class PropertyProxy(ProxyObject):
	def __init__(self, server : Client, ID, documentProxyID) :
		self.documentProxyID = documentProxyID
		super().__init__(server, ID)
	def _getDoubleProperty(self, propertyName: str):
		return self._callFunction("getDoubleProperty", [propertyName])
	def _setDoubleProperty(self, propertyName: str, value):
		return self._callFunction("setDoubleProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getBoolProperty(self, propertyName: str):
		return self._callFunction("getBoolProperty", [propertyName])
	def _setBoolProperty(self, propertyName: str, value):
		return self._callFunction("setBoolProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEBulgeTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEBulgeTypesProperty", [propertyName])
	def _setEnumEBulgeTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEBulgeTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEBoltModelsProperty(self, propertyName: str):
		return self._callFunction("getEnumEBoltModelsProperty", [propertyName])
	def _setEnumEBoltModelsProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEBoltModelsProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getIntProperty(self, propertyName: str):
		return self._callFunction("getIntProperty", [propertyName])
	def _setIntProperty(self, propertyName: str, value):
		return self._callFunction("setIntProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumESecondaryBondLengthTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumESecondaryBondLengthTypeProperty", [propertyName])
	def _setEnumESecondaryBondLengthTypeProperty(self, propertyName: str, value):
		return self._callFunction("setEnumESecondaryBondLengthTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getCStringProperty(self, propertyName: str):
		return self._callFunction("getCStringProperty", [propertyName])
	def _setCStringProperty(self, propertyName: str, value):
		return self._callFunction("setCStringProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getUnsignedLongProperty(self, propertyName: str):
		return self._callFunction("getUnsignedLongProperty", [propertyName])
	def _setUnsignedLongProperty(self, propertyName: str, value):
		return self._callFunction("setUnsignedLongProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEBoltTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEBoltTypesProperty", [propertyName])
	def _setEnumEBoltTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEBoltTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEGeometryChoiceProperty(self, propertyName: str):
		return self._callFunction("getEnumEGeometryChoiceProperty", [propertyName])
	def _setEnumEGeometryChoiceProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEGeometryChoiceProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEMaterialAnalysisTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEMaterialAnalysisTypesProperty", [propertyName])
	def _setEnumEMaterialAnalysisTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEMaterialAnalysisTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumELinerFormulationProperty(self, propertyName: str):
		return self._callFunction("getEnumELinerFormulationProperty", [propertyName])
	def _setEnumELinerFormulationProperty(self, propertyName: str, value):
		return self._callFunction("setEnumELinerFormulationProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEStaticWaterModesProperty(self, propertyName: str):
		return self._callFunction("getEnumEStaticWaterModesProperty", [propertyName])
	def _setEnumEStaticWaterModesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEStaticWaterModesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumELinerTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumELinerTypesProperty", [propertyName])
	def _setEnumELinerTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumELinerTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEJointWaterPressureTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumEJointWaterPressureTypeProperty", [propertyName])
	def _setEnumEJointWaterPressureTypeProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEJointWaterPressureTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEJointStiffnessDefineProperty(self, propertyName: str):
		return self._callFunction("getEnumEJointStiffnessDefineProperty", [propertyName])
	def _setEnumEJointStiffnessDefineProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEJointStiffnessDefineProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEJointTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEJointTypesProperty", [propertyName])
	def _setEnumEJointTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEJointTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEPFPApplicationProperty(self, propertyName: str):
		return self._callFunction("getEnumEPFPApplicationProperty", [propertyName])
	def _setEnumEPFPApplicationProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEPFPApplicationProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEPileApplicationTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumEPileApplicationTypeProperty", [propertyName])
	def _setEnumEPileApplicationTypeProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEPileApplicationTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEPileEndConditionProperty(self, propertyName: str):
		return self._callFunction("getEnumEPileEndConditionProperty", [propertyName])
	def _setEnumEPileEndConditionProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEPileEndConditionProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEPileForceDisplacemtnApplicationPointProperty(self, propertyName: str):
		return self._callFunction("getEnumEPileForceDisplacemtnApplicationPointProperty", [propertyName])
	def _setEnumEPileForceDisplacemtnApplicationPointProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEPileForceDisplacemtnApplicationPointProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEPileConnectionTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumEPileConnectionTypeProperty", [propertyName])
	def _setEnumEPileConnectionTypeProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEPileConnectionTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEPileSkinResistanceTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumEPileSkinResistanceTypeProperty", [propertyName])
	def _setEnumEPileSkinResistanceTypeProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEPileSkinResistanceTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumGdiplusHatchStyleProperty(self, propertyName: str):
		return self._callFunction("getEnumGdiplusHatchStyleProperty", [propertyName])
	def _setEnumGdiplusHatchStyleProperty(self, propertyName: str, value):
		return self._callFunction("setEnumGdiplusHatchStyleProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEMaterialElasticityTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEMaterialElasticityTypesProperty", [propertyName])
	def _setEnumEMaterialElasticityTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEMaterialElasticityTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEStrengthCriteriaTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEStrengthCriteriaTypesProperty", [propertyName])
	def _setEnumEStrengthCriteriaTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEStrengthCriteriaTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEUnsaturatedParameterTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumEUnsaturatedParameterTypeProperty", [propertyName])
	def _setEnumEUnsaturatedParameterTypeProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEUnsaturatedParameterTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEUnsaturatedShearStrengthTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumEUnsaturatedShearStrengthTypeProperty", [propertyName])
	def _setEnumEUnsaturatedShearStrengthTypeProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEUnsaturatedShearStrengthTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEUnsaturatedSingleEffectiveStressMethodProperty(self, propertyName: str):
		return self._callFunction("getEnumEUnsaturatedSingleEffectiveStressMethodProperty", [propertyName])
	def _setEnumEUnsaturatedSingleEffectiveStressMethodProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEUnsaturatedSingleEffectiveStressMethodProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEUnsaturatedTabularValueMethodProperty(self, propertyName: str):
		return self._callFunction("getEnumEUnsaturatedTabularValueMethodProperty", [propertyName])
	def _setEnumEUnsaturatedTabularValueMethodProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEUnsaturatedTabularValueMethodProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEMaterialBehavioursProperty(self, propertyName: str):
		return self._callFunction("getEnumEMaterialBehavioursProperty", [propertyName])
	def _setEnumEMaterialBehavioursProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEMaterialBehavioursProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEGroundWaterModesProperty(self, propertyName: str):
		return self._callFunction("getEnumEGroundWaterModesProperty", [propertyName])
	def _setEnumEGroundWaterModesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEGroundWaterModesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEAnisotropyDefinitionsProperty(self, propertyName: str):
		return self._callFunction("getEnumEAnisotropyDefinitionsProperty", [propertyName])
	def _setEnumEAnisotropyDefinitionsProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEAnisotropyDefinitionsProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEMVModelProperty(self, propertyName: str):
		return self._callFunction("getEnumEMVModelProperty", [propertyName])
	def _setEnumEMVModelProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEMVModelProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEInitialElementLoadingTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumEInitialElementLoadingTypeProperty", [propertyName])
	def _setEnumEInitialElementLoadingTypeProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEInitialElementLoadingTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEHuTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEHuTypesProperty", [propertyName])
	def _setEnumEHuTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEHuTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEUnloadingConditionsProperty(self, propertyName: str):
		return self._callFunction("getEnumEUnloadingConditionsProperty", [propertyName])
	def _setEnumEUnloadingConditionsProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEUnloadingConditionsProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEElasticParametersProperty(self, propertyName: str):
		return self._callFunction("getEnumEElasticParametersProperty", [propertyName])
	def _setEnumEElasticParametersProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEElasticParametersProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEPoissonRatioTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumEPoissonRatioTypeProperty", [propertyName])
	def _setEnumEPoissonRatioTypeProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEPoissonRatioTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumENLIFormulaTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumENLIFormulaTypesProperty", [propertyName])
	def _setEnumENLIFormulaTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumENLIFormulaTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEViscoElasticTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEViscoElasticTypesProperty", [propertyName])
	def _setEnumEViscoElasticTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEViscoElasticTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumECustomModeProperty(self, propertyName: str):
		return self._callFunction("getEnumECustomModeProperty", [propertyName])
	def _setEnumECustomModeProperty(self, propertyName: str, value):
		return self._callFunction("setEnumECustomModeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumETensileCutoffOptionsProperty(self, propertyName: str):
		return self._callFunction("getEnumETensileCutoffOptionsProperty", [propertyName])
	def _setEnumETensileCutoffOptionsProperty(self, propertyName: str, value):
		return self._callFunction("setEnumETensileCutoffOptionsProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumESpecificVolumeAtUnitPressureProperty(self, propertyName: str):
		return self._callFunction("getEnumESpecificVolumeAtUnitPressureProperty", [propertyName])
	def _setEnumESpecificVolumeAtUnitPressureProperty(self, propertyName: str, value):
		return self._callFunction("setEnumESpecificVolumeAtUnitPressureProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEInitialStateOfConsolidationProperty(self, propertyName: str):
		return self._callFunction("getEnumEInitialStateOfConsolidationProperty", [propertyName])
	def _setEnumEInitialStateOfConsolidationProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEInitialStateOfConsolidationProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEMCCapTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumEMCCapTypeProperty", [propertyName])
	def _setEnumEMCCapTypeProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEMCCapTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumECapHardeningTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumECapHardeningTypesProperty", [propertyName])
	def _setEnumECapHardeningTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumECapHardeningTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEConeHardeningTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEConeHardeningTypesProperty", [propertyName])
	def _setEnumEConeHardeningTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEConeHardeningTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEDilationTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEDilationTypesProperty", [propertyName])
	def _setEnumEDilationTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEDilationTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumECapTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumECapTypesProperty", [propertyName])
	def _setEnumECapTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumECapTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumENorSandInitialConsolidationConditionProperty(self, propertyName: str):
		return self._callFunction("getEnumENorSandInitialConsolidationConditionProperty", [propertyName])
	def _setEnumENorSandInitialConsolidationConditionProperty(self, propertyName: str, value):
		return self._callFunction("setEnumENorSandInitialConsolidationConditionProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEFinnFormulaProperty(self, propertyName: str):
		return self._callFunction("getEnumEFinnFormulaProperty", [propertyName])
	def _setEnumEFinnFormulaProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEFinnFormulaProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEFinnByrneDefinitionProperty(self, propertyName: str):
		return self._callFunction("getEnumEFinnByrneDefinitionProperty", [propertyName])
	def _setEnumEFinnByrneDefinitionProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEFinnByrneDefinitionProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEStressHistoryTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEStressHistoryTypesProperty", [propertyName])
	def _setEnumEStressHistoryTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEStressHistoryTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEStressHistoryDefinitionMethodsProperty(self, propertyName: str):
		return self._callFunction("getEnumEStressHistoryDefinitionMethodsProperty", [propertyName])
	def _setEnumEStressHistoryDefinitionMethodsProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEStressHistoryDefinitionMethodsProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEDilationOptionProperty(self, propertyName: str):
		return self._callFunction("getEnumEDilationOptionProperty", [propertyName])
	def _setEnumEDilationOptionProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEDilationOptionProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumECySoilCapOptionProperty(self, propertyName: str):
		return self._callFunction("getEnumECySoilCapOptionProperty", [propertyName])
	def _setEnumECySoilCapOptionProperty(self, propertyName: str, value):
		return self._callFunction("setEnumECySoilCapOptionProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEDilatancyProperty(self, propertyName: str):
		return self._callFunction("getEnumEDilatancyProperty", [propertyName])
	def _setEnumEDilatancyProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEDilatancyProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEInitialConsolidationProperty(self, propertyName: str):
		return self._callFunction("getEnumEInitialConsolidationProperty", [propertyName])
	def _setEnumEInitialConsolidationProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEInitialConsolidationProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumESwellingFormProperty(self, propertyName: str):
		return self._callFunction("getEnumESwellingFormProperty", [propertyName])
	def _setEnumESwellingFormProperty(self, propertyName: str, value):
		return self._callFunction("setEnumESwellingFormProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEWaterConditionProperty(self, propertyName: str):
		return self._callFunction("getEnumEWaterConditionProperty", [propertyName])
	def _setEnumEWaterConditionProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEWaterConditionProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEEnhancedSimpleSoilTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEEnhancedSimpleSoilTypesProperty", [propertyName])
	def _setEnumEEnhancedSimpleSoilTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEEnhancedSimpleSoilTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEWCInputTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumEWCInputTypeProperty", [propertyName])
	def _setEnumEWCInputTypeProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEWCInputTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
