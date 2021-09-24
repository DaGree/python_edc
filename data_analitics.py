import csv #library for us in csv-files
from apriori_python import apriori #lib foor analys

def analys_apriori(datar):
    freqItemSet, rules = apriori(datar, minSup=0.2, minConf=0.3)
    print(rules)
    print(freqItemSet)

def data_parser(name):
    j=0 
    assets=[]
    with open(name, newline='') as File:  
        reader = csv.reader(File,delimiter=',')
        for row in reader:
            if j==int(row[2]):
                assets.append(row[3])
            else:
                print(assets)
                j=int(row[2])
                assets.clear()
                assets.append(row[3])
    print('Writing complete')
              

def data_reader(name):
    with open(name, newline='') as File:  
        transactions=[]
        reader = csv.reader(File,delimiter=',')
        for row in reader:
            transactions.append(row)
    return(transactions)

#datar = []
#datar=data_reader('dataset\Basket.csv')     
data_parser('dataset\BreadBasket_DMS.csv') 
#print(datar)
#analys_apriori(datar)
