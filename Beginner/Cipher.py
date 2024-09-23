message = 'Hello Joseph'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789' 
encrypted_message = ''

for word in message.lower():
    if word == ' ':
        encrypted_message += word
    else:
        index = alphabet.find(word)
        # To avoid an error in script when the loop reaches the end of the  alphabet len variable and sum index + shift exceeds that 
        new_index = (index + shift) % len(alphabet)
        encrypted_message += alphabet[new_index]
    print('word:', word, 'encrypted message:', encrypted_message)