import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special):
    character_pool = ''
    
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        return "Error: No character types selected!"

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Python Password Generator")

    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    print("\nSelect character types to include in your password:")
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits    = input("Include digits? (y/n): ").lower() == 'y'
    use_special   = input("Include special characters? (y/n): ").lower() == 'y'

    if length <= 0:
        print("Password length must be greater than 0.")
        return

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)
    print("\n✅ Your generated password is:\n")
    print(password)

if __name__ == "__main__":
    main()
