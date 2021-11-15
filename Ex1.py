import sys
import json
from Call import Call, Calls
from Building import Building

theBuilding=Building() # creating a building
theBuilding.loadJson(sys.argv[1]) # getting the building attributes from the json file

theCall=Calls() # creating a calls object
theCall.loadCSV(sys.argv[2]) #  getting the calls attributes from the csv file

theCall.exportCSv(sys.argv[3]) # exporting the calls to a new csv file

theBuilding._elevators[1].timeForTravel(1,6)
