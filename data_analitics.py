import csv #library for us in csv-files
from apriori_python import apriori #lib foor analys

assets=[]
with open('dataset\BreadBasket_DMS.csv', newline='') as File:  
    reader = csv.reader(File,delimiter=',')
    for row in reader:  
        assets.append(row)

def data_parser(filename):
    def data_gen():
        with open(filename) as file:
            for line in file:
                yield tuple(k.strip() for k in line.split(','))
    return data_gen

transactions = data_parser('dataset\Basket.csv')

freqItemSet, rules = apriori(transactions, minSup=0.4, minConf=0.5)
print(rules)
print(freqItemSet)
