import csv
import numpy as np

features=[]
labels=[]

dataset=csv.reader(open('shortgestures.csv'), delimiter=',')

for row in dataset:
	ftrs=row[0:6]	
	iftrs=[]
	for f in ftrs:
		iftrs.append(float(f))
	features.append(iftrs)
	if row[6]=='Still': 
		labels.append(float(0))
	if row[6]=='PushLeft':
		labels.append(float(1))
	if row[6]=='PushRight': 
		labels.append(float(2))
	if row[6]=='PushForwards': 
		labels.append(float(3))
	if row[6]=='PushBackwards': 
		labels.append(float(4))
	if row[6]=='LargeCircleRight': 
		labels.append(float(5))
	if row[6]=='LargeCircleLeft': 
		labels.append(float(6))

print features

a = np.asarray(features)

a /= np.max(np.abs(a),axis=0)

print a

#(a.transpose()/np.sum(a, axis=1)).transpose()
