import os

def current_path() :   #showing the current directory
    print("The current directory is:" +' '+ os.getcwd())

current_path()

file_name = input("Please enter the file name you would like to write to:")  #User input on what file they want to use
name = file_name
file_path = os.getcwd()
complete_path = os.path.isfile(name)

if os.path.isdir(file_path): #check if the directory path exists
    print('Directory Exists')

else :
    print("Directory does not exist")


print("Please answer the following information to be added to your document")

name = input("Please enter your name:")    #getting user data
address = input('Please enter your address:')
city = input('City:')
state = input('State:')
zip_code = input('Zip Code:')
phone_number = input('Please enter your phone number with area code:')

print ("You entered the following:" + name + ' , ' + address + ' , ' + city + ' , ' + state + ' , ' + zip_code + ' , ' + phone_number)

list = open(file_name, 'a')    #writing user data to file
list.write(name + ' , ' + address + ' , ' + city + ' , ' + state + ' , ' + zip_code + ' , ' + phone_number)
list.close()
