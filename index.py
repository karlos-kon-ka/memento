import random
from werkzeug.security import generate_password_hash

minus = 'abcdefghijklmnñopqrstuvwxyz'
mayus = minus.upper()
simbolos = '@!()?¿,.'
numeros = '0123456789'
base = minus+mayus+simbolos+numeros
longitud = 12 

for _ in range(10):
    muestra = random.sample( base, longitud)
    password = "".join(muestra)
    encriptacion = generate_password_hash(password)
    print("{} → {}".format(password,encriptacion))

