import os, sys, io
from words import getPhonetic
from random import choice
from time import sleep
import pyttsx
import types 

#pauseTime=1 #time to wait after choice before sayign the technique
pauseTime=1 #time to wait after choice before sayign the technique

#rate=100 #pretty slow
voiceRate=175 #the default rate for say, for most speakers
#rate=300 #pretty fast

###For use with say version... 
voice="Alex" # the default
#voice="Vicki" # 
#voice="Victoria" #
#voice="Bruce" # 
#voice="Ralph" # 

def getAvailableCharts():
    """
        charts are in ./charts/ directory and are csv files the name of which is the name of the charts+".csv"

        input: 
            none
        output: 
            array of tuples [ (1, blah, /home/charts/blah.csv), (2, other, /home/charts/other.csv), ... ] sorted by second element (chart name) indexed by first element (to avoid indexing from zero)
    """
    pathArray=[]
    indexArray=[]
    chartUserIndex=0
    for r,ds,fs in os.walk("./charts/"):
        for f in fs:
            chartName,fext=os.path.splitext(f) 
            fullpath=os.path.join(r,f)
            if fext.lower()=='.csv':
                chartUserIndex+=1
                pathArray.append((chartName,fullpath))
    return map(lambda x: (x[0],x[1][0],x[1][1]),zip(map(lambda x: x+1,xrange(chartUserIndex)),sorted(pathArray)))
    

def displayCharts(aC,displayType='Charts'):
    """
        Display the available charts (or lines in a chart if displayType='Lines'
        input: array of tuples of len at least 2.
    """
    print ""
    if displayType=='Charts':
        print "Available charts to choose from: "
    elif displayType=='Lines':
        print "Available techniques to choose from: "
        
    for el in aC:
        assert type(el[1])==types.StringType
        print "\t"+str(el[0])+". "+el[1]
    print "---------------------------------"
            
def selectChart():
    """
        return the user's chart selection
    """
    chartStr=raw_input("Enter number of chart to display/read: ")
    print "---------------------------------------"
    while (True):
        try:
            chartIndexInt=int(chartStr)
            return chartIndexInt
        except:
            print "-------------------------------------------"
            chartStr=raw_input("Try again... Enter a number: ")
            print "---------------------------------------"

def getChartData(aC,cI):
    """
        input: array of charts, index of selected chart
        output: array of tuples (technique index, technique string) and array of correct length for use with random selection
    """
    fpath=[x[2] for x in aC if x[0]==cI][0]
    retArrTwo=[]
    with open(fpath,'r') as f:
        retArrTemp=[x.strip() for x in f.readlines() if x[0]!='[']
        for el in retArrTemp:
            commentIndex=el.find('[')
            if commentIndex==-1:
                retArrTwo.append(el)
            else:
                retArrTwo.append(el[:commentIndex])
    trackingArray=[x+1 for x in xrange(len(retArrTwo))]
    return zip(map(lambda x: x+1,xrange(len(retArrTwo))),retArrTwo),trackingArray

def displayLines(cLines):
    """
        input: and array of chart lines sep by commas
        output: none
    """
    displayCharts(cLines,displayType='Lines')

def getStringToRead(chartLineData,userLineChoice):
    for el in chartLineData:
        if el[0]==userLineChoice:
            return el[1]
    return "Line Error"
            
def main():
    """
        display the charts (.csv files) in the ./charts directory
        allow user to select a chart by number
        allow user to then select a technique from the chart by number or at random
        read the technique using text-to-speech capabilites
    """
    aCharts=getAvailableCharts() #array of tuples (chartUserIndex, chartName, chartPath)

    displayCharts(aCharts)
    chartUIndex=selectChart()
    chartLineData,trackArr=getChartData(aCharts,chartUIndex)
    userPickedChart=True
    copyArr=list(trackArr) #get a copy in case I want to restore
    
    while True:
        if userPickedChart:
            #display the chart lines and ask user to pick one
            #or user can choose to have a random one picked (as part of taking random path through chart)
            #or user can choose to change chart
            #or user can choose to quit
            displayLines(chartLineData) 
            
            userSelectedLine=False
            print "Select technique to read by number..."
            print "Or hit 'r' to read a random technique"
            print "Or hit 'c' to change to a new chart..."
            print "Or hit 'q' to quit"
            userRawInput=raw_input("Enter your selection: ")
            if userRawInput.lower()=='q':
                sys.exit()
            elif userRawInput.lower()=='c': 
                userPickedChart=False
            elif userRawInput.lower()=='r': 
                if len(trackArr)==0:
                    trackArr=list(copyArr) #restore the entire thing
                userLineChoice=choice(trackArr)
                trackArr.remove(userLineChoice)
                print ""
                print "Random picked technique number {0}. There are {1} techniques remaining.".format(userLineChoice,len(trackArr))
                userSelectedLine=True
            else: 
                try:
                    userLineChoice=int(userRawInput)
                    userSelectedLine=True
                    if userLineChoice>len(copyArr) or userLineChoice<1:
                        print ""
                        print "Technique number out of range. Try again..."
                        userSelectedLine=False
                except:
                    print "Hmm... not sure what you mean... Try again..."

            if userSelectedLine:
                #print userLineChoice,trackArr
                stringToPrint=getStringToRead(chartLineData,userLineChoice)
                stringToRead=getPhonetic(stringToPrint)
                print ""
                print "Now reading technique {0}: {1}".format(userLineChoice,stringToPrint)
                sleep(pauseTime) #Give a little time for tori to get ready after pressing the key
                if 'darwin' in sys.platform.lower():
                    #try using 'say'
                    os.system('say -r '+str(voiceRate)+' -v'+str(voice)+' '+stringToRead.lower())
                elif 'linux' in sys.platform.lower():
                    #try using pyttsx
                    en=pyttsx.init()
                    en.setProperty("rate",voiceRate)
                    en.say(stringToRead.lower())
                    en.runAndWait()
                    del en 
                else:
                    print "Sorry, text-to-speech not supported on this operating system: "+sys.platform 
                userSelectedLine=False
        else:
            displayCharts(aCharts)
            chartUIndex=selectChart()
            chartLineData,trackArr=getChartData(aCharts,chartUIndex)
            userPickedChart=True
            copyArr=list(trackArr) #get a copy in case I want to restore
        
if __name__=='__main__':
    main()
