import csv #library for us in csv-files
from apriori_python import apriori #lib foor analys

transactions=[]
with open('dataset\BreadBasket_DMS.csv', newline='',) as File:  
    assets=[]
    reader = csv.reader(File,delimiter=',')
    for row in reader: 
        if row[2]!='Transaction':
            i = int(row[2])
            assets.insert(i,row[3])
 
#transactions = list(data_parser('dataset\Basket.csv'))
#print(type(transactions))
for i in range(len(assets)):
    # будем теперь обходить массив z[i]
    for j in range(len(assets[i])):
        print(assets[i][j])
#freqItemSet, rules = apriori(assets, minSup=0.3, minConf=0.3)
#print(rules)
#print(freqItemSet)
