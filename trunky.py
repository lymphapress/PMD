# This handles the output of the trunkstock report in PMD and exports it to something more usable. I would love to not need this

import csv
import re
import operator
header = ['Name', 'Model', 'Serial','Cost','Date']
f = open('trunkstock_out.csv', 'w',newline='') #newline otherwise there is an empty row after each write
writer = csv.writer(f)
writer.writerow(header)

with open('trunkstock.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) #drop header
    sortedlist = sorted(csv_reader, key=lambda row: row[2], reverse=False) #sort by lastname
    for row in sortedlist:
            cDate = row[0]
            cFirstName = row[1]
            cLastName = row[2]
            cQty = row[3]
            cQty = cQty.replace("'","")
            cModel = row[4]
            cModel = cModel.replace("'","")
            cSerial = row[5]
            cSerial = cSerial.replace("'","")
            cCost = row[6]
            cCost = cCost.replace("'","")
            cQtyA = re.split(r',\s*(?![^()]*\))', cQty)
            cModelA = re.split(r',\s*(?![^()]*\))', cModel)
            cSerialA = re.split(r',\s*(?![^()]*\))', cSerial)
            cCostA = re.split(r',\s*(?![^()]*\))', cCost)
            x = 0
            oPos = 0
            for i in cModelA:
                z = int(cQtyA[x])
                offSet = 0
                while offSet < z:
                    data = f'[{cFirstName} {cLastName}, {cModelA[x]}, {cSerialA[oPos]}, {cCostA[x]}, {cDate}]'
                    print(data)
                    writer.writerow([cFirstName + ' ' + cLastName,cModelA[x],cSerialA[oPos],cCostA[x],cDate])
                    offSet = offSet + 1
                    oPos = oPos + 1
                x = x + 1