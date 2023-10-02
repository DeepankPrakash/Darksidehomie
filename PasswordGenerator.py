import random
import string

def generate_password(length):
    # Define the characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    if password_length < 1:
        print("Password length must be at least 1 character.")
    else:
        password = generate_password(password_length)
        print("Generated Password:", password)
