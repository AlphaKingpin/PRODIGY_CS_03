import re

def check_password_strength(password):
    feedback = []
    score = 0

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Consider using more than 12 characters for a stronger password.")
    else:
        feedback.append("Password is too short. Use at least 8 characters.")

    # Check for lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include lowercase letters.")

    # Check for uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include uppercase letters.")

    # Check for digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include numbers.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include special characters (!@#$ etc).")

    # Determine strength level
    if score >= 6:
        strength = "🟢 Strong"
    elif score >= 4:
        strength = "🟡 Moderate"
    else:
        strength = "🔴 Weak"

    print(f"Password Strength: {strength}")
    if feedback:
        print("\nSuggestions to improve:")
        for item in feedback:
            print(f" - {item}")

# Example usage
password = input("Enter your password to check its strength: ")
check_password_strength(password)
