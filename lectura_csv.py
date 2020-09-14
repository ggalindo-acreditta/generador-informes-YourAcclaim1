import csv
import requests

with open('prueba_formato.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
        




with open ('new_names.csv','w') as f:
    writer = csv.DictWriter(f, fieldnames=["fruit", "count"])
    writer.writeheader()
    writer.writerow({'fruit':'prohibida','count':'666'})
    f.close()
    
    
