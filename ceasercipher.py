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

text = input("Enter the text to encrypt: ")
s = int(input("Enter the shift value: "))

print("Text  : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))
