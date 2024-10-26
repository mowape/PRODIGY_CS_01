def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, s):
    return encrypt(text, -s)

while True:
    print("\nChoose an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        text = input("Enter the text to encrypt: ")
        s = int(input("Enter the shift value: "))
        print("Encrypted Text: " + encrypt(text, s))

    elif choice == '2':
        text = input("Enter the text to decrypt: ")
        s = int(input("Enter the shift value: "))
        print("Decrypted Text: " + decrypt(text, s))

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
