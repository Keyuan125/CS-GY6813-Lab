# My functions are case insensitive, i.e. "cookie" and "COOKIE" are the same

def encrypt(original_str, key):

    # If the key is less than 0, then I need to make it to a positive number.
    # 
    while key < 0:
        key += 26

    upper_str = original_str.upper()
    encrypted_str = ""

    for c in upper_str:
        if 65 <= ord(c) <= 90:
            new_ascii = ord(c) + key
            while new_ascii > 90:
                new_ascii = new_ascii - 91 + 65
            encrypted_str += chr(new_ascii)
        elif ord(c) == 32:
            encrypted_str += " "
        else:
            print("Unable to decrypt! Function only accepts alphabet and space!")
            return ""
    return encrypted_str

def decrypt(encrypted_str, key):
    while key < 0:
        key += 26

    upper_str = encrypted_str.upper()
    decrypted_str = ""

    for c in upper_str:
        if 65 <= ord(c) <= 90:
            new_ascii = ord(c) - key
            while new_ascii < 65:
                new_ascii = 90 - (64 - new_ascii)
            decrypted_str += chr(new_ascii)
        elif ord(c) == 32:
            decrypted_str += " "
        else:
            print("Unable to decrypt! Function only accepts alphabet and space!")
            return ""
    return decrypted_str 

# e = encrypt("First Test", 5)
# print(e)
# print(decrypt(e, 5))

# e = encrypt("Second Test", -5)
# print(e)
# print(decrypt(e, -5))

# e = encrypt("third Test", -100)
# print(e)
# print(decrypt(e, -100))

# e = encrypt("abcdefh", 1)
# print(e)
# print(decrypt(e, 1))

# e = encrypt("abcdefh", -1)
# print(e)
# print(decrypt(e, -1))