#uses csvjson.com to convert csv file into json from data source
#this is the second version of the type of industries that 
#South Bend, IN has to offer
#tested on Windows 10, Python 3.8

import matplotlib.pyplot as plt
import json, operator 

data = []

with open('csvjson.json', 'r') as f:
    data = json.load(f)

classifications = {}
totalEntries = 0
descriptions =[]

for entry in data:
	classCode = entry["Classification_Code"]
	if classCode in classifications:
		classifications[classCode] = 1 + classifications[classCode]
	else:
		classifications[classCode] = 1
		descriptions.append([classCode, entry["Classification_Description"]])
	totalEntries += 1

descriptions.sort(key = operator.itemgetter(0))

###CLEANING THE DATA###

#merge LPARKO and LPARKU
classifications['LPARK'] = classifications['LPARKO'] + classifications['LPARKU']
del classifications['LPARKO']
del classifications['LPARKU']
descriptions.append(['LPARK', 'LAWN PARK'])

#merge MSGEST and MSGTEC
classifications['MSG'] = classifications['MSGEST'] + classifications['MSGTEC']
del classifications['MSGEST']
del classifications['MSGTEC']
descriptions.append(['MSG', 'MASSAGE'])

#merge OPARPV and OPNAIR
classifications['OP'] = classifications['OPARPV'] + classifications['OPNAIR']
del classifications['OPARPV']
del classifications['OPNAIR']
descriptions.append(['OP', 'OPEN AIR VENDOR'])

#merge RESTAM, RESTIT, and RESTZ
classifications['REST'] = classifications['RESTAM'] + classifications['RESTIT'] + classifications['RESTZ']
del classifications['RESTAM']
del classifications['RESTIT']
del classifications['RESTZ']
descriptions.append(['REST', 'RESTAURANTS'])

#merge TA and TATEST
classifications['T'] = classifications['TA'] + classifications['TATEST']
del classifications['TA']
del classifications['TATEST']
descriptions.append(['T', 'TATOO AND PIERCING'])

#merge TAXICAB, TAXICO, and TAXID
classifications['TAXI'] = classifications['TAXICAB'] + classifications['TAXICO'] + classifications['TAXID']
del classifications['TAXICAB']
del classifications['TAXICO']
del classifications['TAXID']
descriptions.append(['TAXI', 'TAXI RELATED'])

#delete TEST1
totalEntries -= classifications['TEST1']
del classifications['TEST1']

#merge TRANS and TRANSC
classifications['TRAN'] = classifications['TRANS'] + classifications['TRANSC']
del classifications['TRANS']
del classifications['TRANSC']
descriptions.append(['TRAN', 'TRANSIENT MERCHANT'])

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
codes = []

for d in descriptions:
	codes.append(d[0])

for t in topSixClass:
	temp = codes.index(t[0])
	labels.append(descriptions[temp][1])
	sizes.append(t[1])

labels.append('other')
sizes.append(otherClassTotal)

#plotting pie chart
plt.pie(sizes, labels=labels)
plt.title("South Bend Business")
plt.axis('equal')
plt.show()
