#jujitsu charts

Setup and usage instructions:

    1. Make sure python2.7 is installed 
    and is what you are calling when you call python 
    (2.6 will probably work too) 
    (2.4 will not work)
    (3.x will not work)

    2a. For Mac, make sure that the command line utility "say" is installed 
    and functioning 
    
    2b. For linux, install the pyttsx python module 
    (first get pip... on ubuntu this looks somethign like: 
    sudo apt-get install pip) 
    (And then: pip install pyttsx)
    
    2c. For Windows, um... 
    Install cygwin and python2.7 and pip and pyttsx, I guess...

    3. git clone https://github.com/asorini/jujitsu-charts.git
    
    4. cd jujistu-charts
    
    5. python readSay.py


A list of available charts will be displayed on the screen. The user can choose a chart.

Once a chart is chosen a list of techniques on the chart is displayed. The user can choose a technique by number or at random.

To add your own charts just put a new comma-separated value (csv) file in the charts directory. csv files in the charts directory are recognized as such and displayed.

I put some comment in square brackets in the chart (mostly about differences betwee the current stanford charts and old stanford charts)
Anything starting with a "[" is treated as a comment and not displayed

There are some reference docs in the charts directory too.

Also, if you are planning on adding a chart, run the processCSV.py script on it to make sure there is no sillyness going on with the chart and put it in a consistant format, like: python processCSV.py badchart.csv >goodchart.csv
