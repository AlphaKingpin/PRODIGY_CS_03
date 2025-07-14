# Password Strength Checker (Python)

This script checks the strength of a given password based on various criteria such as length, character diversity, and use of special characters. It provides a strength rating and helpful feedback to improve weak passwords.

## Features

- Evaluates password strength as Weak, Moderate, or Strong
- Checks for minimum and optimal length
- Verifies inclusion of lowercase, uppercase, numbers, and special characters
- Provides suggestions for improvement
- Easy-to-use command-line interface

## How It Works

The password is scored based on the following:

- Length: 
  - 12 or more characters: +2 points
  - 8–11 characters: +1 point
- Contains lowercase letters: +1 point
- Contains uppercase letters: +1 point
- Contains numbers: +1 point
- Contains special characters: +1 point

### Strength Levels

- 6 points: Strong
- 4–5 points: Moderate
- Below 4: Weak

## Usage Instructions

1. Run the script:
   ```bash
   python3 password.py
   ```

2. Input your password when prompted.

3. View the strength rating and feedback suggestions.

### Example

```
Enter your password to check its strength: cbE3xHB
Password Strength: Weak

Suggestions to improve:
 - Password is too short. Use at least 8 characters.
 - Include special characters (!@#$ etc).
```

```
Enter your password to check its strength: cbE3xHB4c12qwecbE3xHBoq4uh5n
Password Strength: Strong
```

## Requirements

- Python 3.x
- Standard `re` module (regular expressions)

## Author

Thywill Essel  
Innovative Male Entrepreneur | Python Developer | Founder of The WORD Expertise
