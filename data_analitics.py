import csv #library for us in csv-files
from apriori_python import apriori #lib foor analys

def data_parser():
    assets=[]
    j=0
    with open('dataset\BreadBasket_DMS.csv', newline='') as File:  
        reader = csv.reader(File,delimiter=',')
        for row in reader:
            i=0
            if j == int(row[2]):
                k = int(row[2])
                for i in range(k):
                    assets.insert(0,row[3])     
            else:
                 j == int(row[2])
                 assets.insert(0,row[3])
    return assets

def analys_apriori(datar):
    freqItemSet, rules = apriori(datar, minSup=0.2, minConf=0.3)
    print(rules)
    print(freqItemSet)

def data_writer():
    j=0
    with open('dataset\BreadBasket.csv', mode='w', encoding='utf-8') as w_file:
        fieldnames=['Items']
        writer = csv.DictWriter(w_file, delimiter = ',',lineterminator='\r', fieldnames=fieldnames) 
        with open('dataset\BreadBasket_DMS.csv', newline='') as File:  
            reader = csv.reader(File,delimiter=',')
            for row in reader:
                assets=[]
                if j==int(row[2]):
                    assets.insert(0,row[3])
                else:
                    writer.writerow(assets)
                    j=int(row[2])
                    assets.clear()
                    assets.append(row[3])
    print('Writing complete')
              

def data_parser_lit(name):
    with open(name, newline='') as File:  
        transactions=[]
        reader = csv.reader(File,delimiter=',')
        for row in reader:
            transactions.append(row)
    return(transactions)

datar = []
datar=data_parser_lit('dataset\Basket.csv')     
data_writer() 
#print(datar)
#analys_apriori(datar)
