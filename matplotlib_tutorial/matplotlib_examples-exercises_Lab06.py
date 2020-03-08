#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:55:13 2020
Miriam Stevens
@author: steve276

matplotlib examples and exercises for Lab06
"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

print(plt.style.available)               # prints available plotting styles
sns.set()                                # sets seaborn as global style (for all plots)

#plt.plot([1,2,3,4])               # plt from matplotlib

#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')            # optional axis labels
#plt.show()                        # prints the figure in addition to creating it


#data = np.genfromtxt('Tippecanoe_River_at_Ora.Annual_Metrics.txt', \
#                      skip_header=0, names=True)

data = np.genfromtxt('Tippecanoe_River_at_Ora.Annual_Metrics.txt', \
                      names=True
                      )

#data = np.genfromtxt('Tippecanoe_River_at_Ora.Annual_Metrics.txt', \
#                     skip_header=0, \
#                     names=['Year', 'Mean', 'Max', 'Min', \
#                             'StdDev','Tqmean','RBindex']
#                     )

#x = data['Year']
x = data['Year']

y1 = data['Mean']
y2 = data['Max']
y3 = data['Min']
y4 = data['StdDev']
y5 = data['Tqmean']
y6 = data['RBindex']

plt.rcParams["figure.figsize"] = [8,3]                 # dimensions in inches
plt.plot(x, data['Mean'], 'k', label="Mean", x, data['Max'], 'r', label="Meax", x, data['Min'], 'b', label="Min")
plt.xlabel('Year')
plt.legend()
#plt.grid(True)               # could use if global styling is default
plt.show()
#fig,()

plt.rcParams["figure.figsize"] = [8,3]                 # dimensions in inches
plt.plot(x, data['Mean'], 'k', x, data['Max'], 'r', label="Mean", label="Max")
plt.xlabel('Year')
plt.legend()       # cannot figure out how to get legend values on correctly when all data is in one plot
#plt.grid(True)               # could use if global styling is default
plt.show()
#fig,()

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()  

data = np.genfromtxt('Tippecanoe_River_at_Ora.Annual_Metrics.txt', \
                      names=True
                      )

plt.figure()
#plt.subplots_adjust(bottom=2,top=3)
x = data['Year']

# Top plot
plt.subplot(311)       # subplot(numrows,numcols,plot_number)
plt.rcParams["figure.figsize"] = [18,8] 
#plt.subplots()
plt.plot(x, data['Mean'], 'k', label="Mean")
plt.plot(x, data['Max'], 'r', label="Max")
plt.plot(x, data['Min'], 'b', label="Min")
#plt.xlabel('Year')
plt.ylabel('Streamflow (cfs)')
plt.legend(loc='upper left')
#plt.show()

plt.subplot(312)
# Middle plot
plt.rcParams["figure.figsize"] = [18,8]
plt.plot(x, data['Tqmean']*100, 'g^', label="Tqmean")
#plt.xlabel('Year')
plt.ylabel('Tqmean (%)')
plt.legend(loc='upper left')
#plt.show()

plt.subplot(313)
# Bottom plot
plt.rcParams["figure.figsize"] = [18,8]
plt.bar(x, data['RBindex'], label="R-B index")
plt.xlabel('Year')
plt.ylabel('R-B Index (ratio)')
plt.legend(loc='upper right')
#plt.show()

#plt.tight_layout()
plt.show()

plt.savefig('Lab06.pdf')      # results in empty pdf

#set a style before defining plot; if sns.set() is in use from above, seaborn \
# is already the default plot style --> the global styling is set as seaborn
with plt.style.context('seaborn'):             # seaborn is also already in use from above
     plt.plot(x, y1, 'r--', x, y2, x, y3)
#plt.xlabel..
plt.show()
#fig,()

# Mo's recommended video on subplots - link

fig, ax(ax1, ax2, ax3) = plt.subplots(nrows=3,ncols=1)
print(ax)

#plt.rcParams["figure.figsize"] = [12,4.5] 
ax1.subplots(311)
ax1.plot(x, data['Mean'], 'k', label="Mean")
ax1.plot(x, data['Max'], 'r', label="Max")
ax1.plot(x, data['Min'], 'b', label="Min")
ax1.xlabel('Year')
ax1.ylabel('Streamflow (cfs)')
ax1.legend(loc='upper left')

fig.show()

###################

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()  

data = np.genfromtxt('Tippecanoe_River_at_Ora.Annual_Metrics.txt', \
                      names=True
                      )
x = data['Year']

fig, (f1,f2) = plt.subplots()

f1 = p1.plot()
pl.plot(x, data['Tqmean']*100, 'g^', label="Tqmean")
p1.ylabel('Tqmean (%)')
p1.legend(loc='upper left')




plt.show()

plt.figure()

plt.subplot(311)
plt.plot(x, data['Tqmean']*100, label="Tqmean")
plt.subplot(312)
plt.bar(x, data['RBindex'], label="R-B index")
plt.xlabel('Year')

plt.show()
plt.savefig('Lab06.pdf') 


plt.subplot(313)

###OMG this works dont modify###
fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1)

#ax1.rcParams["figure.figsize"] = [18,8]
ax1.plot(x, data['Tqmean']*100, 'g^', label="Tqmean")
ax1.set_ylabel('Tqmean (%)')
ax1.legend(loc='upper left')

#ax2.rcParams["figure.figsize"] = [18,8]
ax2.bar(x, data['RBindex'], label="R-B index")
ax2.set_xlabel('Year')
ax2.set_ylabel('R-B Index (ratio)')
ax2.legend(loc='upper right')

plt.savefig('Lab06.pdf')
###OMG this works dont modify###

fig, (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1)

#ax1.subplot()      
#plt.rcParams["figure.figsize"] = [18,8] 
ax1.plot(x, data['Mean'], 'k', label="Mean")
ax1.plot(x, data['Max'], 'r', label="Max")
ax1.plot(x, data['Min'], 'b', label="Min")
ax1.set_ylabel('Streamflow (cfs)')
ax1.legend(loc='upper left')

#ax1.rcParams["figure.figsize"] = [18,8]
ax2.plot(x, data['Tqmean']*100, 'g^', label="Tqmean")
ax2.set_ylabel('Tqmean (%)')
ax2.legend(loc='upper left')

#ax2.rcParams["figure.figsize"] = [18,8]
ax3.bar(x, data['RBindex'], label="R-B index")
ax3.set_xlabel('Year')
ax3.set_ylabel('R-B Index (ratio)')
ax3.legend(loc='upper right')

plt.savefig('Lab06.pdf')


