import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import csv


with open('/Users/daniel/DataViz/trim/composite.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates=[]
    AAPL = []
    for row in readCSV:
        dates = row[0]
        AAPL = row[1]

        dates.append(date)
        AAPL.append(AAPL)
print(dates)
print(AAPL)

plt.style.use('BME163.mplstyle')

# from assignment spec
fig_height = 2
fig_width = 3.42

plt.figure(figsize=(fig_width, fig_height))

# axes units are in normalized units: 0-1
panel_width=1/fig_width
panel_height=1/fig_height

# left, bottom, width, height
panel1=plt.axes([0.1,0.2,panel_width,panel_height])

panel1.tick_params(axis='both', which='both',\
                   bottom='off', labelbottom='off',\
                   left='off', labelleft='off',\
                   right='off', labelright='off',\
                   top='off', labeltop='off')
                   
# generate panel 1 points
vals = np.arange(0,np.pi/2,.06)
for val in vals:
    sin = np.sin(val)
    cos = np.cos(val)
    panel1.plot(cos,sin,\
                marker='o', linewidth=0,\
                markeredgewidth=0, markersize=2,\
                markerfacecolor=(cos,cos,cos))
panel1.set_xlim(-0.03,1)
panel1.set_ylim(0,1.04)
plt.show()
#plt.savefig('testPlot.png',dpi=600)
