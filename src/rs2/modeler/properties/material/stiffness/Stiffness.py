from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.material.stiffness.Isotropic import Isotropic
from rs2.modeler.properties.material.stiffness.TransverselyIsotropic import TransverselyIsotropic
from rs2.modeler.properties.material.stiffness.Orthotropic import Orthotropic
from rs2.modeler.properties.material.stiffness.NonLinearHyperbolic import NonLinearHyperbolic
from rs2.modeler.properties.material.stiffness.NonLinearIsotropic import NonLinearIsotropic
from rs2.modeler.properties.material.stiffness.ViscoElastic import ViscoElastic
from rs2.modeler.properties.material.stiffness.Custom import Custom
from rs2.modeler.properties.material.stiffness.ChSoil import ChSoil
from rs2.modeler.properties.material.stiffness.CySoil import CySoil
from rs2.modeler.properties.material.stiffness.DoubleYield import DoubleYield
from rs2.modeler.properties.material.stiffness.HardeningSoil import HardeningSoil
from rs2.modeler.properties.material.stiffness.HardeningSoilSmallStrainStiffness import HardeningSoilSmallStrainStiffness
from rs2.modeler.properties.material.stiffness.SoftSoil import SoftSoil
from rs2.modeler.properties.material.stiffness.SoftSoilCreep import SoftSoilCreep
from rs2.modeler.properties.material.stiffness.SwellingRock import SwellingRock
from rs2.modeler.properties.material.stiffness.ManzariAndDafalias import ManzariAndDafalias
from rs2.modeler.properties.material.stiffness.Norsand import Norsand
from rs2.modeler.properties.material.stiffness.Pm4Sand import Pm4Sand
from rs2.modeler.properties.material.stiffness.Pm4Silt import Pm4Silt
class Stiffness(PropertyProxy):
	"""
	:ref:`Material Property Stiffness Example`

	Attributes:
		Isotropic (Isotropic) : Reference object for modifying isotropic stiffness properties
		TransverselyIsotropic (TransverselyIsotropic) : Reference object for modifying transversely isotropic stiffness properties
		Orthotropic (Orthotropic) : Reference object for modifying orthotropic stiffness properties
		NonLinearHyperbolic (NonLinearHyperbolic) : Reference object for modifying non liner hyperbolic stiffness properties
		NonLinearIsotropic (NonLinearIsotropic) : Reference object for modifying non linear isotropic stiffness properties
		ViscoElastic (ViscoElastic) : Reference object for modifying visco elastic stiffness properties
		Custom (Custom) : Reference object for modifying custom stiffness properties
		ChSoil (ChSoil) : Reference object for ch soil stiffness properties
		CySoil (CySoil) : Reference object for modifying cy soil stiffness properties
		DoubleYield (DoubleYield) : Reference object for modifying double yield stiffness properties
		HardeningSoil (HardeningSoil) : Reference object for modifying hardening soil stiffness properties
		HardeningSoilSmallStrainStiffness (HardeningSoilSmallStrainStiffness) : Reference object for modifying hardening soil small strain stiffness properties
		SoftSoil (SoftSoil) : Reference object for modifying soft soil stiffness properties
		SoftSoilCreep (SoftSoilCreep) : Reference object for modifying soft soil creep stiffness properties
		SwellingRock (SwellingRock) : Reference object for modifying swelling rock stiffness properties
		ManzariAndDafalias (ManzariAndDafalias) : Reference object for modifying manzari and dafalias stiffness properties
		Norsand (Norsand) : Reference object for modifying nor sand stiffness properties
		Pm4Sand (Pm4Sand) : Reference object for modifying pm4 sand stiffness properties
		Pm4Silt (Pm4Silt) : Reference object for modifying pm4 silt stiffness properties

	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.Isotropic = Isotropic(client, ID, documentProxyID, stageFactorInterfaceID)
		self.TransverselyIsotropic = TransverselyIsotropic(client, ID, documentProxyID, stageFactorInterfaceID)
		self.Orthotropic = Orthotropic(client, ID, documentProxyID, stageFactorInterfaceID)
		self.NonLinearHyperbolic = NonLinearHyperbolic(client, ID, documentProxyID, stageFactorInterfaceID)
		self.NonLinearIsotropic = NonLinearIsotropic(client, ID, documentProxyID, stageFactorInterfaceID)
		self.ViscoElastic = ViscoElastic(client, ID, documentProxyID)
		self.Custom = Custom(client, ID, documentProxyID)
		self.ChSoil = ChSoil(client, ID, documentProxyID)
		self.CySoil = CySoil(client, ID, documentProxyID)
		self.DoubleYield = DoubleYield(client, ID, documentProxyID)
		self.HardeningSoil = HardeningSoil(client, ID, documentProxyID)
		self.HardeningSoilSmallStrainStiffness = HardeningSoilSmallStrainStiffness(client, ID, documentProxyID)
		self.SoftSoil = SoftSoil(client, ID, documentProxyID)
		self.SoftSoilCreep = SoftSoilCreep(client, ID, documentProxyID)
		self.SwellingRock = SwellingRock(client, ID, documentProxyID)
		self.ManzariAndDafalias = ManzariAndDafalias(client, ID, documentProxyID)
		self.Norsand = Norsand(client, ID, documentProxyID)
		self.Pm4Sand = Pm4Sand(client, ID, documentProxyID)
		self.Pm4Silt = Pm4Silt(client, ID, documentProxyID)
	def getElasticType(self) -> MaterialElasticityTypes:
		return MaterialElasticityTypes(self._getEnumEMaterialElasticityTypesProperty("MP_ELASTIC_TYPE"))
	def setElasticType(self, value: MaterialElasticityTypes):
		return self._setEnumEMaterialElasticityTypesProperty("MP_ELASTIC_TYPE", value)
