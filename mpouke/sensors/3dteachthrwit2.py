import math
import csv
import serial
from time import sleep

#dataset=csv.reader(open('data.csv'), delimiter=',')

output = csv.writer(open('demo.csv', 'a'), delimiter=',')
port = "/dev/rfcomm1"
ser = serial.Serial(port, baudrate=9600, timeout=10)
#global wholedata[]
#global vectorlist[]
#for row in dataset: print row


print "connecting..."
sleep(2)
ser.write("echo on"+"\r\n")
ser.write("stop all"+"\r\n")
ser.write("sett 114500000"+"\r\n")
ser.write("sens +000005000 10 1 0"+"\r\n")
print ser.portstr 

while True:
    print "****************************************************"
    print "Application for recording stuff, press 1 when ready "
    print "150 samples each"
    print  "****************************************************"
    print "1: Throw, 2: ThrowRight, 3: Grasp, 4: Square 5. blala"
    #dump = ser.readline()
    #print dump
    selection = raw_input()
    #buffer = ser.read(ser.inWaiting())

    if selection == '1':
    	    print "Get ready to record 'Throw' in 3..."
	    sleep(1)
	    print "2..."
	    sleep(1)
	    print "1..."
            sleep(1)
            print "GO!!!"
            buffer = ser.read(ser.inWaiting())
	    ser.flushOutput()
            ser.flushInput()
	    for r in range(256):
		    vector=[]
		    ser.flushOutput()
		    data = ser.readline()
		    data = data.split(",")
		    for i in data:
		    	i=i.rstrip("\r\n")
			vector.append(i)
		    if len(vector) > 3:
			line = vector[-3:]
			iline = [int(n) for n in line]
			iline.append('Throw')
			output.writerow(iline)
			#vectorlist.append(iline)
			#wholedata=vectorcreate()
		   	#result=knntest2.knnestimate(knntest2.data,iline)
			#print result
		   	print iline

    if selection == '2':
    	    print "Get ready to record 'ThrowRight' in 3..."
	    sleep(1)
	    print "2..."
	    sleep(1)
	    print "1..."
            sleep(1)
            print "GO!!!"
            buffer = ser.read(ser.inWaiting())
	    ser.flushOutput()
	    ser.flushInput()
	    for r in range(256):
		    vector=[]
		    ser.flushOutput()
		    data = ser.readline()
		    data = data.split(",")
		    for i in data:
		    	i=i.rstrip("\r\n")
			vector.append(i)
		    if len(vector) > 3:
			line = vector[-3:]
			iline = [int(n) for n in line]
			iline.append('ThrowRight')
			output.writerow(iline)
			#vectorlist.append(iline)
			#wholedata=vectorcreate()
		   	#result=knntest2.knnestimate(knntest2.data,iline)
			#print result
		   	print iline

    if selection == '3':
    	    print "Get ready to record 'Grasp' in 3..."
	    sleep(1)
	    print "2..."
	    sleep(1)
	    print "1..."
            sleep(1)
            print "GO!!!"
            buffer = ser.read(ser.inWaiting())
	    ser.flushOutput()
	    ser.flushInput()
	    for r in range(256):
		    vector=[]
		    ser.flushOutput()
		    data = ser.readline()
		    data = data.split(",")
		    for i in data:
		    	i=i.rstrip("\r\n")
			vector.append(i)
		    if len(vector) > 3:
			line = vector[-3:]
			iline = [int(n) for n in line]
			iline.append('Grasp')
			output.writerow(iline)
			#vectorlist.append(iline)
			#wholedata=vectorcreate()
		   	#result=knntest2.knnestimate(knntest2.data,iline)
			#print result
		   	print iline

    if selection == '4':
    	    print "Get ready to record 'Square' in 3..."
	    sleep(1)
	    print "2..."
	    sleep(1)
	    print "1..."
            sleep(1)
            print "GO!!!"
            buffer = ser.read(ser.inWaiting())
	    ser.flushOutput()
	    ser.flushInput()
	    for r in range(256):
		    vector=[]
		    ser.flushOutput()
		    data = ser.readline()
		    data = data.split(",")
		    for i in data:
		    	i=i.rstrip("\r\n")
			vector.append(i)
		    if len(vector) > 3:
			line = vector[-3:]
			iline = [int(n) for n in line]
			iline.append('Square')
			output.writerow(iline)
			#vectorlist.append(iline)
			#wholedata=vectorcreate()
		   	#result=knntest2.knnestimate(knntest2.data,iline)
			#print result
		   	print iline

    if selection == '5':
    	    print "Get ready to record 'Grasp' in 3..."
	    sleep(1)
	    print "2..."
	    sleep(1)
	    print "1..."
            sleep(1)
            print "GO!!!"
            buffer = ser.read(ser.inWaiting())
	    ser.flushOutput()
	    ser.flushInput()
	    for r in range(256):
		    vector=[]
		    ser.flushOutput()
		    data = ser.readline()
		    data = data.split(",")
		    for i in data:
		    	i=i.rstrip("\r\n")
			vector.append(i)
		    if len(vector) > 3:
			line = vector[-3:]
			iline = [int(n) for n in line]
			iline.append('Grasp')
			output.writerow(iline)
			#vectorlist.append(iline)
			#wholedata=vectorcreate()
		   	#result=knntest2.knnestimate(knntest2.data,iline)
			#print result
		   	print iline



    elif selection == '0':
	    print "Exiting..."
	    break
	    
ser.write("stop all"+"\r\n")
print "Stopping sensor output"
ser.close()
print "Closing serial port connection, sensor light should turn from blue to green"

