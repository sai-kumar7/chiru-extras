import numpy as np
import pandas as pd
from datetime import timedelta
import re
#import time

date = 20100728
dt = pd.datetime(2010, 7, 28)


testread = pd.read_csv('1newannot.csv', parse_dates=True)
larm = pd.read_csv('1LARM.csv', parse_dates=True)
rarm = pd.read_csv('1RARM.csv', parse_dates=True)
#lrm = pd.read_csv('1annot.csv', index_col=0, parse_dates=True)
annoindex = []
larmindex = []
rarmindex = []

def sliding_window_1d(a,ws,ss = None):
    '''
    Parameters
        a  - a 1D array
        ws - the window size, in samples
        ss - the step size, in samples. If not provided, window and step size
             are equal.
    '''
     
    if None is ss:
        # no step size was provided. Return non-overlapping windows
        ss = ws
     
    # calculate the number of windows to return, ignoring leftover samples, and
    # allocate memory to contain the samples
    valid = len(a) - ws
    nw = (valid) // ss
    out = np.ndarray((nw,ws),dtype = a.dtype)
     
    for i in xrange(nw):
        # "slide" the window along the samples
        start = i * ss
        stop = start + ws
        out[i] = a[start : stop]
     
    return out

for f in larm.Time:
    #print f
    hours = pd.datetime.fromtimestamp(f/1000.0)
    correct = pd.datetime.combine(dt,hours.time())
    #print correct - timedelta(hours=9)
    larmindex.append(correct - timedelta(hours=9))

for r in rarm.Time:
    #print f
    hours = pd.datetime.fromtimestamp(r/1000.0)
    correct = pd.datetime.combine(dt,hours.time())
    #print correct - timedelta(hours=9)
    rarmindex.append(correct - timedelta(hours=9))    

for y in testread.Time:
    #splittime = y.split(':')
    #retime = re.findall(r"[\w']+", y)
    hours = pd.datetime.strptime(y,'%H:%M:%S.%f')
    #time = pd.datetime(splittime[0],splittime[1],splittime[2])
    correct = pd.datetime.combine(dt,hours.time())
    annoindex.append(correct)

larm.index = larmindex
rarm.index = rarmindex
testread.index = annoindex
print testread.tail()
del rarm['Time']
del larm['Time']
del testread['Time']

#print rarm.head()

#rarm = rarm.reindex(larmindex)
#annotations = testread.reindex(larmindex)
hands = larm.join(rarm)
#print rarm[:100]
#print hands
#features = []
features = {}

SLIDE = 128
OVERLAP = 64
#global stuff for window sizes

for column in hands:
    print column
    #print hands[column]
    mfeatures = []
    stdfeatures = []
    enfeatures = []
    window = sliding_window_1d(hands[column],SLIDE,OVERLAP)
    for w in window:
        mfeatures.append(np.mean(w))
        stdfeatures.append(np.std(w))
        en = np.fft.fft(w)
        #print en
        absen = abs(en)
        #print absen
        enfeatures.append(np.mean(absen))
    #features.append(mfeatures)
    #features.append(stdfeatures)
    #features.append(enfeatures)
    features[column+'mean']=mfeatures
    features[column+'std']=stdfeatures
    features[column+'en']=enfeatures
    print "Features mean, std and energy added"

def create_correlations(left, right):
    corrfeatures = []
    lwindows = sliding_window_1d(left,SLIDE,OVERLAP)
    rwindows = sliding_window_1d(right,SLIDE,OVERLAP)
    for x,y in zip(lwindows,rwindows):
        corrfeatures.append(float(np.correlate(x,y)))
    return corrfeatures

#print hands['lax']

print hands.columns

xcorr = create_correlations(hands.lax,hands.rax)
ycorr = create_correlations(hands.lay,hands.ray)
zcorr = create_correlations(hands.laz,hands.raz)

features['xcorr']=xcorr
features['ycorr']=ycorr
features['zcorr']=zcorr

#features.append(xcorr)
#features.append(ycorr)
#features.append(zcorr)

print "Correlations added to features"
#print len(features)

dataset = pd.DataFrame(features)

avgtime = []
for f in hands.index:
    avgtime.append(f)
    atime = avgtime[0::OVERLAP]

#print len(avgtime)
#print len(atime)
del atime[-3:]
dataset.index = atime

matched_timestamps = []

fill = 'Idle'
fillannotations = []
index = 0
timeindex = 1
start = True
print len(dataset.index)
print len(testread.index)
for r in range(len(dataset.index)): #Horrible
    #print r
    #print index
    if index >= len(testread.index)-1:
        #print 'wat'
        action = 'Idle'
        fillannotations.append(action)
        continue
    action = testread.Annotation[index]
    if 'STOP' in action: action = 'Idle'
    if 'START' in action: action = action[:-5]
    time = dataset.index[r]
    if start == True: time2 = testread.index[index]
    if start == False: time2 = testread.index[timeindex]
    delta = time-time2
    if delta.total_seconds() <0:
        #print start      
        if start == True: action = 'Idle'
        fillannotations.append(action)
        print delta.total_seconds() <0,'Dataset time: ',time,' Annotation time: ',time2,'Action: ',action,'Index: ',index
    else:
        #print delta.total_seconds() <0
        if start == False: 
            index = index +1
            timeindex = timeindex +1
        #print index
        if index >= len(testread.index)-1:
            #print 'wat'
            action = 'Idle'
            fillannotations.append(action)
            continue
        action = testread.Annotation[index]
        if 'STOP' in action: action = 'Idle'
        if 'START' in action: action = action[:-5]
        fillannotations.append(action)
        start = False
        #print start
        print delta.total_seconds() <0,'Dataset time: ',time,' Annotation time: ',time2, 'Updating... Action: ',action,'Index: ',index
    
#print fillannotations       

# for t in testread.index:
#     delta = []
#     for d in dataset.index:
#         delta.append(abs(t-d))
#     closest = delta.index(min(delta))
#     matched_timestamps.append(dataset.index[closest])

# testread.index = matched_timestamps
# testread.to_csv('annowx.csv')

# annotations = testread.reindex(dataset.index)
# print annotations
# annotations = annotations.fillna(0)
# strp = 'Idle'
# Fixed_annotations = []
# for a in annotations['Annotation']:
#     print a
#     if a == 0:
#         print strp
#         #print 'wat: ',a
#         Fixed_annotations.append(strp)
#     elif 'START' in a:
#         strp = a
#         Fixed_annotations.append(strp)
#     elif 'STOP' in a:
#         strp = 'Idle'
#         Fixed_annotations.append(strp)      

# print Fixed_annotations

#print dataset.tail()
#print dataset
print len(fillannotations)
print len(dataset.index)
dataset['Annotations'] = fillannotations
dataset.to_csv('datatest.csv')
#annotations.to_csv('annotations.csv')
#print annotations.tail()
print dataset.tail()
#dataset = dataset.ix[:-6]
#print dataset
#print dataset.tail()


# timewindows = sliding_window_1d(hands.index,256,128)

# print timewindows
# for t in timewindows:
#     print "start: ",t[0]
#     print "finish: ",t[-1]
#     tdelta = t[0]-t[-1]
#     print tdelta
#     avgtime = t[0]+tdelta
#     print avgtime
#     avgtimes.append(avgtime)
#print dataset
#dataset = pd.DataFrame.from.items([('laxmean' features[0]),

#columns=['laxmean','laxstd','laxen','laymean','laystd','layen','lazmean','lazstd','lazen','lgxmean','lgxstd','lgxen','lgymean','lgystd','lgyen','lgzmean','lgzstd','lgzen','raxmean','raxstd','raxen','raymean','raystd','rayen','razmean','razstd','razen','rgxmean','rgxstd','rgxen','rgymean','rgystd','rgyen','rgzmean','rgzstd','rgzen','xcorr','ycorr','zcorr'])


#print len(features)
#print features
#print mfeatures


#fmean = pd.rolling_mean(hands,128)
#print fmean
#s = raw_input('Press enter to continue')
#hands.plot()
#fmean.plot(subplots=True)
#print annotations[3900:4000]
#whole = pd.concat(testread,larm)

#print whole.head()

#print testread.head()
#print testread.head()

#print larm.head()
#print lrm.head()
