import random

# import pyminizip as pyminizip


def generate_password():
    password_length = 10
    possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    random_character_list = [random.choice(possible_characters) for i in range(password_length)]
    random_password = "".join(random_character_list)
    return random_password


def zip_file(file: str):
    zip_filename = f"{file[:-4]}.zip"
    password = generate_password()
    # pyminizip.compress(file, None, zip_filename, password, int(1))
    return zip_filename, password
