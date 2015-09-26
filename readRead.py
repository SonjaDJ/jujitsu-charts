import os
import types
import sys
from words import replaceWords,replaceWordsKyoko
#from random import randint,choice
from random import choice
from time import sleep

#pauseTime=1 #time to wait after choice before sayign the technique
pauseTime=1 #time to wait after choice before sayign the technique

#rate=100 #pretty slow
rate=175 #the default rate for say, for most speakers
#rate=300 #pretty fast

#voice="Kyoko" # a japanese lady #If you use Kyoko switch to replaceWordsKyoko
voice="Alex" # the default
#voice="Vicki" # 
#voice="Victoria" #
#voice="Bruce" # 
#voice="Ralph" # 

def displayLines(inArray):
    xind=1
    for x in inArray: #looks like blah,    bla,   blah,       blah
        print str(xind)+". ",
        for y in x.split(","):
            print y.strip(),
        print ""
        xind+=1

def listcharts():
    chartI=1
    for r,ds,fs in os.walk("."):
        for filename in fs:
            if ".csv" in filename:
                print str(chartI)+".","\t"+filename
                chartI+=1

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
        fname=raw_input("Please pick a chart from available cvs files (or q to quit): ")
        try:
            #integer label was entered
            intfname=int(fname)
            if intfname <= len(myCharts):
                farr=open(myCharts[intfname-1]).readlines()
                chartLen=len(farr)
                chartPicked=os.path.basename(myCharts[intfname-1])
                newRange=range(chartLen) #For selecting random path through chart
                pickQ=False    
            else:
                print "Chart number "+intfname+" not available..."
                print ""
        except ValueError:
            #user entered a string (that doesn't look like an integer)
            if fname=="q":
                sys.exit()
            else:
                for c in myCharts:
                    if fname in c:
                        farr=open(c).readlines()
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
        try:
            numIn=int(num)-1
            print ""
            print str(num)+". ",
            if numIn>-1 and numIn<len(farr): #don't need this anymore
                readme=farr[numIn]
                print readme
                
                sleep(pauseTime) #a little time to get ready after pressing the key
                os.system('say -r '+str(rate)+' -v'+str(voice)+' '+replaceWords(readme).lower())
                #os.system('say -r '+str(rate)+' -v'+str(voice)+' '+replaceWordsKyoko(readme).lower())
        except:
            print "Didn't understand... try again...",sys.exc_info()[0]
    print ""
