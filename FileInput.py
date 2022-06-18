import re
import numpy as np

### Parsing-File input and decoding
def inp(filename):

	#Open Parsing-File
	file = open(filename, 'r')

	###Cylinder height
	h = 0
	###Cylinder axis
	I = []
	###Cylinder radius
	r = []
	R = 0

	i = 0
	
	for line in file:

		str = line.strip()
		if (str.find("CYLINDRICAL_SURFACE") != -1):
			h = float(str.split()[5])
			print("Cylinder height is", h)

		elif (str.find("CARTESIAN_POINT") != -1):
			s = str.split()
			r.append(float(s[5][:-1]))
			r.append(float(s[6][:-1]))
			r.append(float(s[7][:-1]))
			R = np.sqrt(r[0]**2 + r[1]**2 + r[2]**2)
			print("Cylinder radius is ", R)

		elif ((str.find("DIRECTION") != -1) and (i==0)):
			i += 1

		elif ((str.find("DIRECTION") != -1) and (i==1)):
			s = str.split()
			I.append(float(s[5][:-1]))
			I.append(float(s[6][:-1]))
			I.append(float(s[7][:-1]))
			print("Cylinder Axis is", I)

	#return {"height":h, "radius": r, "axis": I}
	return [h, R, I]