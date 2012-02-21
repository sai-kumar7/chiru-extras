import math
import csv
import serial
import svmclassifierinit
from time import sleep
import numpy as np
from pylab import *
from numpy import linalg as LA
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#ion()
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

dataset=csv.reader(open('demo.csv'), delimiter=',')

gesturelist=[]

port = "/dev/rfcomm1"
ser = serial.Serial(port, baudrate=9600, timeout=10)

def euclidean(v1,v2):
    d=0.0
    for i in range(len(v1)):
        d+=(v1[i]-v2[i])**2
        return math.sqrt(d)

def velocity(ini, acc, time):
	vel = ini + acc*time
	return vel

time = float(0.01)

print "connecting..."
sleep(2)
ser.write("echo on"+"\r\n")
ser.write("stop all"+"\r\n")
ser.write("sett 114500000"+"\r\n")
ser.write("sens +000005000 10 1 0"+"\r\n")
print ser.portstr

vectorlist=[]
    
def gesture3d():
    accelerations=[]
    print "3d gesture..."
    buffer = ser.read(ser.inWaiting())
    ser.flushOutput()
    ser.flushInput()
    for r in range(256):
        gvector=[]
	ser.flushInput()
	gdata = ser.readline()
        #print gdata
	gdata = gdata.split(",")
        #print gdata
	for g in gdata:
	    g=g.rstrip("\r\n")
	    gvector.append(g)
	if len(gvector) > 3:
            #print gvector
	    gline = gvector[-3:]
            #print gline
	    giline = [int(l) for l in gline]
            #print giline
	    #iline.append('Left')
	    #output.writerow(iline)
	    accelerations.append(giline)
	    #wholedata=vectorcreate()
	    #result=knntest2.knnestimate(knntest2.data,iline)
	    #print result
	    #print iline
    #print accelerations
    gesture=transform(accelerations)
    #gxs=[]
    #for g in gesture: gxs.append(g[0]) 
    #gys=[]
    #for g in gesture: gys.append(g[1])
    #gzs=[]
    #for g in gesture: gzs.append(g[2])

    score=measure2(gesture)
    print 'All scores: '
    for e, r in zip(score,gesturelist):
        print 'Score: ',e,' Gesture: ',r[1][3]
    print 'Maximum score: ',max(score)
    #a=score.index(min(score))
    a=score.index(max(score))
    #print a
    #sxs=[]
    #for s in gesturelist[a]: sxs.append(s[0])
    #sys=[]
    #for s in gesturelist[a]: sys.append(s[1])
    #szs=[]
    #for s in gesturelist[a]: szs.append(s[2])

    print 'Recognized gesture: ',gesturelist[a][1][3]
    #print gesturelist[a][1]
    #ax.scatter(gxs, gys, gzs, s=20, c='b')
    #ax.scatter(sxs, sys, szs, s=20, c='r')
    #ax.set_xlabel('X Label')
    #ax.set_ylabel('Y Label')
    #ax.set_zlabel('Z Label')
    #draw()
    raw_input("Press enter when done...")    
    #close()

def transform(accelerations):
    accs=accelerations
    #print accs
    counter = 0
    xs = []
    ys = []
    zs = []
    positions=[]
    gestureacc=np.array([])
    allaccx=np.array([])
    allaccy=np.array([])
    allaccz=np.array([])
    turnedx=np.array([])
    turnedy=np.array([])
    turnedz=np.array([])

    fftvelx=np.zeros(shape=(256,1))
    fftvely=np.zeros(shape=(256,1))
    fftvelz=np.zeros(shape=(256,1))


    initialx = float(0)
    initialy = float(0)
    initialz = float(0)

    initialposx = float(0)
    initialposy = float(0)
    initialposz = float(0)
    for i in accs:
	#print i
	#print len(i)
	accx = float(i[0])
        #accy = float(row[1]-1000)
        accy = float(i[1])
        #accy = accy - 1000
        accz = float(i[2])

        allaccx = np.append(allaccx,accx)
        allaccy = np.append(allaccy,accy)
        allaccz = np.append(allaccz,accz)
        #print allaccx
		
        counter = counter + 1
	
        meanx = allaccx.mean()	
	meany = allaccy.mean()
	meanz = allaccz.mean()

	meanvector = np.array([meanx, meany, meanz])

	#print meanvector	

        xymatrix = np.array([[1,0,0],[0,1,0],[0,0,0]])

	xyprojection = np.dot(meanvector,xymatrix)
        xaxis = np.array([1,0,0])
	alpha = np.arccos(np.dot(xyprojection,xaxis)/(LA.norm(xyprojection)*LA.norm(xaxis)))
        beta = np.arccos(np.dot(meanvector,xyprojection)/(LA.norm(meanvector)*LA.norm(xyprojection)))

        #xyprojection[2]=0
	#meanmagn = LA.norm(meanvector)
	#projmagn = LA.norm(xyprojection)
	#unitmean = meanvector/meanmagn
	#unitproj = xyprojection/projmagn	
		

	#print meanmagn
	#print projmagn	
	
	#xynormal = np.array([0,0,1])
	#xyangle = np.arccos(np.dot(unitmean,xynormal))
	#print xyangle
	#xyangle = np.degrees(xyangle)	
	#print xyangle

	#products = np.dot(unitmean,xaxis)
	 
	#print products

	#alpha = np.arccos(products)
	#alpha = np.degrees(alpha)
	#beta = 90-xyangle
	#print beta
	#beta = np.radians(beta)
	#print beta
	#print alpha
	#print beta

	mrot = np.array([[((np.cos(alpha))**2)*np.sin(beta)+(np.sin(alpha))**2,(np.cos(alpha))*np.sin(alpha)*(np.sin(beta)-1),-(np.cos(alpha))*np.cos(beta)],
		           [np.cos(alpha)*np.sin(alpha)*(np.sin(beta)-1),((np.sin(alpha))**2)*np.sin(beta)+(np.cos(alpha))**2,-(np.sin(alpha))*np.cos(beta)],
	                   [np.cos(alpha)*np.cos(beta),np.sin(alpha)*np.cos(beta),np.sin(beta)]])

	
    for i,j,k in zip(allaccx,allaccy,allaccz):
	accsample = np.asarray([i,j,k])
	#print accsample
	turned = np.dot(accsample,mrot)
	#turned = accsample-meanvector
	#print turned

	acx = turned[0]
	acy = turned[1]
	acz = turned[2]
		
	turnedx = np.append(turnedx,acx)	
	turnedy = np.append(turnedy,acy)
	turnedz = np.append(turnedz,acz)	
			
    turnedx = (turnedx-np.mean(turnedx))/np.std(turnedx)
    turnedy = (turnedy-np.mean(turnedy))/np.std(turnedy)
    turnedz = (turnedz-np.mean(turnedz))/np.std(turnedz)

    #allaccx = (allaccx-np.mean(allaccx))/np.std(allaccx)
    #allaccy = (allaccy-np.mean(allaccy))/np.std(allaccy)
    #allaccz = (allaccz-np.mean(allaccz))/np.std(allaccz)	
	

    #turnedx = (turnedx-np.mean(turnedx))
    #turnedy = (turnedy-np.mean(turnedy))
    #turnedz = (turnedz-np.mean(turnedz))	



    freqx = np.fft.fft(turnedx,256)
    freqy = np.fft.fft(turnedy,256)
    freqz = np.fft.fft(turnedz,256)


    freqx[:2]=0
    freqy[:2]=0
    freqz[:2]=0	

    invx = np.fft.ifft(freqx)
    invy = np.fft.ifft(freqy)
    invz = np.fft.ifft(freqz)

    tx = invx.real
    ty = invy.real
    tz = invz.real
	
    #print turnedx

    #print turnedx
    #print turnedy
    #print turnedz

    for a,b,c in zip(tx,ty,tz):
		
        #print c

        velx = velocity(initialx, a, time)
	vely = velocity(initialy, b, time)
	velz = velocity(initialz, c, time)
		 
	posx = initialposx + velx*time
	posy = initialposy + vely*time
	posz = initialposz + velz*time

        if len(accs[0])==4:
	    positions.append([posx,posy,posz,accs[0][3]])
        else:
            positions.append([posx,posy,posz])
	xs.append(posx)
	ys.append(posy)
	zs.append(posz)

	initialx = velx
	initialy = vely
	initialz = velz
	
	initialposx = posx
	initialposy = posy
	initialposz = posz		
	
	gesture=[xs,ys,zs]
	#return gesture
    #print positions
    #raw_input("Press enter when done...")   
    return positions

def measure(gesture):
    distances=[]
    for i in gesturelist:
        disp=[]
        for a,b in zip(gesture,i):
            d=euclidean(a,b[:3])
            d/=256
            disp.append(d)
        distances.append(sum(disp))
    return distances

def measure2(gesture):
    cdistances=[]
    gesture=np.asarray(gesture)
    for i in gesturelist:
        v2 = np.array([])
        #print i
        for r in i:
            v2 = np.append(v2,(r[:3]))
        v2=v2.flatten()
        gesture=gesture.flatten()
        #print len(v2)
        #print len(gesture)
        cdistance=np.arccos(np.dot(gesture,v2)/(LA.norm(gesture)*LA.norm(v2)))
        inverse=1/cdistance
        cdistances.append(inverse)
    return cdistances


for row in dataset:
    gesture=[]
    for r in range(256):
	try:
            gesture.append(row)
	    if dataset.next(): row=dataset.next()
        except StopIteration :
	    break		
    gpos=transform(gesture)
    gesturelist.append(gpos)
    #print gpos
    #raw_input("Press enter when done...")  

#print gesturelist

#raw_input("Press enter when done...")    

try:
	while True:
	    vector=[]
            buffer = ser.read(ser.inWaiting())
	    ser.flushOutput()
            ser.flushInput()
	    data = ser.readline()
	    #print "Read line"
	    data = data.split(",")
            print "Waiting for gesture"
	    for i in data:
	    	i=i.rstrip("\r\n")
		vector.append(i)
	    if len(vector) > 3:
		line = vector[-3:]
                #print line
		iline = [float(n) for n in line]
		#print vector[-6:]
		#output.writerow(line)
	   	result=svmclassifierinit.classify(iline)
		#print result
		if str('1.0') in str(result): gesture3d()

except KeyboardInterrupt :
	print "Stopping sensor output"
	ser.write("stop all"+"\r\n")
	print "Closing serial port" 
	ser.close()

