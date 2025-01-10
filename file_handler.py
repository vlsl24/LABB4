import os
import file_safe as fs
import menues
from kryptography import encrypt_text,decrypt_text

   #Creates the safe folder where all files will be stored
if not os.path.exists("safe"):
    os.mkdir("safe")
    
    
    
os.chdir("safe")


#------------File functions------------#

    #check if file exists
def get_all_file_names():
    all_items = os.listdir()
    #Function bellow removes all non file entries from the list
    files_with_tails = [item for item in all_items if os.path.isfile(item)] 
    #Function bellow removes the .txt tail from the file names
    files  = [sub[: -4] for sub in files_with_tails]
    return files
   
    
    #function that handles the menu for file handling
   
def file_menue_handler(user_input):
    #print out all file names
    print(get_all_file_names())
    if(user_input=="1"): 
            create_file(input("Ange filens namn: "))  
            
    elif(user_input=="2"):
            read_file(input("Ange filens namn: "))
            
    elif(user_input=="3"):
            write_to_file(input("Ange filens namn: "))
            
    elif(user_input=="4"):
            delete_file(input("Ange filens namn: "))
            
    elif(user_input=="5"):
            os.chdir("..")
            print("Går tillbaka till huvudmenyn")    
            
    return None
    #create file
def create_file(file_name):
    #checks if file exists
    if fs.validate_choice(file_name,get_all_file_names())==file_name:
        print("Filen finns redan.")
    else:
        with open(file_name+".txt", 'w'): #creates the file
            print("Filen har skapats.")
            
    #read file    
def read_file(file_name):
    #checks if file exists
    if fs.validate_choice(file_name,get_all_file_names())==file_name:
        with open(file_name+".txt", 'r') as file: #opens the file
            try:
                print(kryptographer(file.read(),"decrypt"))
            except:
                print("Filen är tom.")
            
    else:
        print("Filen finns inte.")
        
    #write to file   
def write_to_file(file_name):
    #checks if file exists
    if fs.validate_choice(file_name,get_all_file_names())==file_name:
        with open(file_name+".txt", 'a') as file: #opens the file
            text=input("Skriv in texten som ska läggas till: ")
            file.write(kryptographer(text,"encrypt")) #writes to file
            print("Texten har lagts till.")
    else:
        print("Filen finns inte.")
        
    #delete file    
def delete_file(file_name):
    #checks if file exists
    if fs.validate_choice(file_name,get_all_file_names())==file_name:
        os.remove(file_name+".txt")#deletes the file
        print("Filen har tagits bort.")
    else:
        print("Filen finns inte.")        
        
#folowing function will encrypt and decrypt the file
#Why does it exist? Because this way i dont have to call 
#encrypton functions from all of the functions above
def kryptographer(text,mode):#mode is either "encrypt" or "decrypt"| text is the text to be encrypted or decrypted   
    
    """
    Example of use:
    kryptographer(text,"encrypt")
    kryptographer(text,"decrypt")
    """     
    if mode=="encrypt":
        return encrypt_text(text)
    elif mode=="decrypt":
        return decrypt_text(text)
        
        
                                
#------------Folder functions------------#
    #gives a list of all folders in the directory
def get_all_folder_names():
    all_items = os.listdir()
    #Function bellow removes all non directory entries from the list
    folders = [item for item in all_items if os.path.isdir(item)]
    return folders

    #function that handles the folder handling
def folder_handler(user_input):
    
#the following code is written in this way because 
#this is the only way i could imagine the code 
#to print out folders only when user needs to choose folders
# without having to repeat the code in every if statement

    #this if statement creates folder 
    if user_input == '1':
        create_folder(input("Ange mappens namn: "))
    else:
    #following code prints out all folders and asks user to choose a folder
    
        print(get_all_folder_names())
        folder_name = input("Ange mappens namn: ")
        #this if statement tree takes folder that user has chosen and    
        if user_input == '2':
            #opens it
            open_folder(folder_name)
        elif user_input == '3':
            #deletes it
            delete_folder(folder_name)
         
    return None
        
    #creates folder
def create_folder(folder_name):
    if fs.validate_choice(folder_name,get_all_folder_names())==folder_name:
        print("Mappen finns redan.")
    else:
        os.mkdir(folder_name)
        print("Mappen har skapats.")  
        
    #opens folder   
def open_folder(folder_name):
     
    if fs.validate_choice(folder_name,get_all_folder_names())==folder_name:
        os.chdir(folder_name)
        print("Mappen har öppnats.")
        menues.File_menu()
        
        
    else:
        print("Mappen finns inte.")
    
        
    #deletes folder
def delete_folder(folder_name):
    if fs.validate_choice(folder_name,get_all_folder_names())==folder_name:
        os.rmtree(folder_name, ignore_errors=False, onerror=None),
        print("Mappen har tagits bort.")
    
    else:
        print("Mappen finns inte.")
                  