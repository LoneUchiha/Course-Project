# Zachary Clerge 2/10/24 Ceis 150

import csv
import os
# METHODS AT TOP

def add_contact(file_name):
    with open(file_name, "a", newline= '') as addressCSVfile:
        addressWriter = csv.writer(addressCSVfile)  #create CSV writer
        
        #get record
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        
        #must be given as a list
        record = [name, phone]
    
        # write record using commas to seperate each field 
        addressWriter.writerow(record)

    print("\nRecord written successfully.")
    _ = input("\nPress Enter To continue...")

def show_contacts(file_name):
    # read from file
    print("\n\nAddress BookK\n")
    
    with open(file_name, mode = 'r') as addressCSVfile:
        datareader = csv.reader(addressCSVfile, delimiter=',')
        # next (datareader)
        for row in datareader:
            print(row[0], row[1])
            
    _ = input("\nPress Enter to continue...")
            

def find_contact(file_name):
    # get name to fine
    name = input("\nEnter name to find: ")
    
    with open(file_name, mode = 'r') as addressCSVfile:
        datareader = csv.reader(addressCSVfile, delimiter=',' )
        
        # next(datareader)
        for row in datareader:
            if row[0] == name:
                   print(row[0], row[1])
                             
    _= input("\nPress Enter to continue...")


# create our choice variable


def delete_contact(file_name):
    # get name to delete
    name = input("Enter name to delete ")
    
    #create flag (boolean) and set to false
    found = False
    
    # open old file to read data
   # Open a temp new file to write records to keep
    temp_name = file_name + "tmp"
    # notice the 'w on the output to overwrite any current data 
    with open(file_name, 'r') as inp, open(temp_name, 'w', newline='') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[0] == name:
                #flip the flag
                found = True
            else:
                # write the record to keep to the NEW file
                writer.writerow(row)
   # delete the original files and then rename the temporary NEW gile to the old name
    os.remove(file_name)
    os.rename(temp_name, file_name)
    
    # if the record is found tell the user
    if found == True:
        print("\n" + name + " was deleted. ")
    else:
        print("n\Error. " + name + "was not found. ")
        
    _=input("\nPress Enter to continue...")
    
    4


#address application using csv module " comma seperated values"
choice = 0

file_name = "address_book.csv"
# start the application loop that runs until user stops it 
while choice != 5:
    # show the menu
    print("\n\nAddress Book Menu\n")
    print("1) Add a contact ")
    print("2) Delete a contact")
    print("3) Find a contract")
    print("4) Show all contacts")
    print("5) Exit")
    
    # get user's choice
    choice = int( input("\nEnter your choice:") )
    
    # run code based on the user's choice 
    if choice == 1:
         add_contact(file_name)
    elif choice == 2:
         delete_contact(file_name)
    elif choice == 3:
         find_contact(file_name)
    elif choice == 4:
         show_contacts(file_name)
    elif choice == 5:
         print("\nGoodbye!")
    else:
         print("\nError. Please select from the menu. ")