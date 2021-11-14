class Elevator:

    def __init__(self, id, speed=5, minFloor=5, maxFloor=11, closeTime=5, openTime=5, startTime=5, stopTime=5) ->None:
        self._id=id
        self._speed=speed
        self._minFloor=minFloor
        self._maxFloor=maxFloor
        self._closeTime=closeTime
        self._openTime=openTime
        self._startTime=startTime
        self._stopTime=stopTime

    def __str__(self) -> str:
        return "id: "+ str(self._id)+ " speed: "+str(self._speed)+" minFloor: "