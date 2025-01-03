from file_safe import validate_choice
import file_handler as fh


def Main_menu():
    
    while True:
       
        print("1.skapa en ny mapp \n"
              "2.öppna en mapp \n"
              "0.avsluta programmet")
        
        user_input= input("Välj ett alternativ: ")
        ALLOWED_CHOICES = ['1','2','0']
        
        if validate_choice(user_input,ALLOWED_CHOICES):
            if user_input != '0':
               fh.folder_handler(user_input)
    
            if user_input == '0':
                print("Avslutar programmet")
                break
            
        else:
            print("Ogiltigt val, försök igen.")
             