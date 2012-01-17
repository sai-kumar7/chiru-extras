import serial
from time import sleep
#import datetime
import csv
import svmclassifiergrasp
import knndir2
import svmclassifiershort

#output = csv.writer(open('directions.csv', 'wb'), delimiter=',')

port = "/dev/rfcomm0"
ser = serial.Serial(port, baudrate=9600, timeout=10)
print "connecting..."
sleep(2)
ser.write("echo on"+"\r\n")      # write a string
#ser.write("echo on"+"\r\n")      # write a string
ser.write("hello"+"\r\n")
ser.write("stop all"+"\r\n")
ser.write("sett 114500000"+"\r\n")
ser.write("ags +000005000 100 1 0"+"\r\n")
print ser.portstr 

counter=0

def grasp():
	while True:
	    global counter
	    counter+=1
	    vector=[]
	    #print "Got here"
	    data = ser.readline()
	    #print "Read line"
	    data = data.split(",")
	    for i in data:
	    	i=i.rstrip("\r\n")
		vector.append(i)
	    if len(vector) > 3:
		line = vector[-6:]
		iline = [float(n) for n in line]
		#print vector[-6:]
		#output.writerow(line)
	   	if counter > 15:
			result=svmclassifiergrasp.classify(iline)
			print result
			if str('1.0') in str(result):
				counter=0
				handle()
		else: print 'Grasp mode'
	    #sleep(0.5)
	    #print 'not blocked'

def handle():
	while True:
	    global counter
	    counter+=1
	    #print counter
	    vector=[]
	    #print "Got here"
	    data = ser.readline()
	    #print "Read line"
	    data = data.split(",")
	    for i in data:
	    	i=i.rstrip("\r\n")
		vector.append(i)
	    if len(vector) > 3:
		line = vector[-6:]
		iline = [float(n) for n in line]
		#print vector[-6:]
		#output.writerow(line)
		if counter > 15:
		   	result=svmclassifiershort.classify(iline)
			print result
			if str('5.0') in str(result):
				counter=0 
				turn()
			if str('6.0') in str(result):
				counter=0
				grasp()
		else: print 'Handle mode'
	    #sleep(0.5)
	    #print 'not blocked'

def turn():
	while True:
	    vector=[]
	    #print "Got here"
	    data = ser.readline()
	    #print "Read line"
	    data = data.split(",")
	    for i in data:
	    	i=i.rstrip("\r\n")
		vector.append(i)
	    if len(vector) > 3:
		line = vector[-6:]
		iline = [int(n) for n in line]
		#print vector[-6:]
		#output.writerow(line)
	   	result=knndir2.knnestimate(knndir2.data,iline)
		print 'Turn mode: ', result
		if 'Up' in result: handle()
	    #sleep(0.5)
	    #print 'not blocked'

grasp()

print "Stopping sensor output"
ser.write("stop all"+"\r\n")
print "Closing serial port" 
ser.close()

