# Python-Utilisation-Monitor
Collects data, saves to csv log and outputs a PNG graph of RAM and CPU % usage over time using psutil. 
Then uses python3 http.server to serve result over network.

![alt text](https://github.com/BobbyLeonard/Python-Utilisation-Monitor/blob/master/monitor.jpg)

**libraries needed:**

  psutil
  
  matplotlib
  
  pandas
  
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
