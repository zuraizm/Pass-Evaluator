import re

def password_strength(password):
    """
    Evaluates the strength of a password and provides suggestions for improvement.

    Args:
        password (str): The password to evaluate.

    Returns:
        A dictionary with the following keys:
            - strength (int): A score indicating the password strength (1-5).
            - suggestions (list): A list of suggestions for improving the password.
    """
    strength = 0
    suggestions = []

    # Check password length
    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long.")
    elif len(password) >= 12:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        suggestions.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        strength += 1
    else:
        suggestions.append("Password should contain at least one special character.")

    # Check for common patterns
    common_patterns = ["qwerty", "123456", "password", "iloveyou"]
    for pattern in common_patterns:
        if pattern in password.lower():
            suggestions.append(f"Password should not contain common patterns like '{pattern}'.")
            break

    # Evaluate password strength
    if strength < 3:
        strength = 1  # Weak
    elif strength == 3:
        strength = 2  # Medium
    else:
        strength = 3  # Strong
    if strength == 3 and len(password) >= 16:
        strength = 4  # Very Strong
    if strength == 4 and len(password) >= 20:
        strength = 5  # Extremely Strong

    return {"strength": strength, "suggestions": suggestions}

def main():
    password = input("Enter a password: ")
    result = password_strength(password)
    print(f"Password strength: {result['strength']}")
    if result['suggestions']:
        print("Suggestions for improvement:")
        for suggestion in result['suggestions']:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()
