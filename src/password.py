import string
import random
import hashlib

from random import sample

class Generate:
    """
        A classe Generate possui seis métodos para gerar senhas com diferentes características. 

        Attributes
        ----------
        __init__: None
            Este é o construtor da classe Generate e não possui argumentos. Ele apenas inicializa a classe.
      
        Methods
        -------
        password_letters(tam: int):
            Este método gera uma senha composta apenas por letras maiúsculas e minúsculas
        pwd_LettersNumbers(tam: int):
            Este método gera uma senha composta apenas por letras maiúsculas e minúsculas
        password_numbers(tam: int):
            Este método gera uma senha composta apenas por dígitos. O tamanho da senha é especificado pelo argumento tam.
        noRepetition(tam: int):
            Este método gera uma senha numérica sem repetições de caracteres. O tamanho da senha é especificado pelo argumento tam.
        pronounciable_pwd(tam: int):
            Este método gera uma senha pronunciável, alternando vogais e consoantes. O tamanho da senha é especificado pelo argumento tam.
        punctuation(tam: int):
            Este método gera uma senha composta por caracteres de pontuação, letras maiúsculas e minúsculas, dígitos e a letra "ç". O tamanho da senha é especificado pelo argumento tam. 
    """
    def __init__(self) -> None:
        pass

    def password_letters(self,tam): 
        """
            Este método gera uma senha composta apenas por letras maiúsculas e minúsculas, incluindo a letra "ç". O tamanho da senha é especificado pelo argumento tam.


            Parameteres
            -----------
            tam: int
                Tamanho da senha gerada
                   
            Returns
            -------
            passowrd:
                senha gerada
        """
        char = string.ascii_letters + 'ç' 
        password = ''
        for i in range(tam):
            password += random.choice(char) 
        return password

    def pwd_LettersNumbers(self,tam):
        """
            Este método gera uma senha composta apenas por letras maiúsculas e minúsculas, incluindo a letra "ç". O tamanho da senha é especificado pelo argumento tam.


            Parameteres
            -----------
            tam: int
                Tamanho da senha gerada
                   
            Returns
            -------
            tam:int
                senha gerada
        """ 
        char = string.ascii_letters + string.digits+'ç'
        password = '' 
        for i in range(tam):
            password += random.choice(char)
        return password
    
    def password_numbers(self,tam):
        """
            Este método gera uma senha composta apenas por dígitos. O tamanho da senha é especificado pelo argumento tam.

            Parameteres
            -----------
            tam: int
                Tamanho da senha gerada
                   
            Returns
            -------
            passowrd:
                senha gerada
        """ 
        char = string.digits 
        password = '' 
        for i in range(tam):
            password += random.choice(char) 
        return password  
    

    def noRepetition(self, tam):
        """
            Este método gera uma senha numérica sem repetições de caracteres. O tamanho da senha é especificado pelo argumento tam.
            
            Parameteres
            -----------
            tam: int
                Tamanho da senha gerada
                   
            Returns
            -------
            tam:
                senha gerada como uma string
        """ 

        passWordNumeric = sample(range(tam), tam)
        strPassWord = ''.join(map(str, passWordNumeric))
        return strPassWord
    
    
    def pronounciable_pwd(self,tam):
        """
            Este método gera uma senha pronunciável, alternando vogais e consoantes. O tamanho da senha é especificado pelo argumento tam.       
            
            Parameteres
            -----------
            tam: int
                Tamanho da senha gerada
                   
            Returns
            -------
            passowrd:
                senha gerada como uma string
        """
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
        """
            Este método gera uma senha pronunciável, alternando vogais e consoantes. O tamanho da senha é especificado pelo argumento tam.       
            
            Parameteres
            -----------
            tam: int
                Tamanho da senha gerada
                   
            Returns
            -------
            passowrd:
                senha gerada como uma string
        """
        char = string.punctuation + string.ascii_letters + string.digits + 'ç'

        password = ''
        for i in range(tam):
            password += ''.join(random.choice(char))
        
        return password

    