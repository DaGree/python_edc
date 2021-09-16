import apriori_python  #library for analys
import csv #library for usin csv-files

i = 0
with open('D:\py_dev\dataset\BreadBasket_DMS.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        while i < 10:
            print(row)
            i=i+1    