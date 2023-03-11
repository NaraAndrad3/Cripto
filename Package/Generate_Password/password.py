import string
import random
import hashlib

class Generate:
    def __init__(self) -> None:
        pass

    def password_letters(self,tam): 
        char = string.ascii_letters + 'ç' #cria uma string com todas as letras do alfabeto
        password = '' # string onde será criada a senha
        # vai escolher aleatoriamente um caractere da string char a partir do random.choice e ir 
        # concatenando até formar a senha do tamanho desejado
        for i in range(tam):
            password += random.choice(char) # a função choice retorna um elemnto aleatoria da string
        return password

    def pwd_LettersNumbers(self,tam): 
        char = string.ascii_letters + string.digits+'ç'#cria uma string com todas as letras do alfabeto
        password = '' # string onde será criada a senha
        # vai escolher aleatoriamente um caractere da string char a partir do random.choice e ir 
        # concatenando até formar a senha do tamanho desejado
        for i in range(tam):
            password += random.choice(char) # a função choice retorna um elemnto aleatoria da string
        return password
    
    def password_numbers(self,tam): 
        char = string.digits #cria uma string com "todos" os numeros
        password = '' # string onde será criada a senha
        # vai escolher aleatoriamente um caractere da string char e ir 
        # concatenando até formar a senha do tamanho desejado
        for i in range(tam):
            password += random.choice(char) # a função choice retorna um elemnto aleatoria da string
        return password #vai retornar uma senha numeria de tipo int 
    
    def pronounciable_pwd(self,tam):
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        password = ''
        for i in range(tam):
            if (i % 2 == 0):
                password += ''.join(random.choice(vowels))
            else:
                password += ''.join(random.choice(consonants))

        return password
    
    def punctuation(self,tam):
        char = string.punctuation + string.ascii_letters + string.digits + 'ç'

        password = ''
        for i in range(tam):
            password += ''.join(random.choice(char))
        
        return password

    