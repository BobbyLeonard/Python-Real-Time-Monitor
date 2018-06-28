# Python-Real-Time-Monitor

Collects CPU and RAM usage data, appends to a pandas dataframe, 
then display a live matplotlib PNG graph of RAM and CPU % usage over time.
Comes in 2 versions.

>The GUI version uses tkinter as an interface to display the graph.
>'loading.png' is required, set your paths in the script 

>The Webapp version uses Flask and serves an auto refreshing page from your ip on port 80.
>'index.html' should be put in a folder called templates which should be in
>the same folder as Python-Real-Time-Monitor-WebApp.py


![alt text](https://github.com/BobbyLeonard/Python-Utilisation-Monitor/blob/master/sns.jpg)

**Libraries needed:**
  
  >psutil
  
  >matplotlib
  
  >pandas
  
  >seaborn
  
***GUI:***

  >tkinter

***Webapp:***

  >flask

  >flask_socketio
  
**To install libraries:** 

>"pip install psutil"
