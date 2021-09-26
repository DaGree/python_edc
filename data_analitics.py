import csv #library for us in csv-files
#from apriori_python import apriori #lib foor analys
from efficient_apriori import apriori
from fpgrowth_py import fpgrowth
import pandas as pd

def analys_efficient_apriori(datar):
    freqItemSet, rules = apriori(datar, min_support=0.01, min_confidence=0.01) #minSup=0.05, minConf=0.001 min_support=0.01, min_confidence=0.01
    rules_rhs=filter(lambda rule: len(rule.lhs)==1 and len(rule.rhs)==1,rules)
    for rule in sorted(rules_rhs, key=lambda rule: rule.confidence):
        print(rule)
    print(rules)
    print()
    print(freqItemSet)

def analys_fpgrowth(datar):
    freqItemSet, rules = fpgrowth(datar, minSupRatio=0.5, minConf=0.5)
    print(rules)

def analys_apriori(datar):
    freqItemSet, rules = apriori(datar, minSup=0.05, minConf=0.001) #minSup=0.05, minConf=0.001 min_support=0.01, min_confidence=0.01
    print(rules)
    print()
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
                with open('dataset\BreadBasket.csv', mode='a', newline='') as e_file:
                    e_writer = csv.writer(e_file, delimiter=',')
                    e_writer.writerow(assets) 
                #print(assets)
                j=int(row[2])
                assets.clear()
                assets.append(row[3])
    e_file.close
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
#data_parser('dataset\BreadBasket_DMS.csv') 
datar=data_reader('dataset\BreadBasket.csv')   
#print(datar)
analys_efficient_apriori(datar)
