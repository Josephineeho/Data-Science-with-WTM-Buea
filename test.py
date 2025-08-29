import csv
with open("phoneNumbers.csv", newline='\n') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
    file.close()

with open("phoneNumbers.csv", mode='a', newline='\n') as file:
    writer = csv.writer(file)
    writer.writerow(['John', 30, 'New York'])  
    file.close() 

with open("phoneNumbers.csv", newline='\n') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
    file.close()