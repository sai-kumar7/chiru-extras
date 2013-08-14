import os, sys
import pygame
from pygame.locals import *
import mesh_grid5
import csv
from math import *
import Pedestrian
from collections import Counter, defaultdict
import random
import time
from datetime import date, datetime, timedelta
import odcontainer
from scipy.stats.stats import pearsonr
import numpy as np

w = 1500                 #set width of screen
#h = 864                 #set height
h = 1080
screen = pygame.display.set_mode((w, h)) #make screen
pygame.font.init()
running = 1
global ORIGINX, ORIGINY
global ZOOM
BTCAPTURE = False
RANDOMCAPTURE = False #Remember to se Random mode in Pedestrian class
COMPARISONMODE = False
BTLARGECAPTURE = False
RANDOMLARGECAPTURE = False #Remember to se Random mode in Pedestrian class
AHSREAD = True
AHSWRITE = False
#AHSWALK = False
FOOTPRINTREAD = False
ZOOM = 2
ORIGINX = screen.get_width()/2 #move origin 
ORIGINY = (screen.get_height()-100)/2 #move origin
RADIUS = 150
ROADRADIUS = 75
black = 0, 0, 0
colorscheme = [[255, 255, 217],[237, 248, 217],[199, 233, 180],[127, 205, 187],[65, 182, 196],[29, 145, 192],[34, 94, 168],[37, 52, 148],[8, 29, 88]]
heatscheme = [[255, 255, 217],[237, 248, 217],[199, 233, 180],[127, 205, 187],[65, 182, 196],[29, 145, 192],[34, 94, 168],[37, 52, 148],[8, 29, 88]]
bischeme = [[165, 0, 38],[215, 48, 39],[244, 109, 67],[253, 174, 97],[254, 224, 139],[255, 255, 191],[217, 239, 139],[166, 217, 106],[102, 189, 99],[26, 152, 80],[0, 104, 55]]
colorscheme.reverse()
heatscheme.reverse()


if COMPARISONMODE == True: black = 255, 255, 255 #Setting black background to white
#center=[65.013012,25.472756]
center=[65.012962,25.472815]
nuke=[65.01211,25.47619]
willisika=[65.01085,25.473636]
north=[65.014278,25.473272]
stmichaels=[65.012817,25.474781]
#originweight = {}
#destweight = defaultdict(list)
number_of_agents = 0
oulusize = [[-44,-206],[254,-12],[55,270],[-223,74]]
allists = []
path = []

weekevening = []
weekmorning = []
weeknight = []
weekwork = []
ewevening = []
ewmorning = []
ewnight = []
ewwork = []
sunevening = []
sunmorning = []
sunnight = []
sunwork = []

rweekevening = []
rweekmorning = []
rweeknight = []
rweekwork = []
rewevening = []
rewmorning = []
rewnight = []
rewwork = []
rsunevening = []
rsunmorning = []
rsunnight = []
rsunwork = []

ahsweekevening = []
ahsweekmorning = []
ahsweeknight = []
ahsweekwork = []
ahsewevening = []
ahsewmorning = []
ahsewnight = []
ahsewwork = []
ahssunevening = []
ahssunmorning = []
ahssunnight = []
ahssunwork = []

SINGLECLUSTERS = []
TIMECLUSTERS = []

if FOOTPRINTREAD == True:

    weekeveningrd = csv.reader(open('weekevening.csv'),delimiter=',')
    weekmorningrd = csv.reader(open('weekmorning.csv'),delimiter=',')
    weeknightrd = csv.reader(open('weeknight.csv'),delimiter=',')
    weekworkrd = csv.reader(open('weekwork.csv'),delimiter=',')
    eweveningrd = csv.reader(open('ewevening.csv'),delimiter=',')
    ewmorningrd = csv.reader(open('ewmorning.csv'),delimiter=',')
    ewnightrd = csv.reader(open('ewnight.csv'),delimiter=',')
    ewworkrd = csv.reader(open('ewwork.csv'),delimiter=',')
    suneveningrd = csv.reader(open('sunevening.csv'),delimiter=',')
    sunmorningrd = csv.reader(open('sunmorning.csv'),delimiter=',')
    sunnightrd = csv.reader(open('sunnight.csv'),delimiter=',')
    sunworkrd = csv.reader(open('sunwork.csv'),delimiter=',') 

    rweekeveningrd = csv.reader(open('rweekevening.csv'),delimiter=',')
    rweekmorningrd = csv.reader(open('rweekmorning.csv'),delimiter=',')
    rweeknightrd = csv.reader(open('rweeknight.csv'),delimiter=',')
    rweekworkrd = csv.reader(open('rweekwork.csv'),delimiter=',')
    reweveningrd = csv.reader(open('rewevening.csv'),delimiter=',')
    rewmorningrd = csv.reader(open('rewmorning.csv'),delimiter=',')
    rewnightrd = csv.reader(open('rewnight.csv'),delimiter=',')
    rewworkrd = csv.reader(open('rewwork.csv'),delimiter=',')
    rsuneveningrd = csv.reader(open('rsunevening.csv'),delimiter=',')
    rsunmorningrd = csv.reader(open('rsunmorning.csv'),delimiter=',')
    rsunnightrd = csv.reader(open('rsunnight.csv'),delimiter=',')
    rsunworkrd = csv.reader(open('rsunwork.csv'),delimiter=',')

    ahsweekeveningrd = csv.reader(open('ahsweekevening.csv'),delimiter=',')
    ahsweekmorningrd = csv.reader(open('ahsweekmorning.csv'),delimiter=',')
    ahsweeknightrd = csv.reader(open('ahsweeknight.csv'),delimiter=',')
    ahsweekworkrd = csv.reader(open('ahsweekwork.csv'),delimiter=',')
    ahseweveningrd = csv.reader(open('ahsewevening.csv'),delimiter=',')
    ahsewmorningrd = csv.reader(open('ahsewmorning.csv'),delimiter=',')
    ahsewnightrd = csv.reader(open('ahsewnight.csv'),delimiter=',')
    ahsewworkrd = csv.reader(open('ahsewwork.csv'),delimiter=',')
    ahssuneveningrd = csv.reader(open('ahssunevening.csv'),delimiter=',')
    ahssunmorningrd = csv.reader(open('ahssunmorning.csv'),delimiter=',')
    ahssunnightrd = csv.reader(open('ahssunnight.csv'),delimiter=',')
    ahssunworkrd = csv.reader(open('ahssunwork.csv'),delimiter=',')
 
    for row in ahsweekeveningrd:
        ahsweekevening.append(row)
    for row in ahsweekmorningrd:
        ahsweekmorning.append(row)
    for row in ahsweeknightrd:
        ahsweeknight.append(row)
    for row in ahsweekworkrd:
        ahsweekwork.append(row)
    for row in ahseweveningrd:
        ahsewevening.append(row)
    for row in ahsewmorningrd:
        ahsewmorning.append(row)
    for row in ahsewnightrd:
        ahsewnight.append(row)
    for row in ahsewworkrd:
        ahsewwork.append(row)
    for row in ahssuneveningrd:
        ahssunevening.append(row)
    for row in ahssunmorningrd:
        ahssunmorning.append(row)
    for row in ahssunnightrd:
        ahssunnight.append(row)
    for row in ahssunworkrd:
        ahssunwork.append(row)

    for row in weekeveningrd:
        weekevening.append(row)
    for row in weekmorningrd:
        weekmorning.append(row)
    for row in weeknightrd:
        weeknight.append(row)
    for row in weekworkrd:
        weekwork.append(row)
    for row in eweveningrd:
        ewevening.append(row)
    for row in ewmorningrd:
        ewmorning.append(row)
    for row in ewnightrd:
        ewnight.append(row)
    for row in ewworkrd:
        ewwork.append(row)
    for row in suneveningrd:
        sunevening.append(row)
    for row in sunmorningrd:
        sunmorning.append(row)
    for row in sunnightrd:
        sunnight.append(row)
    for row in sunworkrd:
        sunwork.append(row)

    for row in rweekeveningrd:
        rweekevening.append(row)
    for row in rweekmorningrd:
        rweekmorning.append(row)
    for row in rweeknightrd:
        rweeknight.append(row)
    for row in rweekworkrd:
        rweekwork.append(row)
    for row in reweveningrd:
        rewevening.append(row)
    for row in rewmorningrd:
        rewmorning.append(row)
    for row in rewnightrd:
        rewnight.append(row)
    for row in rewworkrd:
        rewwork.append(row)
    for row in rsuneveningrd:
        rsunevening.append(row)
    for row in rsunmorningrd:
        rsunmorning.append(row)
    for row in rsunnightrd:
        rsunnight.append(row)
    for row in rsunworkrd:
        rsunwork.append(row)


    # SINGLECLUSTERS.append(ahsweekmorning)
    # SINGLECLUSTERS.append(ahsweekwork)
    # SINGLECLUSTERS.append(ahsweekevening)
    # SINGLECLUSTERS.append(ahsweeknight)
    # SINGLECLUSTERS.append(ahsewmorning)
    # SINGLECLUSTERS.append(ahsewwork)
    # SINGLECLUSTERS.append(ahsewevening)
    # SINGLECLUSTERS.append(ahsewnight)
    # SINGLECLUSTERS.append(ahssunmorning)
    # SINGLECLUSTERS.append(ahssunwork)
    # SINGLECLUSTERS.append(ahssunevening)
    # SINGLECLUSTERS.append(ahssunnight)

    # SINGLECLUSTERS.append(weekmorning)
    # SINGLECLUSTERS.append(weekwork)
    # SINGLECLUSTERS.append(weekevening)
    # SINGLECLUSTERS.append(weeknight)
    # SINGLECLUSTERS.append(ewmorning)
    # SINGLECLUSTERS.append(ewwork)
    # SINGLECLUSTERS.append(ewevening)
    # SINGLECLUSTERS.append(ewnight)
    # SINGLECLUSTERS.append(sunmorning)
    # SINGLECLUSTERS.append(sunwork)
    # SINGLECLUSTERS.append(sunevening)
    # SINGLECLUSTERS.append(sunnight)

    SINGLECLUSTERS.append(rweekmorning)
    SINGLECLUSTERS.append(rweekwork)
    SINGLECLUSTERS.append(rweekevening)
    SINGLECLUSTERS.append(rweeknight)
    SINGLECLUSTERS.append(rewmorning)
    SINGLECLUSTERS.append(rewwork)
    SINGLECLUSTERS.append(rewevening)
    SINGLECLUSTERS.append(rewnight)
    SINGLECLUSTERS.append(rsunmorning)
    SINGLECLUSTERS.append(rsunwork)
    SINGLECLUSTERS.append(rsunevening)
    SINGLECLUSTERS.append(rsunnight)



if COMPARISONMODE == True:
    #btvr = open('btvisualweights.csv','r') #Bluetooth wifi testing
    #rvr = open('rvisualweights.csv','r') #Random testing
    # btvr = open('2012-05-0210.csv','r') #Bluetooth wifi testing
    # rvr = open('r2012-05-0210.csv','r') #Random testing
    # btreader = csv.reader(btvr,delimiter=',') #Bluetooth wifi testing
    # rreader = csv.reader(rvr,delimiter=',') #Random testing
    #btvr = open('btvisualweights.csv','r') #Bluetooth wifi testing
    #rvr = open('rvisualweights.csv','r') #Random testing
    #btvr = open('2012-05-0210.csv','r') #Bluetooth wifi testing
    #rvr = open('r2012-05-0210.csv','r') #Random testing
    weekeveningrd = csv.reader(open('weekevening.csv'),delimiter=',')
    weekmorningrd = csv.reader(open('weekmorning.csv'),delimiter=',')
    weeknightrd = csv.reader(open('weeknight.csv'),delimiter=',')
    weekworkrd = csv.reader(open('weekwork.csv'),delimiter=',')
    eweveningrd = csv.reader(open('ewevening.csv'),delimiter=',')
    ewmorningrd = csv.reader(open('ewmorning.csv'),delimiter=',')
    ewnightrd = csv.reader(open('ewnight.csv'),delimiter=',')
    ewworkrd = csv.reader(open('ewwork.csv'),delimiter=',')
    suneveningrd = csv.reader(open('sunevening.csv'),delimiter=',')
    sunmorningrd = csv.reader(open('sunmorning.csv'),delimiter=',')
    sunnightrd = csv.reader(open('sunnight.csv'),delimiter=',')
    sunworkrd = csv.reader(open('sunwork.csv'),delimiter=',') 

    rweekeveningrd = csv.reader(open('rweekevening.csv'),delimiter=',')
    rweekmorningrd = csv.reader(open('rweekmorning.csv'),delimiter=',')
    rweeknightrd = csv.reader(open('rweeknight.csv'),delimiter=',')
    rweekworkrd = csv.reader(open('rweekwork.csv'),delimiter=',')
    reweveningrd = csv.reader(open('rewevening.csv'),delimiter=',')
    rewmorningrd = csv.reader(open('rewmorning.csv'),delimiter=',')
    rewnightrd = csv.reader(open('rewnight.csv'),delimiter=',')
    rewworkrd = csv.reader(open('rewwork.csv'),delimiter=',')
    rsuneveningrd = csv.reader(open('rsunevening.csv'),delimiter=',')
    rsunmorningrd = csv.reader(open('rsunmorning.csv'),delimiter=',')
    rsunnightrd = csv.reader(open('rsunnight.csv'),delimiter=',')
    rsunworkrd = csv.reader(open('rsunwork.csv'),delimiter=',')

    ahsweekeveningrd = csv.reader(open('ahsweekevening.csv'),delimiter=',')
    ahsweekmorningrd = csv.reader(open('ahsweekmorning.csv'),delimiter=',')
    ahsweeknightrd = csv.reader(open('ahsweeknight.csv'),delimiter=',')
    ahsweekworkrd = csv.reader(open('ahsweekwork.csv'),delimiter=',')
    ahseweveningrd = csv.reader(open('ahsewevening.csv'),delimiter=',')
    ahsewmorningrd = csv.reader(open('ahsewmorning.csv'),delimiter=',')
    ahsewnightrd = csv.reader(open('ahsewnight.csv'),delimiter=',')
    ahsewworkrd = csv.reader(open('ahsewwork.csv'),delimiter=',')
    ahssuneveningrd = csv.reader(open('ahssunevening.csv'),delimiter=',')
    ahssunmorningrd = csv.reader(open('ahssunmorning.csv'),delimiter=',')
    ahssunnightrd = csv.reader(open('ahssunnight.csv'),delimiter=',')
    ahssunworkrd = csv.reader(open('ahssunwork.csv'),delimiter=',')

    for row in weekeveningrd:
        weekevening.append(row)
    for row in weekmorningrd:
        weekmorning.append(row)
    for row in weeknightrd:
        weeknight.append(row)
    for row in weekworkrd:
        weekwork.append(row)
    for row in eweveningrd:
        ewevening.append(row)
    for row in ewmorningrd:
        ewmorning.append(row)
    for row in ewnightrd:
        ewnight.append(row)
    for row in ewworkrd:
        ewwork.append(row)
    for row in suneveningrd:
        sunevening.append(row)
    for row in sunmorningrd:
        sunmorning.append(row)
    for row in sunnightrd:
        sunnight.append(row)
    for row in sunworkrd:
        sunwork.append(row)

    for row in rweekeveningrd:
        rweekevening.append(row)
    for row in rweekmorningrd:
        rweekmorning.append(row)
    for row in rweeknightrd:
        rweeknight.append(row)
    for row in rweekworkrd:
        rweekwork.append(row)
    for row in reweveningrd:
        rewevening.append(row)
    for row in rewmorningrd:
        rewmorning.append(row)
    for row in rewnightrd:
        rewnight.append(row)
    for row in rewworkrd:
        rewwork.append(row)
    for row in rsuneveningrd:
        rsunevening.append(row)
    for row in rsunmorningrd:
        rsunmorning.append(row)
    for row in rsunnightrd:
        rsunnight.append(row)
    for row in rsunworkrd:
        rsunwork.append(row)

    for row in ahsweekeveningrd:
        ahsweekevening.append(row)
    for row in ahsweekmorningrd:
        ahsweekmorning.append(row)
    for row in ahsweeknightrd:
        ahsweeknight.append(row)
    for row in ahsweekworkrd:
        ahsweekwork.append(row)
    for row in ahseweveningrd:
        ahsewevening.append(row)
    for row in ahsewmorningrd:
        ahsewmorning.append(row)
    for row in ahsewnightrd:
        ahsewnight.append(row)
    for row in ahsewworkrd:
        ahsewwork.append(row)
    for row in ahssuneveningrd:
        ahssunevening.append(row)
    for row in ahssunmorningrd:
        ahssunmorning.append(row)
    for row in ahssunnightrd:
        ahssunnight.append(row)
    for row in ahssunworkrd:
        ahssunwork.append(row)


    TIMECLUSTERS.append([weekmorning,rweekmorning])
    TIMECLUSTERS.append([weekwork,rweekwork])
    TIMECLUSTERS.append([weekevening,rweekevening])
    TIMECLUSTERS.append([weeknight,rweeknight])
    TIMECLUSTERS.append([ewmorning,rewmorning])
    TIMECLUSTERS.append([ewwork,rewwork])
    TIMECLUSTERS.append([ewevening,rewevening])
    TIMECLUSTERS.append([ewnight,rewnight])
    TIMECLUSTERS.append([sunmorning,rsunmorning])
    TIMECLUSTERS.append([sunwork,rsunwork])
    TIMECLUSTERS.append([sunevening,rsunevening])
    TIMECLUSTERS.append([sunnight,rsunnight])

    # TIMECLUSTERS.append([weekmorning,ahsweekmorning])
    # TIMECLUSTERS.append([weekwork,ahsweekwork])
    # TIMECLUSTERS.append([weekevening,ahsweekevening])
    # TIMECLUSTERS.append([weeknight,ahsweeknight])
    # TIMECLUSTERS.append([ewmorning,ahsewmorning])
    # TIMECLUSTERS.append([ewwork,ahsewwork])
    # TIMECLUSTERS.append([ewevening,ahsewevening])
    # TIMECLUSTERS.append([ewnight,ahsewnight])
    # TIMECLUSTERS.append([sunmorning,ahssunmorning])
    # TIMECLUSTERS.append([sunwork,ahssunwork])
    # TIMECLUSTERS.append([sunevening,ahssunevening])
    # TIMECLUSTERS.append([sunnight,ahssunnight])

if AHSWRITE == True:
    ahswriter = csv.writer(open('aweightsw.csv','w'),delimiter=',')

artificial_hotspots = defaultdict(list)

if AHSREAD == True:
    ahsreader = csv.reader(open('aweights.csv','r'),delimiter=',')
    for row in ahsreader:
        artificial_hotspots[int(row[0])]=[int(row[1]),[int(row[2]),int(row[3])],int(row[4])]

aorigins = defaultdict(list)
ATYPEWEIGHTS = [[1,1],[2,1],[3,1],[4,1]]

#if AHSWALK == True:
   #for key,value in artificial_hotspots.iteritems()

def pick_with_type(atype):
    coordlist = []
    for ah in artificial_hotspots:
        if artificial_hotspots[ah][0] == atype: coordlist.append(artificial_hotspots[ah][1])
    return random.choice(coordlist)

def calculate_atypes():
    #omin = min(origins, key=origins.get)
    #omax = max(origins, key=origins.get)
    #print omin
    #print omax
    #minvalue = origins[omin]
    #maxvalue = origins[omax]
    #print 'min: ',minvalue
    #print 'max: ',maxvalue
    #x = locdict[o][0]
    #y = locdict[o][1]
    #print "x: ",x
    #print "y: ",y
    #ishift = origins[o]-minvalue
    # y = 1 + (x-A)*(10-1)/(B-A)
    #intensity = ishift*(255/(maxvalue-minvalue))
    #intensity = ishift*8/(maxvalue-minvalue)
    if not artificial_hotspots: return
    if len(artificial_hotspots) < 4: return

    input = [artificial_hotspots[a][2]*-1 for a in artificial_hotspots]
    #print input
    minvalue = min(input)
    maxvalue = max(input)
    output = []
    for i in input:
        shift = i-minvalue
        newvalue = shift*10/(maxvalue-minvalue)
        output.append(newvalue)
    #output = [int((n - old_min) / old_range * new_range + new_min) for n in input]
    type1list = []
    type2list = []
    type3list = []
    type4list = []
    for r in range(len(output)):
        if artificial_hotspots[r][0] == 1: type1list.append(output[r])
        if artificial_hotspots[r][0] == 2: type2list.append(output[r])
        if artificial_hotspots[r][0] == 3: type3list.append(output[r])
        if artificial_hotspots[r][0] == 4: type4list.append(output[r])
    #print 'typelists ******************* '
    #print type1list
    #print type2list
    #print type3list
    #print type4list

    ATYPEWEIGHTS[0] = [1,sum(type1list)/len(type1list)]
    ATYPEWEIGHTS[1] = [2,sum(type2list)/len(type2list)]
    ATYPEWEIGHTS[2] = [3,sum(type3list)/len(type3list)]
    ATYPEWEIGHTS[3] = [4,sum(type4list)/len(type4list)]
    #for p in pedestrians: p.aorigins = ATYPEWEIGHTS
    #print ATYPEWEIGHTS

def qmean(num):
	return sqrt(sum(float(n)*float(n) for n in num)/float(len(num)))

total_errors = [] 
t1error = []
t2error = []
t3error = []
t4error = []

def reload_artificial_weights():
    #key = len(artificial_hotspots)
    #artificial_hotspots[key].append(selection)
    #artificial_hotspots[key].append([xpos,ypos])
    #hsnodes = []
    #abserror = [] 
    relation1 = []
    relation2 = []
    t1r = [] #ground truth model
    t2r = [] #ground truth model
    t3r = [] #ground truth model
    t4r = [] #ground truth model
    t1rm = [] #model to compare against
    t2rm = [] #model to compare against
    t3rm = [] #model to compare against
    t4rm = [] #model to compare against
    #t1abs = [] #Absolute error of the model
    #t2abs = [] #Absolute error of the model
    #t3abs = [] #Absolute error of the model
    #t4abs = [] #Absolute error of the model


    hotspot_error = []
    t1 = []
    t2 = []
    t3 = []
    t4 = []
    dl = []
    for a in artificial_hotspots:
        ahsweights = []
        #print wat
        for r in range(len(mesh_grid5.nodes)):
            rad = RADIUS
            if artificial_hotspots[a][0] == 4: rad = ROADRADIUS
            if (mesh_grid5.nodes[r].x-artificial_hotspots[a][1][0])**2 + (mesh_grid5.nodes[r].y - artificial_hotspots[a][1][1])**2 < rad**2:
               relation1.append(rel1[r])
               relation2.append(rel2[r])
               #print 'testing',rel2[r]-rel1[r]
               #print 'testing2',comparisondict[r]
               ahsweights.append(comparisondict[r])
               artificial_hotspots[a][2] = (sum(ahsweights)/len(ahsweights))
               aorigins[a]=[artificial_hotspots[a][0],artificial_hotspots[a][1]]
               hotspot_error.append(abs(float((artificial_hotspots[a][2]))))

               if artificial_hotspots[a][0] == 1: t1.append(artificial_hotspots[a][2])
               if artificial_hotspots[a][0] == 2: t2.append(artificial_hotspots[a][2])
               if artificial_hotspots[a][0] == 3: t3.append(artificial_hotspots[a][2])
               if artificial_hotspots[a][0] == 4: t4.append(artificial_hotspots[a][2])

               #if artificial_hotspots[a][0] == 1: t1abs.append(abs(float((artificial_hotspots[a][2]))))
               #if artificial_hotspots[a][0] == 2: t2abs.append(abs(float((artificial_hotspots[a][2]))))
               #if artificial_hotspots[a][0] == 3: t3abs.append(abs(float((artificial_hotspots[a][2]))))
               #if artificial_hotspots[a][0] == 4: t4abs.append(abs(float((artificial_hotspots[a][2]))))


               if artificial_hotspots[a][0] == 1: 
                   t1r.append(rel1[r])
                   t1rm.append(rel2[r])
               if artificial_hotspots[a][0] == 2: 
                   t2r.append(rel1[r])
                   t2rm.append(rel2[r])                   
               if artificial_hotspots[a][0] == 3: 
                   t3r.append(rel1[r])
                   t3rm.append(rel2[r])
               if artificial_hotspots[a][0] == 4: 
                   t4r.append(rel1[r])
                   t4rm.append(rel2[r])

        #print 'Artificial hotspot: type,location,average error: ',a,artificial_hotspots[a]
        #if artificial_hotspots[a][0] != 3: dl.append([vdistsqr([0,0],artificial_hotspots[a][1]),abs(artificial_hotspots[a][2])])
        dl.append([vdistsqr([0,0],artificial_hotspots[a][1]),abs(artificial_hotspots[a][2])])
            #print 'Artificial hotspot type ',selection,' inserted'
            #for a in artificial_hotspots:
            #print artificial_hotspots[a]
    dl.sort()
    ds = [d[0]for d in dl]
    es = [d[1]for d in dl]
    std = []
    ste = []
    for f in ds:
        f = f-np.mean(ds)
        #print f
        f = f/np.std(ds)
        #print f
        #print '****'
        std.append(f)
    for f in es:
        f = f-np.mean(es)
        #print f
        f = f/np.std(es)
        #print f
        #print '****'
        ste.append(f)
    #for x,y in zip(
    #for f in dl: print f
    # print 'Total number of ground truth footsteps',sum(relation1)
    # print 'Total number of model footsteps',sum(relation2)
    # print 'Relation between model and ground truth',float(sum(relation2))/float(sum(relation1))
    # print 'correlation between distance and error in all hotspots',pearsonr(std,ste)
    print 'Average error inside hotspot locations: ',sum(hotspot_error)/len(hotspot_error)
    print ''
    # print 'Type 1 total hotspot error: ', sum(t1)
    # print 'Type 2 total hotspot error: ', sum(t2)
    # print 'Type 3 total hotspot error: ', sum(t3)
    # print 'Type 4 total hotspot error: ', sum(t4)
    #print 'Type 1 relation between model and ground truth: ',float(sum(t1rm))/float(sum(t1r))
    #print 'Type 2 relation between model and ground truth: ',float(sum(t2rm))/float(sum(t2r))
    #print 'Type 3 relation between model and ground truth: ',float(sum(t3rm))/float(sum(t3r))
    #print 'Type 4 relation between model and ground truth: ',float(sum(t4rm))/float(sum(t4r))
    #print sum(hotspot_error),sum(relation1)
    print ''
    #print 'Quadratic mean of t1 total error ',qmean(t1r),'quadratic mean of ground truth model',qmean(t1)
    print 'Relationship between quadratic error in all hotspots and ground truth at all hotspots',qmean(hotspot_error)/qmean(relation1)
    print 'Type 1 relation between model and ground truth: ',qmean(t1r)/qmean(t1)
    print 'Type 2 relation between model and ground truth: ',qmean(t2r)/qmean(t2)
    print 'Type 3 relation between model and ground truth: ',qmean(t3r)/qmean(t3)
    print 'Type 4 relation between model and ground truth: ',qmean(t4r)/qmean(t3)

    total_errors.append(qmean(hotspot_error)/qmean(relation1)) 
    t1error.append(qmean(t1r)/qmean(t1))
    t2error.append(qmean(t2r)/qmean(t2))
    t3error.append(qmean(t3r)/qmean(t3))
    t4error.append(qmean(t4r)/qmean(t4))

    print total_errors
    print t1error
    print t2error
    print t3error
    print t4error
    #print 'Relation between model absolute error and ground truth',float(sum(relation1))/float(sum(hotspot_error))
    #print 'Type 1 relation between model abs error and ground truth: ',float(sum(t1abs))/float(sum(t1r))
    #print 'Type 2 relation between model abs error and ground truth: ',float(sum(t2abs))/float(sum(t2r))
    #print 'Type 3 relation between model abs error and ground truth: ',float(sum(t3abs))/float(sum(t3r))
    #print 'Type 4 relation between model abs error and ground truth: ',float(sum(t4abs))/float(sum(t4r))

def point_inside_polygon(x,y,poly):

    n = len(poly)
    inside = False
    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

def gpsToTundra(lat, lon):
    deltalat = center[0]-lat
    deltalon = center[1]-lon
    dispnorth = 1000*(deltalat*111.28)
    dispeast = -1000*(111.28*deltalon*cos(radians(lat)))
    return [dispeast,dispnorth]

def gps_raw(coord):
    tundralist=[]
    for c in coord:
         #print c
         tundralist.append(gpsToTundra(float(c[0]),float(c[1])))
    return tundralist

def loadOBJ(filename):  
    numVerts = 0  
    verts = []  
    faces = []  
    vertsOut = []  
    facesOut = []  
    for line in open(filename, "r"):  
        vals = line.split()  
        if vals[0] == "v":  
            v = map(float, vals[1:4])  
            verts.append(v)  
        #if vals[0] == "vn":  
        #    n = map(float, vals[1:4])  
        #    norms.append(n)  
        if vals[0] == "f":  
            for f in vals[1:]:  
                w = f.split()  
                # OBJ Files are 1-indexed so we must subtract 1 below  
                vertsOut.append(list(verts[int(w[0])-1]))  
                #normsOut.append(list(norms[int(w[2])-1]))  
                numVerts += 1  
    #return vertsOut, facesOut
    return vertsOut

def group(lst, n):
    return zip(*[lst[i::n] for i in range(n)])

def findCentroid2D(v1,v2,v3):
    x = (v1[0]+v2[0]+v3[0])/3
    y = (v1[1]+v2[1]+v3[1])/3
    #z = (v1[2]+v2[2]+v3[2])/3
    return(x,y)

def vdistsqr(a, b):
    x = b[0] - a[0] 
    y = b[1] - a[1]
    return sqrt(x * x + y * y)

def vequal(a, b):
    return vdistsqr(a, b) < (0.001 * 0.001)

vertlist = loadOBJ("largerdec.obj")

nodes = group(vertlist,3)
xynodes = []

def check_node(a):
    for n in xynodes:
        if point_inside_polygon(a[0],a[1],n):
            #print "Found"
            return True
    return False

def corner_side(a,b,c):
    # Check if point A lies left or right of the apex C
    ax = a[0]
    bx = b[0]
    ay = a[1]
    by = b[1]
    cx = c[0]
    cy = c[1]
    middlex = (ax+bx)/2
    middley = (ay+by)/2
    return ((middlex - cx)*(ay - cy) - (middley - cy)*(ax - cx)) > 0

for i in nodes:
    newnode=[]
    for v in i:
        xyvertex=[]
        xyvertex.append(v[0])
        xyvertex.append(v[2])
        newnode.append(xyvertex)
    xynodes.append(newnode)

rel1 = {}
rel2 = {}
comparisondict = {}
def comparisonchange(r1,r2):
    if COMPARISONMODE == True:
        for x,y in zip(r1,r2):
            #print x,y
            comparisondict[int(x[0])]=int(y[1])-int(x[1])
            rel1[int(x[0])]=(int(x[1]))
            rel2[int(x[0])]=(int(y[1]))
    avgdifference = []
    avgoutside = []
    for r in range(len(mesh_grid5.coords)):#HOLDON
        avgoutside.append(abs(float(comparisondict[r])))
        #print r,' outside hotspot', abs(float(comparisondict[r])), 'appended'
        for a in artificial_hotspots:
            rad = RADIUS
            if artificial_hotspots[0] == 4: rad = ROADRADIUS
            if (mesh_grid5.nodes[r].x-artificial_hotspots[a][1][0])**2 + (mesh_grid5.nodes[r].y - artificial_hotspots[a][1][1])**2 < rad**2:
                avgoutside[r]=0.0
                #print r,' inside hotspot. Node ',r,'is',avgoutside[r]
                #continue
        

        avgdifference.append(abs(float(comparisondict[r])))
    print len(avgoutside)
    print 'Average difference: ',sum(avgdifference)/len(avgdifference)
    print 'Average difference outside hotspots: ',sum(avgoutside)/len(avgoutside)

#print 'Comparisondict should be coming out now'
#for key, value in comparisondict.iteritems(): print key,value
#print 'Well did it?'


nodevisual = {}
for node in range(len(xynodes)):
    nodevisual[node]=0

def load_nodevisual(cluster):
    for r in range(len(SINGLECLUSTERS[cluster])):
        #print 'node:',r
        nodevisual[r] = int(SINGLECLUSTERS[cluster][r][1])
        #print SINGLECLUSTERS[cluster][r][1]
    #for key,value in nodevisual.iteritems():
        #print key,value

def draw_map():
    #COMPARISONMODE = False
    if COMPARISONMODE == True:
        for n in xrange(len(xynodes)):
            intnode = []
            for i in xynodes[n]:
                intnode.append([int(i[0])*ZOOM+ORIGINX,int(i[1])*ZOOM+ORIGINY])
            #print intnode
            #pygame.draw.circle(screen, (0, 255, 0), (int(n[0]), int(n[1])), 1)
            #if comparisondict[n] == 0: pygame.draw.polygon(screen, (100, 100,100), intnode, 1)
            # if comparisondict[n] > 0 and comparisondict[n] <= 4: pygame.draw.polygon(screen, heatscheme[0], intnode, 0)
            # if comparisondict[n] > 4 and comparisondict[n] <= 8: pygame.draw.polygon(screen, heatscheme[1], intnode, 0)
            # if comparisondict[n] > 8 and comparisondict[n] <= 12: pygame.draw.polygon(screen, heatscheme[2], intnode, 0)
            # if comparisondict[n] > 12 and comparisondict[n] <= 16: pygame.draw.polygon(screen, heatscheme[3], intnode, 0)
            # if comparisondict[n] > 16 and comparisondict[n] <= 20: pygame.draw.polygon(screen, heatscheme[4], intnode, 0)
            # if comparisondict[n] > 20 and comparisondict[n] <= 24: pygame.draw.polygon(screen, heatscheme[5], intnode, 0)
            # if comparisondict[n] > 24 and comparisondict[n] <= 30: pygame.draw.polygon(screen, heatscheme[6], intnode, 0)
            if comparisondict[n] < -100: pygame.draw.polygon(screen, bischeme[0], intnode, 0)
            if comparisondict[n] > -100 and comparisondict[n] <= -80: pygame.draw.polygon(screen, bischeme[1], intnode, 0)
            if comparisondict[n] > -80 and comparisondict[n] <= -60: pygame.draw.polygon(screen, bischeme[2], intnode, 0)
            if comparisondict[n] > -60 and comparisondict[n] <= -40: pygame.draw.polygon(screen, bischeme[3], intnode, 0)
            if comparisondict[n] > -40 and comparisondict[n] <= -20: pygame.draw.polygon(screen, bischeme[4], intnode, 0)
            if comparisondict[n] > -20 and comparisondict[n] < 0: pygame.draw.polygon(screen, bischeme[5], intnode, 0)
            if comparisondict[n] > 0 and comparisondict[n] <= 20: pygame.draw.polygon(screen, bischeme[6], intnode, 0)
            if comparisondict[n] > 20 and comparisondict[n] <= 40: pygame.draw.polygon(screen, bischeme[7], intnode, 0)
            if comparisondict[n] > 40 and comparisondict[n] <= 60: pygame.draw.polygon(screen, bischeme[8], intnode, 0)
            if comparisondict[n] > 60 and comparisondict[n] <= 80: pygame.draw.polygon(screen, bischeme[9], intnode, 0)
            if comparisondict[n] > 80: pygame.draw.polygon(screen, bischeme[10], intnode, 0)

            #if comparisondict[n] > 30: pygame.draw.polygon(screen, heatscheme[7], intnode, 0)
            pygame.draw.polygon(screen, (100, 100,100), intnode, 1)

    else:
        for n in xrange(len(xynodes)):
            intnode = []
            for i in xynodes[n]:
                intnode.append([int(i[0])*ZOOM+ORIGINX,int(i[1])*ZOOM+ORIGINY])
            #print n,':',nodevisual[n]
            #print intnode
            #pygame.draw.circle(screen, (0, 255, 0), (int(n[0]), int(n[1])), 1)
            #if nodevisual[n] == 0: pygame.draw.polygon(screen, (100, 100,100), intnode, 1)
            # if nodevisual[n] > 0 and nodevisual[n] <= 4: pygame.draw.polygon(screen, heatscheme[0], intnode, 0)
            # if nodevisual[n] > 4 and nodevisual[n] <= 8: pygame.draw.polygon(screen, heatscheme[1], intnode, 0)
            # if nodevisual[n] > 8 and nodevisual[n] <= 12: pygame.draw.polygon(screen, heatscheme[2], intnode, 0)
            # if nodevisual[n] > 12 and nodevisual[n] <= 16: pygame.draw.polygon(screen, heatscheme[3], intnode, 0)
            # if nodevisual[n] > 16 and nodevisual[n] <= 20: pygame.draw.polygon(screen, heatscheme[4], intnode, 0)
            # if nodevisual[n] > 20 and nodevisual[n] <= 24: pygame.draw.polygon(screen, heatscheme[5], intnode, 0)
            # if nodevisual[n] > 24 and nodevisual[n] <= 30: pygame.draw.polygon(screen, heatscheme[6], intnode, 0)
            if nodevisual[n] > 0 and nodevisual[n] <= 10: pygame.draw.polygon(screen, heatscheme[0], intnode, 0)
            if nodevisual[n] > 10 and nodevisual[n] <= 20: pygame.draw.polygon(screen, heatscheme[1], intnode, 0)
            if nodevisual[n] > 20 and nodevisual[n] <= 30: pygame.draw.polygon(screen, heatscheme[2], intnode, 0)
            if nodevisual[n] > 30 and nodevisual[n] <= 40: pygame.draw.polygon(screen, heatscheme[3], intnode, 0)
            if nodevisual[n] > 40 and nodevisual[n] <= 60: pygame.draw.polygon(screen, heatscheme[4], intnode, 0)
            if nodevisual[n] > 60 and nodevisual[n] <= 80: pygame.draw.polygon(screen, heatscheme[5], intnode, 0)
            if nodevisual[n] > 80 and nodevisual[n] <= 100: pygame.draw.polygon(screen, heatscheme[6], intnode, 0)
            if nodevisual[n] > 100 and nodevisual[n] <= 120: pygame.draw.polygon(screen, heatscheme[7], intnode, 0)
            if nodevisual[n] > 120: pygame.draw.polygon(screen, heatscheme[8], intnode, 0)
            #print nodevisual[n]
            #if nodevisual[n] > 30: pygame.draw.polygon(screen, heatscheme[7], intnode, 0)
            pygame.draw.polygon(screen, (100, 100,100), intnode, 1)
        #pygame.display.flip()

def find_closest(a):
    distances = []
    for b in mesh_grid5.coords: 
        distances.append(vdistsqr(a, b))
    smallest = min(distances)
    return distances.index(smallest)

def find_closest_from_list(a,l):
    #print 'This is current:', a
    #print 'This is the list of closest', l
    distances = []
    coordinates = []
    for b in l:
        bc = mesh_grid5.coords[b]
        distances.append(vdistsqr(a, bc))
        coordinates.append(bc)
    smallest = min(distances)
    closest = coordinates[distances.index(smallest)]
    return closest

import heapq

def find_n_closest(a,n):
    distances = []
    nclosest = []
    for b in mesh_grid5.coords: 
        distances.append(vdistsqr(a, b))    
    nlesser_items = heapq.nsmallest(n, distances)
    for i in nlesser_items:
        nclosest.append(distances.index(i))
    return nclosest

    #sdist = distances.sort()
    #return distances[0:n]

#MODIFIED VERSION
def find_n_closest_w_distance(a,n,hs_type=1):
    limit = RADIUS
    if hs_type == 4: limit = ROADRADIUS
    distances = []
    nclosest = []
    underdistance = []
    for r in range(len(mesh_grid5.coords)):
        d = vdistsqr(a, mesh_grid5.coords[r])
        if d < limit:
            underdistance.append(r)    
    #nlesser_items = heapq.nsmallest(n, distances)
    #for i in nlesser_items:
        #nclosest.append(distances.index(i))
    #return nclosest
    return underdistance

    #sdist = distances.sort()
    #return distances[0:n]


def triarea(a,b,c):
    ax = b[0] - a[0]
    ay = b[1] - a[1]
    bx = c[0] - a[0]
    by = c[1] - a[1]
    return bx * ay - ax * by

def string_pull(route,portals):
    #apexindex = 0
    points=[]
    centerindex = 0
    leftIndex = 0
    rightIndex = 0
    apexIndex = 0
    portalApex = route[0]
    points.append(portalApex)
    i = 0
    if len(route) == 1: 
        #print "Short route, no funneling"
        return route
    if len(portals) == 0: print "Portal warning!",route
    isleft = corner_side(portals[0][0],portals[0][1],portalApex)
    if isleft:
        portalLeft = portals[0][0]
        portalRight = portals[0][1]
    else:
        portalLeft = portals[0][1]
        portalRight = portals[0][0]
    
    #currentfunnel = triarea(apex,currentleft,currentright)
    while i <= len(portals)-1:
    #for p in portals:
        p1 = portals[i][0]
        p2 = portals[i][1]
        c = route[i]
        #p1 = p[0]
        #p2 = p[1]
        #c = route[portals.index(p)]
        isleft = corner_side(p1,p2,c)
        if isleft:
            left = p1
            right = p2
        else:
            left = p2
            right = p1

        #Update right vertex.
        if triarea(portalApex, portalRight, right) <= 0.0:
            if vequal(portalApex, portalRight) or triarea(portalApex, portalLeft, right) > 0.0:
                #Tighten the funnel.
                portalRight = right
                rightIndex = i
            else:
                #Right over left, insert left to path and restart scan from portal left point.
                points.append(portalLeft)
                #Make current left the new apex.
                portalApex = portalLeft
                apexIndex = leftIndex
                #Reset portal
                portalLeft = portalApex
                portalRight = portalApex
                leftIndex = apexIndex
                rightIndex = apexIndex
                #Restart scan
                i = apexIndex
                #continue

        #Update left vertex.
        if triarea(portalApex, portalLeft, left) >= 0.0:
            if vequal(portalApex, portalLeft) or triarea(portalApex, portalRight, left) < 0.0:
                #Tighten the funnel.
                portalLeft = left
                leftIndex = i
            else:
                #Left over right, insert right to path and restart scan from portal right point.
                points.append(portalRight)
                #Make current right the new apex.
                portalApex = portalRight
                apexIndex = rightIndex
                #Reset portal
                portalLeft = portalApex
                portalRight = portalApex
                leftIndex = apexIndex
                rightIndex = apexIndex
                #Restart scan
                i = apexIndex
                #continue

        i = i+1

    points.append(route[-1])
    return points

        #newfunnel1 = triarea(apex,left,currentright)
        #newfunnel2 = triarea(apex,left,currentright)
        #if newfunnel < currentfunnel and newfunnel >0:
        #    leftindex = leftindex + 1
        #    currentleft = portals[leftindex][0]


        #funnel = triarea(left,right,apex)

def knn(point,points,k=12):
    avgx = 0.0
    avgy = 0.0
    dlist = []
    closest = []    
    for p in points:
        dlist.append([vdistsqr(point,[float(p[0]),float(p[1])]),points.index(p)])
    dlist.sort(key = lambda x: x[0])
    for f in range(k):
        #print f
        #print dlist[f]
        closest.append(points[dlist[f][1]])
    for c in closest:
        #print c[0]
        avgx += float(c[0])
        avgy += float(c[1])
    avgx = avgx/k 
    avgy = avgy/k
    avg=[avgx,avgy]
    return avg
            
def create_route(source,destination):
    a = mesh_grid5.find_node(source)
    b = mesh_grid5.find_node(destination)
    route = mesh_grid5.search_path(a,b)
    edges = mesh_grid5.search_portals(a,b)
    funnelpoints = string_pull(route,edges)
    return funnelpoints

def weighted_choice(choices):
   #print choices
   total = sum(w for c,w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto+w > r:
         return c
      upto += w
   assert False, "Shouldn't get here"

def fuzzy_destination(destination):
    #fuzzylist = find_n_closest(destination,10)
    fuzzylist = find_n_closest_w_distance(destination,50)
    rc = random.choice(fuzzylist)
    #print "Fuzzy destination", random.choice(fuzzylist)
    return rc

def pick_first(origins):
    #origins = odmatrix.get_origins()
    locdict = odmatrix.get_all_locations()
    #print origins
    #print locdict
    locindex = weighted_choice(origins.items())
    target = locdict[int(locindex)]
    return locindex,fuzzy_destination(target)

def pick_second(current,od):
    #global destweight
    #print "whatta",current
    #print od
    #print od[str(current)]
    locdict = odmatrix.get_all_locations()
    locindex = weighted_choice(od[str(current)])
    target = locdict[int(locindex)]
    return locindex,fuzzy_destination(target)

spotroutes = []

def draw_route():
    tlist = gps_raw(gpslist)
    #a = 231
    a = mesh_grid5.random_target()
    b = mesh_grid5.random_target()
    #b = 1044
    anode = xynodes[a]
    bnode = xynodes[b]
    acoord = findCentroid2D(anode[0],anode[1],anode[2])
    bcoord = findCentroid2D(bnode[0],bnode[1],bnode[2])
    nuclear = gpsToTundra(nuke[0],nuke[1])
    sm = gpsToTundra(stmichaels[0],stmichaels[1])
    #print acoord,bcoord
    pygame.draw.circle(screen, (255, 0, 0), (int(acoord[0])*ZOOM+ORIGINX, int(acoord[1])*ZOOM+ORIGINY), 4)
    pygame.draw.circle(screen, (0, 255, 100), (int(bcoord[0])*ZOOM+ORIGINX, int(bcoord[1])*ZOOM+ORIGINY), 4)
    pygame.draw.circle(screen, (255, 255, 255), (int(sm[0])*ZOOM+ORIGINX, int(sm[1])*ZOOM+ORIGINY), 4)
    pygame.draw.circle(screen, (255, 255, 255), (int(nuclear[0])*ZOOM+ORIGINX, int(nuclear[1])*ZOOM+ORIGINY), 4)
    route = mesh_grid5.search_path(a,b)
    edges = mesh_grid5.search_portals(a,b)
    pygame.display.flip()
    if route:
        path = []
        funnelpoints = string_pull(route,edges)
        #print funnelpoints
        for f in funnelpoints:
            px = f[0]*ZOOM+ORIGINX
            py = f[1]*ZOOM+ORIGINY
            path.append([px,py])
        pygame.draw.lines(screen, (0, 255, 0), False, path, 2)
        for f in funnelpoints:
            pygame.draw.circle(screen, (0, 255, 100), (int(f[0])*ZOOM+ORIGINX, int(f[1])*ZOOM+ORIGINY), 4)
           
        #for r in route:
            #pygame.draw.circle(screen, (0, 255, 100), (int(r[0])*ZOOM+ORIGINX, int(r[1])*ZOOM+ORIGINY), 3)
    if tlist:
        for t in tlist:
            if not check_node(t):
                b = [0,0]
                b[0], b[1] = t[1], t[0]
                #print "What happens: ",t
                c = mesh_grid5.coords[find_closest(b)]
                pygame.draw.circle(screen, (255, 255, 255), (int(c[0])*ZOOM+ORIGINX, int(c[1])*ZOOM+ORIGINY), 3)
                pygame.draw.circle(screen, (100, 100, 100), (int(t[0])*ZOOM+ORIGINX, int(t[1])*ZOOM+ORIGINY), 3)
            #print "wat"
            #print t[0],t[1]
            else:
                pygame.draw.circle(screen, (50, 255, 50), (int(t[0])*ZOOM+ORIGINX, int(t[1])*ZOOM+ORIGINY), 3)
    if edges:
        for e in edges:
            e1 = e[0]
            e2 = e[1]
            c = route[edges.index(e)]
            isleft = corner_side(e1,e2,c)
            if isleft:
                left = e1
                right = e2
            else:
                left = e2
                right = e1

            pygame.draw.circle(screen, (255, 255, 255), (int(left[0])*ZOOM+ORIGINX, int(left[1])*ZOOM+ORIGINY), 2)
            pygame.draw.circle(screen, (100, 100, 255), (int(right[0])*ZOOM+ORIGINX, int(right[1])*ZOOM+ORIGINY), 2)     
            #pygame.draw.circle(screen, (255, 255, 255), (int(e[0][0])*ZOOM+ORIGINX, int(e[0][1])*ZOOM+ORIGINY), 2)
            #pygame.draw.circle(screen, (100, 100, 255), (int(e[1][0])*ZOOM+ORIGINX, int(e[1][1])*ZOOM+ORIGINY), 2)
            #pygame.draw.line(screen, (255,255,255), (int(e[0][0])*ZOOM+ORIGINX, int(e[0][1])*ZOOM+ORIGINY), (int(e[1][0])*ZOOM+ORIGINX, int(e[1][1])*ZOOM+ORIGINY), 2)

    pygame.display.flip()

def update_time(day,hour):
    #day = '2012-05-08'
    d = datetime.strptime(day,'%Y-%m-%d')
    #dstmp = time.strptime(day,"%Y-%m-%d")
    hour = hour + 1
    if hour == 24:
        hour = 0
        d = d+timedelta(days=1)
        #print str(d)
        day = d.strftime("%Y-%m-%d")
        #day = str(d)
    return day,str(hour)
    #return     
  
#print route

#starttime = time.time()
odmatrix = odcontainer.OriginContainer()
if __name__ == "__main__":
    day = '2012-05-01'
    #dstmp = time.strptime(day,"%Y-%m-%d")
    #print dstmp
    hour = '6' #Do not put leading zeros, e.g. use 8 instead of 08
    #origins, od, number_of_agents = odmatrix.update_weights(day,hour)
    odmatrix.update_weights(day,hour)
    origins = odmatrix.get_origins()
    if FOOTPRINTREAD == True:
        load_nodevisual(0)
    if COMPARISONMODE == True: 
        comparisonchange(TIMECLUSTERS[0][0],TIMECLUSTERS[0][1])
        reload_artificial_weights()
        calculate_atypes()
    #print origins
    od = odmatrix.get_od()
    number_of_agents = odmatrix.get_pedno()
    #print number_of_agents
    pedestrians = []
    frame = 0
    #peds = ['ped1','ped2','ped3','ped4','ped5','ped6','ped7','ped8','ped9','ped10','ped11','ped12']
    #for ped in peds:
        #ped = Pedestrian.Pedestrian()
        #ped.set_random_location()
        #ped.set_random_goal()
        #ped.set_path()
        #pedestrians.append(ped)

    for r in range(number_of_agents):
        r = Pedestrian.Pedestrian()
        r.set_random_location()
        r.destweights = od
        r.origins = origins
        hotspot, goal = pick_first(origins)
        r.aorigins = ATYPEWEIGHTS
        r.hotspot = hotspot
        r.set_goal(goal)
        r.set_path()
        pedestrians.append(r)
        

    for pd in pedestrians:
        pd.neighbors.extend(pedestrians)
        pd.neighbors.remove(pd) 

pedestrian_simulation = True
mode = 0
stick = 0
timechoice = 0
while running and __name__ == "__main__":
    #clock.tick()
    stick += 1
    global mode
    global pedestrian_simulation
    #elapsed_time = time.time() - starttime
    #print elapsed_time
    #if elapsed_time > 600: #You can set the speed of time changes here
    if stick == 2400:
        #starttime = time.time()
        day,hour = update_time(day,int(hour))
        #WRITE 12 SEGMENT TIME UPDATE HERE
        #if BTLARGECAPTURE == True: towrite = day+hour+'.csv'
        #if RANDOMLARGECAPTURE == True: towrite = 'r'+day+hour+'.csv'
        #if AHSWALK == True: towrite = 'ahs'+day+hour+'.csv'
        # if hour == '10':
        #     #print towrite
        #     #writer = csv.writer(open(towrite,'w'),delimiter=',')
        #     #for key,value in nodevisual.iteritems():
        #         writer.writerow([key,value])
        #         nodevisual[key]=0
        # if hour == '14':
        #     print towrite
        #     writer = csv.writer(open(towrite,'w'),delimiter=',')
        #     for key,value in nodevisual.iteritems():
        #         writer.writerow([key,value])
        #         nodevisual[key]=0
        # if hour == '18':
        #     print towrite
        #     writer = csv.writer(open(towrite,'w'),delimiter=',')        
        #     for key,value in nodevisual.iteritems():
        #         writer.writerow([key,value])
        #         nodevisual[key]=0
        # if hour == '22':
        #     print towrite
        #     writer = csv.writer(open(towrite,'w'),delimiter=',')
        #     for key,value in nodevisual.iteritems():
        #         writer.writerow([key,value])
        #         nodevisual[key]=0
        # if hour == '2':
        #     print towrite
        #     writer = csv.writer(open(towrite,'w'),delimiter=',')
        #     for key,value in nodevisual.iteritems():
        #         writer.writerow([key,value])
        #         nodevisual[key]=0
        # if hour == '6':
        #     print towrite
        #     writer = csv.writer(open(towrite,'w'),delimiter=',')
        #     for key,value in nodevisual.iteritems():
        #         writer.writerow([key,value])
        #         nodevisual[key]=0
        # if day == '2012-05-31':
        #     print 'It seems that everything went ok'
        #     running = 0

        odmatrix.update_weights(day,hour)
        origins = odmatrix.get_origins()
        #print origins
        od = odmatrix.get_od()
        number_of_agents = odmatrix.get_pedno()
        for ped in pedestrians:
            ped.aorigins = ATYPEWEIGHTS
            ped.destweights = od
            ped.origins = origins
        stick = 0
        #print pedestrians[0].destweights
    #Set true if want animated pedestrians
    mpos = pygame.mouse.get_pos()
    xpos = (mpos[0]-ORIGINX)/ZOOM
    ypos = (mpos[1]-ORIGINY)/ZOOM
    frame = frame +1
    if frame == 20 and pedestrian_simulation == True:
        #fps = clock.get_fps()
        #print fps/20
        #screen.fill(black)
        #print "Simulating..."
        #mode = 3
        #screen.fill(black)
        draw_map()
        #draw_gps()
        origins = odmatrix.get_origins()
        #print day,hour, origins
        locdict = odmatrix.get_all_locations()
        #print '**************************** This many origins: ',len(origins)
        if len(artificial_hotspots) > 0:
            for a in artificial_hotspots:
                clr = (255,255,255)
                if artificial_hotspots[a][2] < -100: clr =  bischeme[0]
                if artificial_hotspots[a][2] > -100 and artificial_hotspots[a][2] <= -80: clr =  bischeme[0]
                if artificial_hotspots[a][2] > -80 and artificial_hotspots[a][2] <= -60: clr =  bischeme[1]
                if artificial_hotspots[a][2] > -60 and artificial_hotspots[a][2] <= -40: clr =  bischeme[2]
                if artificial_hotspots[a][2] > -40 and artificial_hotspots[a][2] <= -20: clr =  bischeme[3]
                if artificial_hotspots[a][2] > -20 and artificial_hotspots[a][2] < 0: clr =  bischeme[4]
                if artificial_hotspots[a][2] > 0 and artificial_hotspots[a][2] <= 20: clr =  bischeme[5]
                if artificial_hotspots[a][2] > 20 and artificial_hotspots[a][2] <= 40: clr =  bischeme[6]
                if artificial_hotspots[a][2] > 40 and artificial_hotspots[a][2] <= 60: clr =  bischeme[7]
                if artificial_hotspots[a][2] > 60 and artificial_hotspots[a][2] <= 80: clr =  bischeme[8]
                if artificial_hotspots[a][2] > 80: clr =  bischeme[8]

                # if artificial_hotspots[a][0] == 1: clr = (255,0,0)
                # if artificial_hotspots[a][0] == 2: clr = (0,255,0)
                # if artificial_hotspots[a][0] == 3: clr = (0,0,255)
                # if artificial_hotspots[a][0] == 4: clr = (255,255,0)
                x = artificial_hotspots[a][1][0]
                y = artificial_hotspots[a][1][1]
                rad = RADIUS
                if artificial_hotspots[a][0] == 4: rad = ROADRADIUS
                pygame.draw.circle(screen, clr,(int(x*ZOOM+ORIGINX), int(y*ZOOM+ORIGINY)), rad*ZOOM,1)
                #for xy in artificial_hotspots[a][2]:
                    #pygame.draw.circle(screen, (255,255,255),(int(xy[0]*ZOOM+ORIGINX), int(xy[1]*ZOOM+ORIGINY)), 5)
                    #pygame.draw.polygon(screen, (255,10,255),xy, 0)
            
        for o in origins:
            omin = min(origins, key=origins.get)
            omax = max(origins, key=origins.get)
            #print omin
            #print omax
            minvalue = origins[omin]
            maxvalue = origins[omax]
            #print 'min: ',minvalue
            #print 'max: ',maxvalue
            x = locdict[o][0]
            y = locdict[o][1]
            #print "x: ",x
            #print "y: ",y
            ishift = origins[o]-minvalue
            # y = 1 + (x-A)*(10-1)/(B-A)
            #intensity = ishift*(255/(maxvalue-minvalue))
            intensity = ishift*8/(maxvalue-minvalue)
            #print 'intensity: ',intensity
            #print intensity
            pygame.draw.circle(screen, (colorscheme[intensity][0],colorscheme[intensity][1],colorscheme[intensity][2]),(int(x*ZOOM+ORIGINX), int(y*ZOOM+ORIGINY)), 5)
            #pygame.draw.circle(screen, (int(intensity),0,255-intensity), (int(x*ZOOM+ORIGINX), int(y*ZOOM+ORIGINY)), 5)
        pedestrians = [p for p in pedestrians if p.to_be_destroyed == False]
        if len(pedestrians) < number_of_agents:
            #print 'oeoe'
            entrys = []
            #print origins
            for key in origins:
                if key == 2001 or key == 2002 or key == 2003 or key == 2004: entrys.append([key,origins[key]])
                #print 'found entrys'
            #print len(entrys)
            if len(entrys) > 0: entry = weighted_choice(entrys)
            else: entry = random.choice([2001,2002,2003,2004])
            #entrys = []
            #print origins
            #for key in origins:
                #if key == 2001 or key == 2002 or key == 2003 or key == 2004: entrys.append([key,origins[key]])
            #entry = weighted_choice(entrys)
            #if entry == 2001: portals = [[-36,-192],[35,-138],[131,-78],[235,-5]]
            #if entry == 2003: portals = [[235,-5],[178,68],[122,154],[59,244]]
            #if entry == 2004: portals = [[59,244],[-38,182],[-121,125],[-211,67]]
            #if entry == 2002: portals = [[-211,67],[-149,-26],[-97,-112],[-44,-192]]
            #if entry == 2001: portals = [[75,-560],[144,-560],[172,-560],[195,-561],[274,-559],[427,-558],[598,-560],[680,-460],[679,-429],[678,-392],[681,-232],[675,-160],[675,-106]] 
            #if entry == 2002: portals = [[-617,-561],[-218,-554],[-199,559],[-86,-560],[-356,-560],[-698,-474],[-696,-376]]
            #if entry == 2003: portals = [[681,26],[676,271],[677,384],[676,440],[264,713],[386,716],[427,716],[427,714],[622,729]]
            #if entry == 2004: portals = [[-698,181],[-696,206],[-695,262],[-695,334],[-695,262],[-696,333],[-697,385],[-612,714],[-579,715],[-487,716],[-362,708],[233,713],[-98,717],[40,716],[161,718]]

            if entry == 2001: portals = [[-86,-559],[76,-560], [143,-559], [171,-558], [194,-560], [273,-560], [427,-559], [598,-562], [861,-515], [866,-468], [862,-198]]
            if entry == 2002: portals = [[-199,-560], [-219,-560], [-356,-560], [-617,-563], [-631,-558], [-927,-514], [-882,-513]]
            if entry == 2003: portals = [[864,130], [864,165], [868,387], [868,473], [867,786], [866,820], [866,874], [837,1084], [778,1093], [605,1085], [582,1091], [482,1085], [421,1086], [338,1087], [308,1086], [141,1083], [111,1087], [89,1086]]
            if entry == 2004: portals = [[-1016,801], [-1031,918], [-1028,1080], [-848,1084], [-728,1104], [-585,1086], [-440,1085], [-347,1076], [-231,1090], [-150,1085], [-44,1094]]

            portal = random.choice(portals)
            r = Pedestrian.Pedestrian()
            r.set_location(portal[0],portal[1])
            #r.set_location(locdict[entry][0],locdict[entry][1])
            #r.set_random_location()
            r.destweights = od
            r.origins = origins
            hotspot, goal = pick_first(origins)
            r.hotspot = hotspot
            r.aorigins = ATYPEWEIGHTS
            #r.set_goal(goal)
            #r.set_path()
            pedestrians.append(r)
        #print 'supposed to be: ',number_of_agents
        #print 'there is: ',len(pedestrians)
        for p in pedestrians:
            #pth = []
            #for f in p.path:
            #    px = f[0]*ZOOM+ORIGINX
            #    py = f[1]*ZOOM+ORIGINY
            #    pth.append([px,py])
            #pygame.draw.lines(screen, (0, 255, 0), False, pth, 2)
            p.update()
            if FOOTPRINTREAD == False:
                if p.routenodes != None:
                    #print p.routenodes
                    for r in p.routenodes:
                        #trail = xynodes[r]
                        nodevisual[r]+=1
                    p.routenodes = None
                    #hmark = []
                    #for i in trail:
                        #hmark.append([int(i[0])*ZOOM+ORIGINX,int(i[1])*ZOOM+ORIGINY])
                    #pygame.draw.polygon(screen, (255,255,255),hmark, 1)
                    #n = check_node(r)
                    #nodevisual[n]+=1
                    #pygame.draw.polygon(screen, (255, 255, 50), (int(r[0])*ZOOM+ORIGINX, int(r[1])*ZOOM+ORIGINY), 2)
            #heatpoint = p.node
            #if heatpoint != None:
                #hcoord = xynodes[heatpoint]
                #hmark = []
                #for i in hcoord:
                    #hmark.append([int(i[0])*ZOOM+ORIGINX,int(i[1])*ZOOM+ORIGINY])
                #pygame.draw.polygon(screen, (255,255,255),hmark, 1)
            #obs = p.define_observation()
            #observation = []
            #for o in obs:
                #ox = o[0]*ZOOM+ORIGINX
                #oy = o[1]*ZOOM+ORIGINY
                #observation.append([ox,oy])            
            #pygame.draw.polygon(screen, (0,255,0), observation, 1)
            #PEDESTRIAN DRAWING HAPPENS HERE
            if p.exiting == False: pygame.draw.circle(screen, (50, 255, 50), (int(p.x)*ZOOM+ORIGINX, int(p.y)*ZOOM+ORIGINY), 2)
            else: pygame.draw.circle(screen, (255, 100, 50), (int(p.x)*ZOOM+ORIGINX, int(p.y)*ZOOM+ORIGINY), 2)

            #pygame.draw.circle(screen, (50, 255, 50), (int(p.x)*ZOOM+ORIGINX, int(p.y)*ZOOM+ORIGINY), 2)
            #print "Wat happens",p.x,p.y
        frame = 0
        #print nodevisual
        pygame.display.flip()
    if pygame.font:
        font = pygame.font.Font(None, 36)
        timetext = font.render(str(day),0,(0,255,10))
        hourtext = font.render(hour+':00',0,(0,255,10))
        text = font.render(str((xpos,ypos)), 1, (0, 255, 10))
        textpos = text.get_rect(centerx=screen.get_width()-100)
        timepos = text.get_rect(centerx=screen.get_width()-300)
        hourpos = text.get_rect(centerx=screen.get_width()-150)
        screen.fill(black)
        #screen.fill(black, textpos)
        #screen.fill(black, hourpos)
        screen.blit(text, textpos)
        #screen.fill(black, timepos)
        screen.blit(timetext, timepos)                              
        screen.blit(hourtext, hourpos)
        pygame.display.update(textpos)
        pygame.display.update(timepos)    
        pygame.display.update(hourpos)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        if BTCAPTURE == True:
            for key,value in nodevisual.iteritems():
                btwriter.writerow([key,value])
        if RANDOMCAPTURE == True:
            for key,value in nodevisual.iteritems():
                rwriter.writerow([key,value])
        if AHSWRITE == True:
            for key,value in artificial_hotspots.iteritems():
                #ahswriter.writerow([key,value])
                ahswriter.writerow([key,value[0],value[1][0],value[1][1],value[2]])
        running = 0
    if event.type == KEYDOWN and event.key == K_q:
        global ZOOM
        ZOOM = ZOOM + 1
        print 'ZOOM',ZOOM
    if event.type == KEYDOWN and event.key == K_a:
        global ZOOM
        ZOOM = ZOOM - 1
        if ZOOM == 0: ZOOM = 1
        print 'ZOOM',ZOOM
    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.mouse.get_rel()
        #print event.button
    if event.type == pygame.MOUSEBUTTONUP:
        global ORIGINX
        global ORIGINY
        mousepos = pygame.mouse.get_rel()
        ORIGINX = ORIGINX + mousepos[0] 
        ORIGINY = ORIGINY + mousepos[1]
        #print mousepos
    if event.type == KEYDOWN and event.key == K_i:
        print 'inserting hotspot at',xpos,ypos
        selection = int(raw_input('Select hotspot type from: (1)Shopping/Nightlife, (2)Public service, (3)Suburb/park or (4)Major road: '))
        key = len(artificial_hotspots)
        artificial_hotspots[key].append(selection)
        artificial_hotspots[key].append([xpos,ypos])
        #hsnodes = []
        ahsweights = []
        for r in range(len(mesh_grid5.nodes)):
            rad = RADIUS
            if selection == 4: rad = ROADRADIUS
            if (mesh_grid5.nodes[r].x-xpos)**2 + (mesh_grid5.nodes[r].y - ypos)**2 < rad**2:
                ahsweights.append(comparisondict[r])
                #print 'oeoeoeee'
                #hsnodes.append([mesh_grid5.nodes[r].x,mesh_grid5.nodes[r].y])
                #inode = []
                #for i in xynodes[r]:
                    #inode.append([int(i[0])*ZOOM+ORIGINX,int(i[1])*ZOOM+ORIGINY])
                    #pygame.draw.circle(screen, (50, 255, 50), (int(mesh_grid5.nodes[r].x)*ZOOM+ORIGINX, int(mesh_grid5.nodes[r].y)*ZOOM+ORIGINY), 2)
                #hsnodes.append(inode)
        artificial_hotspots[key].append(sum(ahsweights)/len(ahsweights))
        print 'Artificial hotspot type ',selection,' inserted'
        reload_artificial_weights()
        for a in artificial_hotspots:
            print artificial_hotspots[a]    
    if event.type == KEYDOWN and event.key == K_p:
        timechoice = timechoice + 1
        if timechoice == 12: timechoice = 0
        print 'Timecluster ',timechoice
        if COMPARISONMODE == True: 
            comparisonchange(TIMECLUSTERS[timechoice][0],TIMECLUSTERS[timechoice][1])
            reload_artificial_weights()
            calculate_atypes()
        if FOOTPRINTREAD == True:
            load_nodevisual(timechoice)
        for p in pedestrians: p.aorigins = ATYPEWEIGHTS
        if COMPARISONMODE==True:
            if timechoice == 0:
                a0writer = csv.writer(open('aw0.csv','w'),delimiter=',')
                for key,value in artificial_hotspots.iteritems():
                    a0writer.writerow([key,value[0],value[1][0],value[1][1],value[2]])

            if timechoice == 1:
                a0writer = csv.writer(open('aw1.csv','w'),delimiter=',')
                for key,value in artificial_hotspots.iteritems():
                    a0writer.writerow([key,value[0],value[1][0],value[1][1],value[2]])

            if timechoice == 2:
                a0writer = csv.writer(open('aw2.csv','w'),delimiter=',')
                for key,value in artificial_hotspots.iteritems():
                    a0writer.writerow([key,value[0],value[1][0],value[1][1],value[2]])

            if timechoice == 3:
                a0writer = csv.writer(open('aw3.csv','w'),delimiter=',')
                for key,value in artificial_hotspots.iteritems():
                    a0writer.writerow([key,value[0],value[1][0],value[1][1],value[2]])

            if timechoice == 4:
                a0writer = csv.writer(open('aw4.csv','w'),delimiter=',')
                for key,value in artificial_hotspots.iteritems():
                    a0writer.writerow([key,value[0],value[1][0],value[1][1],value[2]])

            if timechoice == 5:
                a0writer = csv.writer(open('aw5.csv','w'),delimiter=',')
                for key,value in artificial_hotspots.iteritems():
                    a0writer.writerow([key,value[0],value[1][0],value[1][1],value[2]])

            if timechoice == 6:
                a0writer = csv.writer(open('aw6.csv','w'),delimiter=',')
                for key,value in artificial_hotspots.iteritems():
                    a0writer.writerow([key,value[0],value[1][0],value[1][1],value[2]])

            if timechoice == 7:
                a0writer = csv.writer(open('aw7.csv','w'),delimiter=',')
                for key,value in artificial_hotspots.iteritems():
                    a0writer.writerow([key,value[0],value[1][0],value[1][1],value[2]])

            if timechoice == 8:
                a0writer = csv.writer(open('aw8.csv','w'),delimiter=',')
                for key,value in artificial_hotspots.iteritems():
                    a0writer.writerow([key,value[0],value[1][0],value[1][1],value[2]])

            if timechoice == 9:
                a0writer = csv.writer(open('aw9.csv','w'),delimiter=',')
                for key,value in artificial_hotspots.iteritems():
                    a0writer.writerow([key,value[0],value[1][0],value[1][1],value[2]])

            if timechoice == 10:
                a0writer = csv.writer(open('aw10.csv','w'),delimiter=',')
                for key,value in artificial_hotspots.iteritems():
                    a0writer.writerow([key,value[0],value[1][0],value[1][1],value[2]])

            if timechoice == 11:
                a0writer = csv.writer(open('aw11.csv','w'),delimiter=',')
                for key,value in artificial_hotspots.iteritems():
                    a0writer.writerow([key,value[0],value[1][0],value[1][1],value[2]])

    if event.type == KEYDOWN and event.key == K_o:
        timechoice = timechoice - 1
        if timechoice == -1: timechoice = 11
        print 'Timecluster ',timechoice
        comparisonchange(TIMECLUSTERS[timechoice][0],TIMECLUSTERS[timechoice][1])
        reload_artificial_weights()
        calculate_atypes()
        for p in pedestrians: p.aorigins = ATYPEWEIGHTS

    # if event.type == pygame.MOUSEBUTTONDOWN:
    #     pedestrian_simulation = False
    #     screen.fill(black)
    #     draw_map()
    #     if pedestrian_simulation == False: draw_gps(mode)
    #     #draw_route()
    #     mode = mode+1
    #     if mode == 7:
    #         pedestrian_simulation = True
    #         print "Simulating pedestrians", pedestrian_simulation
    #     if mode == 8: mode = 0
    #     pygame.display.flip()

