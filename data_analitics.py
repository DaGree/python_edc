import apriori_python  #library for analys
import csv #library for usin csv-files

with open('dataset\BreadBasket_DMS.csv', newline='') as File:  
    reader = csv.reader(File,delimiter=',')
    for row in reader:  
        print(row[3]) 
    print(row[3])