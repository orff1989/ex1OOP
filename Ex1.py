import sys
import json

from Building import Building

#building =sys.argv[1]
#calls = sys.argv[2]
#out = sys.argv[3]
#print("building= " + building +" calls= " + calls +" out= "+ out)
b1= Building()
print(b1)
b1.loadJson("B2.json")
print(b1._elevators[0])
