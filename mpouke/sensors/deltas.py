import csv

data = csv.reader(open('shortgestures.csv'), delimiter=',')
xlist = []
initial = float(0)


for row in data:
	xlist.append(row[0])
	ylist.append(row[1])
	zlist.append(row[2])

def velocity(ini, acc, time):
	vel = ini + acc*time
	return vel

for x in xlist:
	acc = float(x)
	final = velocity(initial, acc, float(0.1))
	initial = final
	print initial

#new_position = current_position + velocity * elapsed