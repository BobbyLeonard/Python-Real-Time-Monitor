# Python-Real-Time-Monitor


Collects CPU and RAM usage data, appends to a pandas dataframe and uses tkinter for a GUI to display a live matplotlib PNG graph of RAM and CPU % usage over time. Easily tweaked to measure different items. 


![alt text](https://github.com/BobbyLeonard/Python-Utilisation-Monitor/blob/master/sns.jpg)

**libraries needed:**
  
  tkinter

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
Until I have learnt some Flask,
You can view the PNG remotely by using 
python3 http.server to serve PNG over network.
Because a new image is being saved approximately every second, the webpage just needs to refreshed to make it appear as a stream.
For this you can use an auto refesh extension for Chrome.
  
  >Open a command prompt
  
  >"cd WWW"
    
  >"python -m http.server"
  
  Open your broswer and go to port 8000 on the machine running the script.
  Use an auto refresh extension to refresh the image.
  
  
