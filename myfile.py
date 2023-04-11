import random
import string

def generate_password(length):
    """Generate a random password with the specified length."""
    # Use lowercase, uppercase, digits, and punctuation characters
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    # Generate a password using the specified length and characters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == '__main__':
    # Prompt the user to enter a password length
    length = int(input("Enter password length: "))
    # Generate and print a random password
    password = generate_password(length)
    print("Your random password is:", password)
