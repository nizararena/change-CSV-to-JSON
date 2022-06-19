import json 
import csv


#replace python/clients.csv with your own file
# replace your delimeter with the one you want ef ; : ...
with open("python/clients.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    next (reader)
    #for row in reader:
     #   print(row)

    data = { "clients": [] }
    
    for row in reader:
        
        #replace whats between '' with the value of the row
        
        data['clients'].append({"guid":
        row[0],"first":row[1],"last":row[2],"street":row[3],"zip":row[4],"zip":row[5]})
    with open("clients.json", "w") as f:
        json.dump(data, f, indent=4)