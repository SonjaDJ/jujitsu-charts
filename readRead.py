import os
import sys
from words import replaceWords
from random import randint

def displayLines(inArray):
    xind=1
    for x in inArray: #looks like blah,    bla,   blah,       blah
        print xind,
        for y in x.split(","):
            print y.strip(),
        print ""
        xind+=1

def listcharts():
    for r,ds,fs in os.walk("."):
        for filename in fs:
            if ".csv" in filename:
                print "\t"+filename

def getCharts():
    charts=[]
    for r,ds,fs in os.walk("."):
        for filename in fs:
            if ".csv" in filename:
                charts.append("/".join([r,filename]))
    return charts


#f=open("aiki4.csv")
#farr=f.readlines()
#f.close()
pickQ=True
while(1):
    if pickQ:
        print ""
        print "Available Charts:\n"
        listcharts() 
        myCharts=getCharts()
        print ""
        try:
            fname=raw_input("Please pick a chart from available cvs files: ")
            #if ".csv" in fname:
            #    farr=open(fname).readlines()
            #else:
            #    farr=open(fname+".csv").readlines()
            for c in myCharts:
                if fname in c:
                    farr=open(c).readlines()
                    chartLen=len(farr)
                    chartPicked=os.path.basename(c)
                    pickQ=False    
        except:
            print "Error, chart not available"
            pickQ=True
    else:
        print ""
        print chartPicked
        print ""
        displayLines(farr)
        print ""
        num=raw_input("Next number? (r for random, q to quit, c to change chart): ")
        if num=="q":
            break
        elif num=="c":
            pickQ=True
        elif num=="r":
            num=randint(1,chartLen)  
        try:
            numIn=int(num)-1
            if numIn>-1 and numIn<len(farr):
                readme=farr[numIn]
                os.system('say '+replaceWords(readme).lower())
        except:
            print "Didn't understand... try again...",sys.exc_info()[0]
    print ""
