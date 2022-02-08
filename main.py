from Espresso import Espresso
from Mocha import Mocha

beverage = Espresso()
beverage = Mocha(beverage)
beverage = Mocha(beverage)

print(beverage.getDiscription(), beverage.cost(), 'RUB')
