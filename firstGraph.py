#uses csvjson.com to convert csv file into json from 
#data source
#tested on Windows 10, Python 3.8

import matplotlib.pyplot as plt
import json, operator 

data = []

with open('csvjson.json', 'r') as f:
    data = json.load(f)

classifications = {}
totalEntries = 0

for entry in data:
	classCode = entry["Classification_Code"]
	
	if classCode in classifications:
		classifications[classCode] = 1 + classifications[classCode]
	else:
		classifications[classCode] = 1
	
	totalEntries += 1
  
#convert dict to list
classList = [ [k,v] for k, v in classifications.items() ]
#sort list
classList.sort(key = operator.itemgetter(1), reverse=True)

topSixClass = classList[:6]
rest = classList[6:]

otherClassTotal = 0

#totaling up the other catagories
for r in rest:
	otherClassTotal += r[1]

#preping data for chart
labels = []
sizes = []

for t in topSixClass:
	labels.append(t[0])
	sizes.append(t[1])

labels.append('other')
sizes.append(otherClassTotal)

#plotting pie chart
plt.pie(sizes, labels=labels)
plt.title("South Bend Business")
plt.axis('equal')
plt.show()