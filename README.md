# 🔐 Secret Message Encoder & Decoder (Python)

A simple Python project that encodes and decodes messages using a custom algorithm. This project demonstrates string manipulation, loops, and basic object-oriented programming in Python.

## 🚀 Features
Encode normal messages into secret code
Decode secret messages back to original text
Works with full sentences (multiple words)
Handles small and large words differently
Uses random characters for stronger encoding

## 🧠 How It Works
🔐 Encoding Rules

For each word in the message:

✅ If word length ≥ 3:

Remove the first letter
- Add it to the end
- Add 3 random letters at the beginning
- Add 3 random letters at the end
  
Example
```
hello → elloh → abcellohxyz
```
✅ If word length < 3:

- Simply reverse the word

🔓 Decoding Rules

To decode the message:

✅ If word length ≥ 3:

- Remove first 3 letters
- Remove last 3 letters
- Move last letter to the front

  Example
  ```
  abcellohxyz → elloh → hello
## 💡Concepts Used
- String slicing
- Lists and loops
- Functions and classes
- Random string generation
