import matplotlib.pyplot as plt
import os
import pandas as pd
import time
import psutil

filepath = "c:\\users\\bobby\\desktop\\CPUPercent.txt"
imagepath = "c:\\users\\bobby\\desktop\\www\\monitor.png"

def WriteToFile(item, location, mode):
		writepath = open(location, mode)
		writepath.write(item)
		writepath.close()

		
cmd = "cd. > c:\\users\\bobby\\desktop\\CPUPercent.txt"
# Create or overwrite the log file
os.system(cmd)		
WriteToFile("Time,CPU#1,CPU#2,CPU#3,CPU#4,RAM%\n", filepath, 'a+')
clock = int(time.strftime("%S", time.localtime()))
DataPointCount = 0
global width
width = 2

try:
	while(True):
		#If clock var is not equal to actual clock, run this...
		if clock != int(time.strftime("%S", time.localtime())):
			clock = int(time.strftime("%S", time.localtime()))
			outstring = ""
			for item in list(psutil.cpu_percent(interval=None, percpu=True)):
				outstring = outstring + str(item) 
				outstring = outstring + ",\\"
				bufferstring = outstring[:-1]
				limits = len(outstring)
				outstring = bufferstring
				outstring + "\n\\"
			
			mem = list(psutil.virtual_memory())
			output = "," + str(mem[2])
			finaloutput = outstring[:-1] + output
			WriteToFile(time.strftime("%H:%M:%S", time.localtime()), filepath, 'a+')
			WriteToFile(",", filepath, 'a+')
			WriteToFile(finaloutput, filepath, 'a+')
			WriteToFile("\n", filepath, 'a+')
			df1 = pd.read_csv(filepath)
			df1['AvgCPU%'] = (df1['CPU#1'] + df1['CPU#2'] + df1['CPU#3'] + df1['CPU#4']) / 4
			df1.set_index("Time",drop=False,inplace=True)
			df1.drop('CPU#1', axis=1, inplace=True)
			df1.drop('CPU#2', axis=1, inplace=True)
			df1.drop('CPU#3', axis=1, inplace=True)
			df1.drop('CPU#4', axis=1, inplace=True)
			os.system('cls')
			
			if DataPointCount > 2:
				plt.figure()
				if DataPointCount % 500 == 0:
					width = width / 2
					if width < 0.5:
						width = 0.5
				 
				df1.plot(ylim=(0,100), linewidth=width)
					
				plt.Axes.set_autoscalex_on(plt, True)
				plt.minorticks_off()
				plt.xlabel("Samples: {}".format(DataPointCount))
				plt.ylabel("% Utilisation")
				plt.savefig(imagepath,format="png")
				print("pic saved")
				plt.close('all')
			DataPointCount += 1

except(KeyboardInterrupt, SystemExit):
	os.system("cls")
	exit()
			