# Python-Real-Time-Monitor
Collects CPU and RAM usage data, appends to a pandas dataframe and uses tkinter for a GUI to display a realtime matplotlib PNG graph of RAM and CPU % usage over time 

## To View online
Until I have learnt some Flask,
You can view the PNG remotely by using 
python3 http.server to serve PNG over network.
Because a new image is being saved approximately every second, the webpage just needs to refreshed to make it appear as a stream.
For this you can use an auto refesh extension for Chrome.


![alt text](https://github.com/BobbyLeonard/Python-Utilisation-Monitor/blob/master/monitorseaborn.jpg)

**libraries needed:**
  
  tkinter

  psutil
  
  matplotlib
  
  pandas
  
  seaborn (optional, if not using see Standard Visualization below)
  
**To install libraries:** 

>e.g "pip install psutil"

**Remember:** change the filepath and imagepath variables to suit your system.
For non-Windows OS change os.system(cmd)
psutil did not work for me on RPi3.

**To View Remotely:**

  >Create a new folder called WWW and set imagepath to save here.
  
  >Open a command prompt
  
  >"cd WWW"
    
  >"python -m http.server"
  
  Open your broswer and go to port 8000 on the machine running the script.
  Use an auto refresh extension to refresh the image.
  
  
