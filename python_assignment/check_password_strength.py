import re

def check_password_strength(password):
    # minimum length check
    if len(password) < 8:
        return False
    
    # Uppercase and Lowercase Letters check
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False
    
    # Digit check
    if not any(char.isdigit() for char in password):
        return False
    
    # Special characters check
    if not re.search("[!@#$%^&*]", password):
        return False
    
    # If all criteria are met
    return True

# Get the user Input for password
user_password = input("Vlearn@123")

# Check password strength
if check_password_strength(user_password):
    print("Password is strong")
else:
    print("Password does not meet the criteria. Please ensure it has at least 8 characters, both uppercase and lowercase letters, at least one digit, and at least one special character.")
