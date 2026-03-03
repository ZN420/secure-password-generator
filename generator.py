import random
import string

def generate_password():
    print("--- SECURE PASSWORD GENERATOR v1.0 ---")
    
    # As per Admiral's style: fixed input logic
    try:
        length = int(input("Enter password length (e.g., 12): "))
    except ValueError:
        print("Invalid input! Defaulting to 12 characters.")
        length = 12

    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    all_chars = letters + digits + symbols
    
    # Logic to ensure at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the length
    password += random.choices(all_chars, k=length-3)
    
    # Shuffle for randomness
    random.shuffle(password)
    
    result = "".join(password)
    print(f"\nYour Secure Password: {result} 🛡️")

if __name__ == "__main__":
    generate_password()
