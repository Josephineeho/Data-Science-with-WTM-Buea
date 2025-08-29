import csv

print("Welcome to phonebook ")

def main():
    while(True):
        printMenu()
        selectedOption = int(input("Select option: "))
        if(selectedOption ==1):
            printPhoneNumbers()
        elif(selectedOption ==2):
            storePhoneNumber()
        elif(selectedOption==3):
            exit()
        else:
            print("Invalid option!")
        main()    
        

    
def printMenu():
    print("1. print all PhoneNumbers")
    print("2. store PhoneNumber")
    print("3. Exit")

def storePhoneNumber():
    name = input(" Enter name:")
    phoneNum = input(" Enter phone number:") 
    with open("phoneNumbers.csv", mode='a', newline ="\n") as file:
        writer = csv.writer(file)
        writer.writerow([name, phoneNum])
        file.close()
        print("Number saved successfully")

def printPhoneNumbers():
    with open("phoneNumbers.csv", mode="r", newline="\n") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

main()
