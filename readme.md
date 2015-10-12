#jujitsu charts

Setup and usage instructions:

    1. Make sure python2.7 is installed and is what you are calling when you call python (2.6 will probably work too) (2.4 will not work)
    
    2a. For mac make sure that the command line utility "say" is installed and functioning 
    
    2b. For linux make sure that python pyttsx is installed 
    
    3. git clone https://github.com/asorini/jujitsu-charts.git
    
    4. cd jujistu-charts
    
    5. python readSay.py


A list of available charts will be displayed on the screen. The user can choose a chart.

Once a chart is chosen a list of techniques on the chart is displayed. The user can choose a technique by number or at random.

To add your own charts just put a new comma-separated value (csv) file in the charts directory. csv files in the charts directory are recognized as such and displayed.

There are some reference docs in the charts directory too.

Also, if you are planning on adding a chart, run the processCSV.py script on it to make sure there is no sillyness going on with the chart and put it in a consistant format, like: python processCSV.py badchart.csv >goodchart.csv
