import matplotlib
matplotlib.use('Agg')

from io import BytesIO
import base64

import matplotlib.pyplot as plt
import os
import pandas as pd
import time
import psutil
import seaborn as sns
from flask import Flask
from datetime import datetime, timedelta, date, time


app = Flask(__name__)

sns.set()
sns.set_context("paper")
sns.set_style("ticks", {'axes.facecolor': '#EAEAF2', 'axes.grid': True, 'grid.color': '.8', 'grid.linestyle': u'-'})
sns.set_palette("bright")
DataPointCount = 0
df = pd.DataFrame()
startClock = datetime.now()
clock = datetime.now()

@app.route('/')
def index():
    global width, DataPointCount, df, clock, startClock
    width = 2
    while (True):
        try:
            # If clock var is not equal to actual clock, run this...
            if clock != datetime.now():
                TD = datetime.now() - startClock
                CpuVal = psutil.cpu_percent(interval=None, percpu=False)
                RamVal = psutil.virtual_memory()[2]
                df2 = pd.DataFrame({'AvgCPU%': CpuVal, 'RAM%': RamVal,
                                    'Time':datetime.now().strftime("%S")},
                                   index=[DataPointCount])
                df = df.append(df2)
                df['meanCPU%'] = df['AvgCPU%'].mean()
                df['minCPU%'] = df['AvgCPU%'].min()
                df['maxCPU%'] = df['AvgCPU%'].max()
                df.set_index("Time", drop=True, inplace=True)
                os.system('cls')

                if DataPointCount > 2:
                    plt.figure()
                    if DataPointCount % 500 == 0:
                        width = width / 1.3
                        if width < 0.5:
                            width = 0.5

                    df.plot(ylim=(0, 100), linewidth=width, alpha=0.5)
                    plt.Axes.set_autoscalex_on(plt, True)
                    plt.minorticks_off()
                    TD = str(TD)
                    plt.xlabel('Samples')
                    plt.ylabel("% Utilisation")
                    TD = TD.split('.')[0]
                    plt.title("{} samples over {}".format(DataPointCount, TD))

                    Imageoutputhtml = '''
                    <html>
                        <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=yes">
                            <meta name="description" content="">
                            <meta name="author" content="">
                            <meta http-equiv="refresh" content="1">
                            <!-- ^^^ auto refresh ^^^ -->
                            <link rel="icon" href="{{ url_for('static', filename='favicon.jpg') }}">
                            <!-- Latest compiled and minified CSS -->
                            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
                            <title>Python Monitor</title>
                        </head>
                            <body>
                            <div class="row">
                            <div class="mx-auto text-center">
                                <img src="data:image/jpeg;base64,{}" alt="PyMon">
                            </div>
                            </div>
                            </body>
                        </html>
                    '''
                    img_base64 = BytesIO()
                    plt.savefig(img_base64, format='jpg', dpi=120)
                    img = base64.b64encode(img_base64.getvalue())
                    img = str(img)
                    img = img[2:-1]
                    DataPointCount += 1
                    print("pic saved")
                    plt.close('all')
                    return Imageoutputhtml.format(img)

                DataPointCount += 1
                print("pic saved")
                plt.close('all')



        except(KeyboardInterrupt, SystemExit):
            os.system("cls")
            return 0

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
