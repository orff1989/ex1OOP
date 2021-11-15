import sys
import json
from Call import Call, Calls
from Building import Building

theBuilding=Building() # creating a building
theBuilding.loadJson(sys.argv[1]) # getting the building attributes from the json file

theCall=Calls() # creating a calls object
theCall.loadCSV(sys.argv[2]) #  getting the calls attributes from the csv file

for c in theCall.calls: # iterating over the calls
    theTime = float('inf')
    ans=-1

    for elev in theBuilding._elevators:
        t = elev.timeForTravel(elev._pos,c._srcFloor)
        if theTime>t:
            theTime=t
            ans = elev
    ans._pos=c._destFloor
    c._assignment=ans._id

theCall.exportCSv(sys.argv[3]) # exporting the calls to a new csv file




