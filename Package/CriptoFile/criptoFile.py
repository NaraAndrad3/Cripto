import hashlib
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class CriptoFiles:
    def __init__(self) -> None:
        pass

    def openFile(self,fileName):
        with open (fileName,'r') as f: # abre o arquivo 
            arq = f.read()
        return arq

    def encriptyFile(self,fileName):
        blocks = 16
        salt = 'ç'
        arq = self.openFile(fileName)
        encFile = fileName[:7] + '.enc' # nome do arquivo criptografado
        print(encFile)

        key = os.urandom(32) # gera uma senha aleatória 

        initVector = os.urandom(16) # gera um vetor de inicialização

        
        

        return 
        

       
        





