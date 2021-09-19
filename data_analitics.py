import csv #library for us in csv-files
from apriori_python import apriori #lib foor analys

transactions=[]
with open('dataset\Basket.csv', newline='', encoding='latin-1') as File:  
    assets=[]
    reader = csv.reader(File,delimiter=',')
    for row in reader:  
        assets.append(row[1])

def data_parser(filename):
    
    def data_par():
        with open(filename) as file:
            for line in file:
                yield tuple(k.strip() for k in line.split(','))
    return data_par
    
#transactions = list(data_parser('dataset\Basket.csv'))
#print(type(transactions))
for i in range(10):
    print(assets[i])
freqItemSet, rules = apriori(assets, minSup=0.3, minConf=0.3)
print(rules)
print(freqItemSet)
