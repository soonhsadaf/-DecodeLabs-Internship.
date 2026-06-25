import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."

    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*")

    remaining = ''.join(
        random.choice(
            string.ascii_letters +
            string.digits +
            "!@#$%^&*"
        )
        for _ in range(length - 4)
    )

    password_list = list(lowercase + uppercase + digit + special + remaining)
    random.shuffle(password_list)

    return ''.join(password_list)

print("=" * 50)
print("      RANDOM PASSWORD GENERATOR")
print("=" * 50)

try:
    length = int(input("Enter password length: "))
    password = generate_password(length)

    print("\nGenerated Password:")
    print(password)

except ValueError:
    print("Please enter a valid number.")
