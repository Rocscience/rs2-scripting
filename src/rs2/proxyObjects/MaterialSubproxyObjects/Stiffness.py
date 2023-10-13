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
	def __init__(self, server : Client, ID, documentProxyID):
		self.Isotropic = Isotropic(server, ID, documentProxyID)
		self.TransverselyIsotropic = TransverselyIsotropic(server, ID, documentProxyID)
		self.Orthotropic = Orthotropic(server, ID, documentProxyID)
		self.NonLinearHyperbolic = NonLinearHyperbolic(server, ID, documentProxyID)
		self.NonLinearIsotropic = NonLinearIsotropic(server, ID, documentProxyID)
		self.ViscoElastic = ViscoElastic(server, ID, documentProxyID)
		self.Custom = Custom(server, ID, documentProxyID)
		self.ChSoil = ChSoil(server, ID, documentProxyID)
		self.CySoil = CySoil(server, ID, documentProxyID)
		self.DoubleYield = DoubleYield(server, ID, documentProxyID)
		self.HardeningSoil = HardeningSoil(server, ID, documentProxyID)
		self.HardeningSoilSmallStrainStiffness = HardeningSoilSmallStrainStiffness(server, ID, documentProxyID)
		self.SoftSoil = SoftSoil(server, ID, documentProxyID)
		self.SoftSoilCreep = SoftSoilCreep(server, ID, documentProxyID)
		self.SwellingRock = SwellingRock(server, ID, documentProxyID)
		self.ManzariAndDafalias = ManzariAndDafalias(server, ID, documentProxyID)
		self.Norsand = Norsand(server, ID, documentProxyID)
		self.Pm4Sand = Pm4Sand(server, ID, documentProxyID)
		self.Pm4Silt = Pm4Silt(server, ID, documentProxyID)
		super().__init__(server, ID, documentProxyID)
	def getElasticType(self) -> MaterialElasticityTypes:
		return MaterialElasticityTypes(self._getEnumEMaterialElasticityTypesProperty("MP_ELASTIC_TYPE"))
	def setElasticType(self, value: MaterialElasticityTypes):
		return self._setEnumEMaterialElasticityTypesProperty("MP_ELASTIC_TYPE", value)
