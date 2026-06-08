import re

def password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        strength += 1

    if strength <= 2:
        return "Weak Password"
    elif strength == 3 or strength == 4:
        return "Medium Password"
    else:
        return "Strong Password"

# Main Program
pwd = input("Enter Password: ")
result = password_strength(pwd)
print("Password Strength:", result)