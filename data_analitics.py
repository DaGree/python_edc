import apriori_python  #library for analys
import csv #library for usin csv-files


assets=[]
with open('dataset\BreadBasket_DMS.csv', newline='') as File:  
    reader = csv.reader(File,delimiter=',')
    for row in reader:  
        assets.append(row[3])
    
i = 1    
while i <= 10:
    print(i,' ',assets[i], ' ')
    #print()
    i=i+1