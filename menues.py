from file_safe import validate_choice
import file_handler as fh


def File_menu():
    
    while True:
    
        print(  "\n1.skapa en ny fil \n"
                "2.Läs en  befintlig fil \n"
                "3.Lägg till text i en befintlig fil \n"
                "4.ta bort en fil \n"
                "5.gå tillbaka till huvudmenyn")
        user_input= input("Välj ett alternativ: ")
        ALLOWED_CHOICES = ["1","2","3","4","5"]
    
        if validate_choice(user_input, ALLOWED_CHOICES):
            if user_input == "5":
                fh.file_menue_handler(user_input)
                break
            
            else:
                fh.file_menue_handler(user_input)
    
    return None


def Main_menu():
    
    
    while True:
       
        print("1.skapa en ny mapp \n"
              "2.öppna en mapp \n"
              "3.radera en mapp \n"
              "0.avsluta programmet")
        
        user_input= input("Välj ett alternativ: ")
        ALLOWED_CHOICES = ["1","2","3","0"]
        
        if validate_choice(user_input,ALLOWED_CHOICES):
            if user_input != "0":
                fh.folder_handler(user_input)
                
            if user_input == "0":
                print("Avslutar programmet")
                break
            
            
        else:
            print("Ogiltigt val, försök igen.")
            
    return None            
         
             