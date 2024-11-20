import os
#------------File functions------------#

    #check if file exists
def file_existance_check(file_name):
    if os.path.exists(file_name):
        return True
    #create file
def create_file(file_name):
    if file_existance_check(file_name):
        print("Filen finns redan.")
    else:
        with open(file_name, 'w') as file:
            print("Filen har skapats.")
    #read file    
def read_file(file_name):
    if file_existance_check(file_name):
        with open(file_name, 'r') as file:
            print(file.read())
    else:
        print("Filen finns inte.")
        
    #write to file   
def write_to_file(file_name, text):
    if file_existance_check(file_name):
        with open(file_name, 'a') as file:
            file.write(text)
            print("Texten har lagts till.")
    else:
        print("Filen finns inte.")
        
    #delete file    
def delete_file(file_name):
    if file_existance_check(file_name):
        os.remove(file_name)
        print("Filen har tagits bort.")
    else:
        print("Filen finns inte.")        
                                
#------------Folder functions------------#

    #check if folder exists
def folder_existance_check(folder_name):
    if os.path.exists(folder_name):
        return True
    
    #create folder
def create_folder(folder_name):
    if folder_existance_check(folder_name):
        print("Mappen finns redan.")
    else:
        os.mkdir(folder_name)
        print("Mappen har skapats.")  
        
    #open folder   
def open_folder(folder_name):
    if folder_existance_check(folder_name):
        os.chdir(folder_name)
        print("Mappen har öppnats.")
    else:
        print("Mappen finns inte.")
                  