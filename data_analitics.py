import csv #library for us in csv-files
from apriori_python import apriori #lib foor analys

def data_parser():
    assets=[]
    with open('dataset\BreadBasket_DMS.csv', newline='') as File:  
        reader = csv.reader(File,delimiter=',')
        for row in reader:
            i=0
            j = int(row[2])-1
            for i in range(j):
                assets.insert(1,row[3])      
    return assets

def analys_apriori(datar):
    freqItemSet, rules = apriori(datar, minSup=0.2, minConf=0.3)
    print(rules)
    print(freqItemSet)

def output(a):
    with open('dataset\BreadBasket.csv', mode="w", encoding='utf-8') as w_file:
        writer = csv.DictWriter(w_file, delimiter = ",",lineterminator="\r")
    for i in range (len(datar)):
        for j in range (len(datar[i])):
            print(datar[i][j])
   
with open('dataset\Basket.csv', newline='') as File:  
    transactions=[]
    reader = csv.reader(File,delimiter=',')
    for row in reader:
        transactions.append(row)

datar = []
datar=data_parser()         
#print(datar)
analys_apriori(datar)
