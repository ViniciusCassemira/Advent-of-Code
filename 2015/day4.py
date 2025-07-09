import hashlib

secret_key = "bgvyzdsv"
prefix = "000000"
concat_number = 1
hash_found = False

def criptografar_md5(text):
    hash_md5 = hashlib.md5()
    hash_md5.update(text.encode('utf-8'))
    return hash_md5.hexdigest()

while not hash_found:
    attempt = secret_key + str(concat_number)
    hash_md5 = criptografar_md5(attempt)
    if hash_md5.startswith(prefix):
        print(f"Hash found: {hash_md5}")
        print(f"1º number:{concat_number}")
        hash_found = True
    else:
        concat_number += 1