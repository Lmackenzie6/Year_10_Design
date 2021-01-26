

val = "00:00"

h = val[0:2]

h = int(h)

m = val[3:5]

timeOfDay = "AM"

if (12 <= h <= 23):
	timeOfDay = "PM"
	h = h - 12

if (h == 0):
	h = 12


print(str(h)+":"+str(m))