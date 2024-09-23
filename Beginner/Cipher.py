# Notes
'''
Variables defined outside a function have a global scope and they can be accessed from any part of your code.
Variables defined inside a function are local to that function and cannot be accessed outside of it.
'''

# This function receive two arguments: the non-encrypted message and the offset
def Caesar_Cipher(plain_message, offset): 
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789' 
    encrypted_message = ''

    for word in plain_message.lower():
        if word == ' ':
            encrypted_message += word
        else:
            index = alphabet.find(word)
            # To avoid an error in script when the loop reaches the end of the  alphabet len variable and sum index + shift exceeds that 
            new_index = (index + offset) % len(alphabet)
            encrypted_message += alphabet[new_index]
    
    print('plain message:', plain_message)
    print('encrypted message:', encrypted_message)

# Examples
message = 'Hello Joseph'

# Example 1 with offset as 3
Caesar_Cipher(message, 3)

# Example 2 with offset as 10
Caesar_Cipher(message, 10)

# Example 2 with offset as 13
Caesar_Cipher(message, 13)