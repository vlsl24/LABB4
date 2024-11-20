from file_safe import validate_choice

def create_folder():
    
    return None

def open_folder():
    return None
    
   


def Main_menu():
    loop=True
    while loop:
        print("1.skapa en ny mapp \n"
              "+2.öppna en mapp \n"
              "0.avsluta programmet")
        
        user_input= input("Välj ett alternativ: ")
        ALLOWED_CHOICES = ['1','2','0']
        
        if validate_choice(user_input,ALLOWED_CHOICES):
            if user_input == '1':
               create_folder()
    
            elif user_input == '2':
               open_folder()
           
            elif user_input == '0':
                print("Avslutar programmet")
                loop=False
            break
        else:
            print("Ogiltigt val, försök igen.")
             