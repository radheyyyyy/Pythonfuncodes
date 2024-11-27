import random
import string

def generate_password(length):
    # Define character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt user for password length
    try:
        length = int(input("Enter the desired length of the password (minimum 6 characters): "))
        
        if length <= 6:
            print("Password length must be at least 6 characters.")
            return
        
        # Generate password
        password = generate_password(length)
        
        # Display the password
        print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
