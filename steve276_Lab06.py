#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 18:59:24 2020
Miriam Stevens
@author: steve276

Uses subplots from matplotlib to generate a single page with three plots.
The page is saved to a pdf and command line arguments are used to determine
the input and output file names.
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns                  # seaborn used for auto scaling plots

#print(plt.style.available)            # list available matplotlib chart styles
sns.set()                              # sets seaborn as default global style

print("Enter name of file to open as <filename.ext> :")
filename = input()

# expected file: either 'Tippecanoe_River_at_Ora.Annual_Metrics.txt'
#                or     'Wildcat_Creek_at_Lafayette.Annual_Metrics.txt'

data = np.genfromtxt(f"{filename}", names=True)   # read input with f'string; names in first line taken as headers

x = data['Year']

fig, (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1)

# Top plot - three variables, one plot
#ax1.rcParams["figure.figsize"] = [18,8]                # rcParams not compatible with ax., only with plt. 
ax1.plot(x, data['Mean'], 'k', label="Mean")
ax1.plot(x, data['Max'], 'r', label="Max")
ax1.plot(x, data['Min'], 'b', label="Min")
ax1.set_ylabel('Streamflow (cfs)')
ax1.legend(loc='upper left')

# Middle plot
#ax2.rcParams["figure.figsize"] = [18,8]                # size in inches
ax2.plot(x, data['Tqmean']*100, 'g^', label="Tqmean")
ax2.set_ylabel('Tqmean (%)')
ax2.legend(loc='upper left')

# Bottom plot
#ax3.rcParams["figure.figsize"] = [18,8]
ax3.bar(x, data['RBindex'], label="R-B index")
ax3.set_xlabel('Year')
ax3.set_ylabel('R-B Index (ratio)')
ax3.legend()

#plt.show()                        # uncomment to display in GUI upon creation
           
print("Enter name of PDF to be saved as <filename>. Exclude the extension. :")
output_file = input()                  # examples : Tippecanoe_Metrics, Wildcat_Metrics
plt.savefig('%s.pdf' % output_file)
