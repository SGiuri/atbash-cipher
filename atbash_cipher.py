import re


def encode(plain_text):
    clear_text = re.sub(f"[^a-zA-Z0-9\']", "", plain_text).lower()

    encrypted_text_string = ""

    for letter in clear_text:
        try:
            int(letter)
            encrypted_text_string += letter
        except:

            x = ord("z") - (ord(letter) - ord("a"))

            encrypted_text_string += chr(x)
    print(clear_text, encrypted_text_string)
    encrypted_text = " ".join([encrypted_text_string[j:j + 5] for j in range(0, len(encrypted_text_string), 5)])
    return encrypted_text


def decode(ciphered_text):
    clean_ciphered_text = re.sub(f"[^a-zA-Z0-9\']", "", ciphered_text).lower()

    decrypted_text_string = ""

    for letter in clean_ciphered_text:
        try:
            int(letter)
            decrypted_text_string += letter
        except:

            y = ord("a") - (ord(letter) - ord("z"))

            decrypted_text_string += chr(y)

    return decrypted_text_string
