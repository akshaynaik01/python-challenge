"""
Challenge 2: Palindrome Checker

Write a program that checks if a given string is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters
that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Examples:
- "racecar" -> True
- "A man, a plan, a canal: Panama" -> True
- "hello" -> False
"""

def is_palindrome(s):
    """
    Check if a string is a palindrome.
    
    Args:
        s: The string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove spaces, punctuation, and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Check if it reads the same forwards and backwards
    return cleaned == cleaned[::-1]

# Test cases
if __name__ == "__main__":
    test_cases = [
        "racecar",
        "A man, a plan, a canal: Panama",
        "hello",
        "12321",
        "Python",
    ]
    
    for test in test_cases:
        result = is_palindrome(test)
        print(f'{test:35} -> {result}')
