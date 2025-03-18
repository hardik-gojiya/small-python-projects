import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ""
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""

    all_characters = lower + upper + digits + special

    if not all_characters:
        print("Error: You must select at least one character type.")
        return ""

    password = "".join(random.choice(all_characters) for _ in range(length))
    return password


def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 4:
            print("Password length should be at least 4.")
            return

        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
        use_digits = input("Include digits? (y/n): ").lower() == "y"
        use_special = input("Include special characters? (y/n): ").lower() == "y"

        password = generate_password(length, use_uppercase, use_digits, use_special)
        if password:
            print(f"✅ Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for length.")


if __name__ == "__main__":
    main()
