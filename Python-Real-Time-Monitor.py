import tkinter as tk
import matplotlib.pyplot as plt
import os
import pandas as pd
import psutil
import seaborn as sns
from datetime import datetime, timedelta, date, time
from shutil import copyfile


sns.set()
sns.set_context("paper")
sns.set_style("ticks", {'axes.facecolor': '#EAEAF2', 'axes.grid': True, 'grid.color': '.8', 'grid.linestyle': u'-'})
sns.set_palette("bright")



imagepath = "c:\\users\\bobby\\desktop\\www\\monitor.png" 
#Change for your machine

copyfile('c:\\users\\bobby\\desktop\\www\\loading.png', 'c:\\users\\bobby\\desktop\\www\\monitor.png')
#Change for your machine, loading.png is required, available from github page

clock = datetime.now()
startClock = datetime.now()
df = pd.DataFrame()
width = 2 #Line width for graph
DataPointCount = 0

class TkLemon():
	def __init__(self):
		self.canvas = tk.Canvas(root, width = 950, height = 1200)
		self.img = tk.PhotoImage(file=imagepath)
		self.imgArea = self.canvas.create_image(0, 0, anchor = 'nw', image = self.img)
		self.canvas.pack()
		root.after(100, self.changeImg)
		root.after(101, self.chkRes)	


	def changeImg(self):
		try:
			self.img = tk.PhotoImage(file=imagepath)
			self.canvas.itemconfig(self.imgArea, image = self.img)
			root.after(100, self.changeImg)
		except:
			#if theres an error, wait and try next snapshot
			root.after(1, self.changeImg)
			
	def chkRes(self):
		try:
			#If clock var is not equal to actual clock, run this...
			global clock, df, DataPointCount, width, startClock
			if clock != datetime.now():
				TD = datetime.now() - startClock
				CpuVal = psutil.cpu_percent(interval=None, percpu=False)
				RamVal = psutil.virtual_memory()[2]
				df2 = pd.DataFrame({'CPU':CpuVal, 'RAM':RamVal, 'Time':datetime.now().strftime("%S")}, index=[DataPointCount])
				df = df.append(df2)
				df['meanCPU'] = df['CPU'].mean()
				df['minCPU'] = df['CPU'].min()
				df['maxCPU'] = df['CPU'].max()
				os.system('cls')
				
				if DataPointCount > 2: #You have enough data, begin plotting.
					fig = plt.figure()
					if DataPointCount % 500 == 0: #As the data increases, thin the line.
						width = width / 1.3
						if width < 0.5:
							width = 0.5
					
					
					df.plot(ylim=(0,100), linewidth=width, alpha=0.5)
					plt.Axes.set_autoscalex_on(plt, True)
					plt.minorticks_off()
					TD = str(TD)
					plt.xlabel('Samples')
					plt.ylabel("% Utilisation")
					TD = TD.split('.')[0]
					plt.title("{} samples over {}".format(DataPointCount, TD))
					plt.savefig(imagepath,format="png",dpi=145)
					print(p.cwd())
					print("pic saved")
					plt.close('all')
				DataPointCount += 1
				clock = datetime.now()
				root.after(101, self.chkRes)	
			
		except(KeyboardInterrupt, SystemExit):
			os.system("cls")
			exit()

root = tk.Tk()
root.geometry("950x1200")
root.title("Python-Real-Time-Monitor")
app = TkLemon()

while(True):
	try:
		root.mainloop()
		
	except(KeyboardInterrupt, SystemExit):
		os.system("cls")
		exit()
