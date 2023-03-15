from cryptography.fernet import Fernet #biblioteca que fornece suporte a algoritmos de criptografia
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64



class FilesDec:
    """
        Esta classe define uma classe chamada FilesDec, que contém métodos para criptografar e descriptografar arquivos com uma chave gerada a partir de uma senha.

        Attributes
        ----------

        Esta classe python não possui atributos.

        
        Methods
        -------
        __init__(self):
            é um método especial que é executado quando um objeto é criado a partir da classe. Neste caso, ele não faz nada.
        encryptPassword(pwd):
            recebe uma senha como parametro e gera uma chave de criptografia.
        extensionChange(filename):
            recebe um arquivo como parametro.
        encryptFile(filename, pwd):
            recebe um arquivo criptografado e uma senha como paramentro.
        decryptFiles(filename, pwd):
            recebe um aquivo criptografado como parametro e uma senha como entrada para criptografar a senha.
        decryptFiles(filename, pwd):
            recebe um aquivo criptografado como parametro e uma senha como entrada para descriptografar a senha.
    """

    def _init_(self):
        pass

    def encryptPassword(self, pwd):
        """
            Recebe uma senha como entrada e usa a biblioteca cryptography para gerar uma chave de criptografia a partir dessa senha. A chave é retornada na forma de uma string codificada.

            Parameteres
            -----------
            pwd: str
                senha a ser criptografada.
                   
            Returns
            -------
            kye:
                Retrona a chave a ser usada na função 'encryptFile(filename, pwd)'
        """
        password = pwd.encode()
        salt = bytes('ç/@&%)+LK~qer!?#(<>:;/\|-','utf-8')
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key

    def extensionChange(self, filename):
        """
            O método extensionChange recebe o nome de um arquivo como entrada e retorna o nome do arquivo sem sua extensão.

            Parameteres
            -----------
            filename: str
                senha a ser criptografada.
                   
            Returns
            -------
            file:
                Retorna o nome do arquivo sem sua extensão
        """
        file = ""
        for i in filename:
            if i == ".":
                break
            else:
                file += i

        return file

    def encryptFile(self, filename, pwd):
        """
            Este método criptografa um arquivo com uma senha e retorna o nome do arquivo de chave. Ele usa o encryptPassword()método para derivar uma chave da senha de entrada e, em seguida, grava a chave em um arquivo com o mesmo nome do arquivo de entrada, mas com uma extensão ".key". Por fim, ele usa o algoritmo de criptografia para criptografar o arquivo de entrada com a chave derivada e salva os dados criptografados no mesmo arquivo  

            Parameteres
            -----------
            filename: str
                arquivo para ser criptografado
            pwd: str
                senha criptografada 

                   
            Returns
            -------
            fileKey:
                Retorna o arquivo criptografado com a extensão .key
        """
        encryptKey = self.encryptPassword(pwd)

        fileKey = self.extensionChange(filename) + ".key"

        with open(fileKey, "wb") as fileK:
            fileK.write(encryptKey)

        with open(filename, "rb") as f:
            file = f.read()

        enc = Fernet(encryptKey)
        encriptedData = enc.encrypt(file)
        with open(filename, "wb") as encryptyFile:
            encryptyFile.write(encriptedData)
        
        return fileKey

    def decryptFiles(self, filename, pwd):
        """
            Este método descriptografa um arquivo com uma senha. Ele usa o encryptPassword()método para derivar uma chave da senha de entrada e, em seguida, lê a chave de um arquivo com o mesmo nome do arquivo de entrada, mas com uma extensão ".key". Se a chave derivada não corresponder à chave armazenada no arquivo de chave, o método imprimirá uma mensagem de erro. Caso contrário, ele usa o algoritmo de criptografia simétrica Fernet para descriptografar o arquivo de entrada com a chave derivada e salva os dados descriptografados no mesmo arquivo.

            Parameteres
            -----------
            filename: str
                arquivo para ser criptografado
            pwd: str
                senha usada encriptar e decriptar o arquivo.
                   
            Returns
            -------
            Sem retorno
        """
        
        fileKey = self.extensionChange(filename) + ".key"

        with open(fileKey, "rb") as fk:
            key = fk.read()

        encriptedKey = self.encryptPassword(pwd)
        if encriptedKey != key:
            print('Erro ao descriptar arquivo. senha incorreta')
        else:
            enc = Fernet(key)

            with open(filename, "rb") as f:
                file = f.read()

                decryptedData = enc.decrypt(file)

            with open(filename, "wb") as fileDecrypted:
                fileDecrypted.write(decryptedData)




