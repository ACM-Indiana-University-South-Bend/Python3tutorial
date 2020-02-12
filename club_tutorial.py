#### ACM Club Tutorial
#### Indiana University South Bend 
#### Created by: Josh Barrett
#### Modified by:

'''
	This tutorial is to get to know some of the basics 
	of Python 3 and some common libraries that will be 
	useful for coding competitions and general knowledge.
	
	The code is open source but the data we will be using is
	property of the City of South Bend, Indiana.
	
	Link: https://data-southbend.opendata.arcgis.com/datasets/employee-compensation-2012-2014
'''

## The style of this tutorial is a work in progress and will 
## likely be stating the obvious more than once to some of you.
## However, this is done to help those that have never fired 
## up Python before.

########################################################################

# Use 'pip' to install these to your global python environment.
# They are libraries that are needed to run this tutorial in 
# its entirety. Do NOT worry about virtual environments at this time!

# pip is already installed if you have anything Python 3.4 or newer!

#### Commands to be typed in the terminal (Linux/Mac)or 
#### the command prompt (Windows):
# pip install numpy
# pip install pandas

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Assuming that the file from the website is downloaded into the same
# directory as this Python program, the data is loaded into a 
# Panda's "DataFrame".
data = pd.read_csv("Employee_Compensation_City_of_South_Bend.csv") 

# This prints the first 5 entries in the DataFrame and some other info.
print(data.head())
print('\n')
print(data.info())
print('\n')

# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
# The above link will help further explain what is going on next.

data2 = data[["Department", "Compensation", "Year"]]
print(data2.head())

# The next three lines are for converting the Compensation to an int.
data2.Compensation = [x.strip('$') for x in data2.Compensation]
data2.Compensation = [x.replace(',','') for x in data2.Compensation]
data2.Compensation = [int(round(float(x))) for x in data2.Compensation]

print(data2.head(150))

# This begins showing how the departments are shown in the raw data.
list_of_depts = []

for index, row in data2.iterrows():
	if row['Department'] not in list_of_depts:
		list_of_depts.append(row['Department'])

print("Number of Departments:", len(list_of_depts))
for d in list_of_depts:
	print(d)

# Replaces 'Not a number' with "UNKNOWN"
data2['Department'].fillna("UNKNOWN", inplace= True)

# Similar departments are merged, using two different methods...
# May need some refactoring but the data is converted properly in the tests
data2.Department = [x.replace('FIRE ','FIRE') for x in data2.Department]
data2.Department = [x.replace('POLICE ','POLICE') for x in data2.Department]
data2.Department = [x.replace('POLICE/COMMON COUNCIL','POLICE') for x in data2.Department]

data2.loc[data2['Department'] == 'CODE ENFORCEMENT'] = 'CODE ENFORCEMENT/ANIMAL CONTROL'
data2.loc[data2['Department'] == 'CODE ENF/ANIMAL CTRL'] = 'CODE ENFORCEMENT/ANIMAL CONTROL'
data2.loc[data2['Department'] == 'ANIMAL CONTROL'] = 'CODE ENFORCEMENT/ANIMAL CONTROL'

# Showing what has changed
list_of_depts2 = []

for index, row in data2.iterrows():
	if row['Department'] not in list_of_depts2:
		list_of_depts2.append(row['Department'])

print("Number of Departments:", len(list_of_depts2))

list_of_depts2.sort()

for d in list_of_depts2:
	print(d)

list_of_years = []

for index, row in data2.iterrows():
	if row['Year'] not in list_of_years:
		list_of_years.append(row['Year'])
		if row['Year'] is not int:
			print(index)

# THE INDEXES ABOVE, THAT PRINT IN THE CONSOLE, MUST BE LOOKED AT!

print(list_of_years)

data_2014 = data2.loc[data2['Year'] == 2014]

# Line below shows the last entries because the end of the data set had non 2014 values
print(data_2014.tail(15))

data_2014['Dept_Num'] = 0

for dept in list_of_depts2: 
	data_2014.loc[data_2014.Department == dept, 'Dept_Num'] = 1 + list_of_depts2.index(dept)

print(data_2014.head())

data_2014.plot.scatter(x='Dept_Num', y='Compensation')

plt.show()

# https://www.datacamp.com/community/tutorials/pandas-split-apply-combine-groupby
















