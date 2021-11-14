import json
from Elevator import Elevator
import csv

class Building:

    def __init__(self, minFloor=0, maxFloor=10, elevators=[]) ->None:
        self._minFloor=minFloor
        self._maxFloor=maxFloor
        self._elevators=elevators

    def __str__(self) ->str:
        return str(self.__dict__)


    def loadJson(self, file):
        try:
            with open(file, "r+") as f:
                dicBuilding=json.load(f)
                self._minFloor=dicBuilding['_minFloor']
                self._maxFloor=dicBuilding['_maxFloor']
                theElevators=dicBuilding["_elevators"]
                for i in theElevators:
                    elev= Elevator(i["_id"],i["_speed"], i["_minFloor"],i["_maxFloor"], i["_closeTime"],i["_openTime"], i["_startTime"], i["_stopTime"])
                    self._elevators.append(elev)
        except IOError as e:
           print(e)

