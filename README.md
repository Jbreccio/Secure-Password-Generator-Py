# 🔐 Secure Password Generator

A customizable password generator that creates secure passwords with different complexity criteria.

## 📋 Features

- 🔢 Password length control
- 🔤 Uppercase option
- 🔡 Lowercase option
- 🔢 Number option
- 🔣 Special symbol option
- 🚫 Ambiguous character removal
- 💾 Multiple password generation
- 🔍 Password strength check
- 📊 Security analysis

## 🛠️ Technologies Used

- Python 3.7+
- `random` module (native)
- `secrets` module (more secure)
- `string` module (native)

## 🚀 How to Run

1. Clone the repository
2. Navigate to the project folder
3. Run the command:
```bash
python main.py
```

## 📖 How to Use

1. Run the program
2. Set the password length
3. Choose the character types
4. Decide whether to exclude ambiguous characters
5. Choose how many passwords to generate
6. View the generated passwords and their analysis

## 🎯 Character Types

- **Uppercase**: A-Z
- **Lowercase**: a-z
- **Numbers**: 0-9
- **Symbols**: !@#$%^&*()_+-=[]{}|;:,.<>?

## 🚫 Ambiguous Characters (Optional)

- **Numbers**: 0, 1
- **Letters**: O, I, l (easily confused)

## 🔍 Strength Analysis

- 🔴 **Weak**: <8 characters or few types
- 🟡 **Medium**: 8-11 characters with varied types
- 🟢 **Strong**: 12+ characters with all types

## 🎯 Concepts Learned

- Secrets module (cryptographically secure)
- Random module
- String module
- String manipulation
- Input validation
- Complexity analysis
- Good security practices

## 📝 Usage Example

```
🔐 SECURE PASSWORD GENERATOR
Password length (8-128): 16
Include uppercase? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y
Exclude ambiguous characters? (y/n): y
How many passwords to generate? (1-10): 3

Generated Passwords:
1. Kp@9mVx7RtYw3#Nq (Strength: 🟢 Strong)
2. Bz$5fHj8LmPr2&Xs (Strength: 🟢 Strong)
3. Ck#4nQs9WtGv6!Zy (Strength: 🟢 Strong)
```

## 🔧 Future Improvements

- Saving passwords to a file
- Leak checking
- Word-based generation
- Graphical user interface
- Integration with password managers

## 📄 License

This project is licensed under the MIT license.
