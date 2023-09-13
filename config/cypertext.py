from cryptography.fernet import Fernet

class cypertext:
    
    key = None

    def __init__(self,key=None):
        self.key = key

    def encrypt(self,password=None):
        key = Fernet.generate_key()
        secret_key = Fernet(key)
        password = secret_key.encrypt(bytes(password, encoding='ASCII'))
        return key.decode(), password.decode()
    
    def encryptkey(self,key=None, password=None):
        secret_key = Fernet(key)
        password = secret_key.encrypt(password)
        return password

    def decrypt(self, key= None, password=None):
        secret_key = Fernet(key)
        password = secret_key.decrypt(password)
        return password
    
    def ascii(self,text=None):
        text = bytes(text, encoding='ASCII')
        return text

    def issame(self, input_password=None, key=None, password=None):
        secret_key = Fernet(key)
        password = secret_key.decrypt(password)

        result = False
        input_password = bytes(input_password, encoding='ASCII')
        
        if input_password == password:
            result = True

        return result
