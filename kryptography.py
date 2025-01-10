from cryptography.fernet import Fernet
KEY="VV8d1GYYBokbjOopvhEl47LfGpOMkwGI53o1VQeXIDQ=" #encryption key
F=Fernet(KEY) #Fernet obj
def encrypt_text(text):
    #encrypted message
    text=text.encode()#converts text to bytes
    token=F.encrypt(text)#encrypts the text
    token=token.decode()#converts bytes to string
    return token #returns the encrypted text

def decrypt_text(text):
    #decrypted message
    #text=text.encode()#converts text to bytes
    token=F.decrypt(text) #decrypts the text
    token=token.decode()#converts bytes to string
    return token 
    