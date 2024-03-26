def decrypt_caesar_cipher(encrypted_string, offset):
    decrypted_message = ''
    for char in encrypted_string:
        if char.isalpha(): # Check if the character is a letter
            # Determine the position of the character in the alphabet
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            # Decrypt the character by shifting it back by the offset
            decrypted_char = chr((ord(char) - base - offset) % 26 + base)
        else:
            # Keep non-alphabetic characters unchanged
            decrypted_char = char
        decrypted_message += decrypted_char
    return decrypted_message

## Example usage:
#encrypted_string = "Ifmmp xpsme!"
#for offset in range(26):
#    decrypted_message = decrypt_caesar_cipher(encrypted_string, offset)
#    print(f"Decrypted message with offset {offset}:", decrypted_message)

## Enter a single offset
#encrypted_string = input("Encrypted String: ")
#offset = input("Offset: ")
#decrypted_message = decrypt_caesar_cipher(encrypted_string, int(offset))
#print(decrypted_message)

## Loop through offsets 0-25
encrypted_string = input("Encrypted String: ")
for offset in range(26):
    decrypted_message = decrypt_caesar_cipher(encrypted_string, offset)
    print(f"Decrypted message with offset {offset}:", decrypted_message)