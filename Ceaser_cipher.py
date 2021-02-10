def encryption(plain_text,key):
    print("Plain text is: ",end="")
    plain_text = plain_text.replace(" ","")
    plain_text = plain_text.upper()
    print(plain_text.upper())
    cipher_text=""
    for i in range(len(plain_text)):
        char = plain_text[i]
        cipher_text+=chr(((ord(char)+key-65)%26)+65)
    return cipher_text

def decryption(cipher_text,key):
    print("Cipher text is: ",end="")
    cipher_text = cipher_text.replace(" ","")
    cipher_text = cipher_text.upper()
    print(cipher_text.upper())
    plain_text=""
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        plain_text+=chr(((ord(char)-key-65)%26)+65)
    return plain_text

choice=0
while choice!=3:
    print("1. Encryption\n2. Decryption\n3. Exit")
    choice = int(input("Enter the choice: "))
    if choice==1:
        plain_text = str(input("Please enter the plain text: "))
        key = int(input("Enter the key: "))
        cipher_text = encryption(plain_text,key)
        print("Encrypted text is: ",cipher_text)

    elif choice==2:
        cipher_text = str(input("Please enter the cipher text: "))
        key = int(input("Enter the key: "))
        plain_text = decryption(cipher_text,key)
        print("Decrypted text is: ",plain_text)

    elif choice==3:
        print("Thanks for using this code.")
        break

    else:
        print("Invalid choice!")