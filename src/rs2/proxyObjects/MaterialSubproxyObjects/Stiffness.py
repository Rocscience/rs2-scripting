from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.Isotropic import Isotropic
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.TransverselyIsotropic import TransverselyIsotropic
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.Orthotropic import Orthotropic
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.NonLinearHyperbolic import NonLinearHyperbolic
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.NonLinearIsotropic import NonLinearIsotropic
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.ViscoElastic import ViscoElastic
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.Custom import Custom
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.ChSoil import ChSoil
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.CySoil import CySoil
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.DoubleYield import DoubleYield
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.HardeningSoil import HardeningSoil
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.HardeningSoilSmallStrainStiffness import HardeningSoilSmallStrainStiffness
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.SoftSoil import SoftSoil
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.SoftSoilCreep import SoftSoilCreep
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.SwellingRock import SwellingRock
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.ManzariAndDafalias import ManzariAndDafalias
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.Norsand import Norsand
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.Pm4Sand import Pm4Sand
from rs2.proxyObjects.MaterialSubproxyObjects.StiffnessSubProxyObjects.Pm4Silt import Pm4Silt
class Stiffness(PropertyProxy):
	"""
	:ref:`Material Property Stiffness Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		self.Isotropic = Isotropic(client, ID, documentProxyID)
		self.TransverselyIsotropic = TransverselyIsotropic(client, ID, documentProxyID)
		self.Orthotropic = Orthotropic(client, ID, documentProxyID)
		self.NonLinearHyperbolic = NonLinearHyperbolic(client, ID, documentProxyID)
		self.NonLinearIsotropic = NonLinearIsotropic(client, ID, documentProxyID)
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
		super().__init__(client, ID, documentProxyID)
	def getElasticType(self) -> MaterialElasticityTypes:
		return MaterialElasticityTypes(self._getEnumEMaterialElasticityTypesProperty("MP_ELASTIC_TYPE"))
	def setElasticType(self, value: MaterialElasticityTypes):
		return self._setEnumEMaterialElasticityTypesProperty("MP_ELASTIC_TYPE", value)