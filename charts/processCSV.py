#Use this to put csv files into a nicelooking consistent format
import sys,io,string

if len(sys.argv)<2:
    print "usage $ python processCSV <csvfile>"
    sys.exit()

fname=sys.argv[1]

f=io.open(fname,'r',encoding="utf-8")
for line in f:
    newline=filter(lambda x: x in string.printable,line.lower().strip())
    newestLine=""
    for word in newline.split(","):
        newestLine+=word.strip().lstrip()+", "
    print newestLine[0:len(newestLine)-2]

