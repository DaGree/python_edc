import csv #library for us in csv-files
from apriori_python import apriori #lib foor analys

def output(assets):
    for i in range(9683):
        for j in range(100):
            print(assets[i][j])
    
def input_arr(reader):
    A=[]
    for i in range(int(reader)):
        row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
        A.append(row)
    return A

with open('dataset\BreadBasket_DMS.csv', newline='') as File:  
    transactions=[]
    reader = csv.reader(File,delimiter=',')
    for row in reader:
        if row[2]!='Transaction':
            i = int(row[2])
            #transactions.append(i)
            #transactions.append(row[3])
            transactions.insert(i,row[3])
 
#transactions = list(data_parser('dataset\Basket.csv'))
#print(type(transactions))
#print(assets)
#output(assets)
freqItemSet, rules = apriori(transactions, minSup=0.4, minConf=0.5)
print(rules)
print(freqItemSet)
