"""
AP Computer Science Principles - Python Challenge
Challenge: String Manipulation and Analysis

Description:
Write a Python program to analyze and manipulate strings according to AP CSP standards.
This challenge focuses on string methods, list operations, and algorithm design.

Problem:
1. Create a function that checks if a string is a palindrome (ignoring spaces and case)
2. Create a function that counts the frequency of each character
3. Create a function that performs basic cipher encryption (Caesar cipher)
4. Combine these functions to create a complete string analysis tool
"""

# Challenge 1: Palindrome Checker
def is_palindrome(text):
    """
    Check if a string is a palindrome.
    Args:
        text (str): The string to check
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    # Check if it equals its reverse
    return cleaned == cleaned[::-1]


# Challenge 2: Character Frequency Counter
def count_characters(text):
    """
    Count the frequency of each character in a string.
    Args:
        text (str): The string to analyze
    Returns:
        dict: Dictionary with character frequencies
    """
    frequency = {}
    for char in text.lower():
        if char != " ":
            frequency[char] = frequency.get(char, 0) + 1
    return frequency


# Challenge 3: Caesar Cipher
def caesar_cipher(text, shift):
    """
    Encrypt text using Caesar cipher.
    Args:
        text (str): The text to encrypt
        shift (int): Number of positions to shift
    Returns:
        str: Encrypted text
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result


# Main function to demonstrate all challenges
def main():
    print("=== AP CSP Python Challenge: String Analysis ===")
    print()
    
    # Test Palindrome
    test_strings = ["A man a plan a canal Panama", "hello", "racecar"]
    print("Palindrome Test:")
    for text in test_strings:
        print(f"  '{text}' is palindrome: {is_palindrome(text)}")
    print()
    
    # Test Character Frequency
    test_text = "programming"
    print(f"Character Frequency in '{test_text}':")
    freq = count_characters(test_text)
    for char, count in sorted(freq.items()):
        print(f"  '{char}': {count}")
    print()
    
    # Test Caesar Cipher
    original = "Hello World"
    shifted = caesar_cipher(original, 3)
    print(f"Caesar Cipher (shift=3):")
    print(f"  Original: {original}")
    print(f"  Encrypted: {shifted}")
    print()


if __name__ == "__main__":
    main()
