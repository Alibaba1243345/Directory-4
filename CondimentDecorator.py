from abc import ABC, abtractmethod
from Beverage import Beverage

class CondimentDecorator(Beverage, ABC):
	@abtractmethod
	def getDescription(self)->str:
		return self._description