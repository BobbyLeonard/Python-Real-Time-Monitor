# Python-Real-Time-Monitor
Collects CPU and RAM usage data, appends to a pandas dataframe, 
then display a live matplotlib PNG graph of RAM and CPU % usage over time.
Comes in 2 versions.
The GUI version uses tkinter as an interface to display the graph.
The Webapp version uses Flask and serves an auto refreshing image from your ip on port 5000.


![alt text](https://github.com/BobbyLeonard/Python-Utilisation-Monitor/blob/master/sns.jpg)

**libraries needed:**
  
  tkinter
  
  flask

  psutil
  
  matplotlib
  
  pandas
  
  seaborn 
  
**To install libraries:** 

>e.g "pip install psutil"

**Remember:** 

>Create a new folder called WWW and set imagepath to save here.

Change the imagepath variable to suit your system.
For non-Windows OS change os.system(cmd)
psutil did not work for me on RPi3.

**To View Remotely:**
Use the webapp version
  
  
