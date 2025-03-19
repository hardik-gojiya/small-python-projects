plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key: (1-25) "))


def encrypt(plaintext, key):
    ciphertext= ""
    
    for char in plaintext:
        if char.isalpha() and char.islower():
            ciphertext += chr((ord(char) +key -97) % 26 + 97)
        elif char.isalpha() and char.isupper():
            ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        else:
            ciphertext += char
    
    return ciphertext
    


print(f"Ciphertext: {encrypt(plaintext, key)}")
