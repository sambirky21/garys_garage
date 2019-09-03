from leaf import Leaf
from crosstrek import CrossTrek
from mustang import Mustang
from ram import Ram
from pumpstation import PumpStation
from chargingstation import ChargingStation

ram = Ram()
must = Mustang()
tree = Leaf()

gas_pump_station = PumpStation()
electric_charging_station = ChargingStation()

gas_pump_station.add_vehicle(ram)
gas_pump_station.add_vehicle(must)
electric_charging_station.add_vehicle(tree)