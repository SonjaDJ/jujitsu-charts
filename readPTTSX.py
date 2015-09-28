import os
import types
import sys
from words import multiple_replace,myWords
#from random import randint,choice
from random import choice
from time import sleep
import pyttsx
import io #ugh, need io.open because otherwise get binary garbage from utf-8 files

#pauseTime=1 #time to wait after choice before sayign the technique
pauseTime=1 #time to wait after choice before sayign the technique

#rate=100 #pretty slow
#rate=175 #the default rate for say, for most speakers
voiceRate=140 #for pyttsx default voice on ubuntu #the default rate for say, for most speakers
#rate=300 #pretty fast

###For use with say version...
#voice="Alex" # the default
#voice="Vicki" # 
#voice="Victoria" #
#voice="Bruce" # 
#voice="Ralph" # 

#sometime pyttsx fails to initialize...
try:
    en=pyttsx.init()
except:
    print "Could not set up pyttsx speach engine..."
    print "Quiting..."
    sys.exit()



def displayLines(inArray):
    xind=1
    for x in inArray: #looks like blah,    bla,   blah,       blah
        print str(xind)+". ",
        for y in x.split(","):
            print y.strip(),
        print ""
        xind+=1

#charts from getcharts
def listcharts():
    chartI=1
    chartsArray=getCharts()
    #for r,ds,fs in os.walk("."):
    #    for filename in fs:
    #        if ".csv" in filename:
    #            chartsArray.append(filename)
    #            #print str(chartI)+".","\t"+filename
    #            #chartI+=1
    #chartsArray.sort()
    for c in chartsArray:
        print str(chartI)+".","\t"+os.path.basename(c)
        chartI+=1



def getCharts():
    charts=[]
    for r,ds,fs in os.walk("."):
        for filename in fs:
            if ".csv" in filename:
                #charts.append("/".join([r,filename]))
                charts.append(os.path.join(r,filename))
    charts.sort()
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
        fname=raw_input("Please pick a chart from available cvs files (or q to quit): ")
        try:
            #integer label was entered
            intfname=int(fname)
            if intfname <= len(myCharts):
                farr=io.open(myCharts[intfname-1],encoding="utf-8").readlines()
                #print "HERE3",farr
                chartLen=len(farr)
                chartPicked=os.path.basename(myCharts[intfname-1])
                #print "HERE4",chartPicked
                newRange=range(chartLen) #For selecting random path through chart
                pickQ=False    
            else:
                print "Chart number "+intfname+" not available..."
                print ""
        except ValueError:
            #print "HERE1"
            #user entered a string (that doesn't look like an integer)
            if fname=="q":
                sys.exit()
            else:
                for c in myCharts:
                    if fname in c:
                        farr=io.open(c,encoding="utf-8").readlines()
                        #print "HERE2",farr
                        chartLen=len(farr)
                        chartPicked=os.path.basename(c)
                        newRange=range(chartLen) #For selecting random path through chart
                        pickQ=False    
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
            ##This if want rand, but I think I'd prefer random path through each once
            #num=randint(1,chartLen)  
            num=choice(newRange)+1 #newRange is set when the chart is first chosen
            if len(newRange)>1:
                newRange.remove(num-1) #get rid of this one from the random choices so hit each one once
            else:
                pickQ=True
            print "Remaining: ",map(lambda x: x+1,newRange)
        if (num>-1 or num.isdigit()) and (num!="c"): #the num>-1 is there first because if user hit "r" num is an int, but if not num is a string... this is bad... 
        #if num>-1 or num.isdigit(): #the num>-1 is there first because if user hit "r" num is an int, but if not num is a string... this is bad... 
            readme=""
            try:
                numIn=int(num)-1
                print ""
                print str(num)+". ",
                if numIn>-1 and numIn<len(farr): #don't need this anymore
                    readme=farr[numIn]
            except:
                print "Didn't understand... try again...",sys.exc_info()[0]
            print readme
            sleep(pauseTime) #a little time to get ready after pressing the key
            sayString=multiple_replace(myWords,readme).lower()
                #print sayString
                #UGH, why do I need a new one every time...
                #if I don't do this it will only say the first one and then dies on the other lines 
                #(onyl says first bit)
            del en
            en=pyttsx.init()
            en.setProperty("rate",voiceRate)
            en.say(sayString)
            en.runAndWait()
    print ""
