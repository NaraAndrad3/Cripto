import hashlib

def password_hash(pwd):
    """
           Função que recebe uma senha como entrada e retorna seu hash. A função usa o algoritmo de derivação de chave baseado em senha PBKDF2 com o algoritmo de hash SHA256 para gerar um hash seguro da senha fornecida.
           "sal" (salt) para aumentar a segurança do hash. O sal é um valor aleatório que é adicionado à senha antes de calcular o hash, o que torna mais difícil para um invasor pré-calcular o hash para uma determinada senha.

            
            Parameteres
            -----------
            pwd: int
                Tamanho da senha gerada
                   
            Returns
            -------
            passowrd:
                senha gerada como uma string
    """
    salt = b'somesalt' # Adicione um sal para aumentar a segurança do hash
    password = hashlib.pbkdf2_hmac('sha256', pwd.encode('utf-8'), salt, 100000)
    return password.hex()

