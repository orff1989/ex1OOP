import csv
class Call:

    def __init__(self,elevCall="Elevator call", time=0, srcFloor=0, destFloor=0, status=0, assignment=-1):
        self._elevCall=elevCall
        self._time=time
        self._srcFloor=srcFloor
        self._destFloor=destFloor
        self._status=status
        self._assignment=assignment

class Calls:
    def Calls(self, calls=[]):
      self._calls=calls



    def loadCSV(self, file):
        allTheCalls = []
        with open(file) as f:
            reader = csv.reader(f)
            for row in reader:
               c = Call(elevCall=row[0],time=float(row[1]),srcFloor=int(row[2]),destFloor=int(row[3]),status=int(row[4]),assignment=int(row[5]))
               allTheCalls.append(c)
            self._calls=allTheCalls


    def exportCSv(self, file):
        ncalls =[]
        for c in self._calls:
            ncalls.append(c.__dict__.values())

        with open(file,'w', newline="") as f:
            writeOnCSV = csv.writer(f)
            writeOnCSV.writerows(ncalls)

    @property
    def calls(self):
        return self._calls