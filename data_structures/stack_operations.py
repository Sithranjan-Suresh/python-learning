"""
Problem: Stack-based String Operations
--------------------------------------
1. Reverse a string using a stack (deque)
2. Check if parentheses/brackets/braces in a string are balanced
"""

from collections import deque

# ------------------ Reverse String ------------------
def reverse_string(word):
    """
    Reverse a string using a stack
    Steps:
    1. Push each character onto the stack
    2. Pop characters from the stack to build the reversed string
    """
    stack = deque()
    reversed_word = ""
    
    # Push all characters onto stack
    for ch in word:
        stack.append(ch)
    
    # Pop from stack to get reversed string
    while stack:
        reversed_word += stack.pop()
    
    return reversed_word

# ------------------ Balanced Parentheses ------------------
def does_match(open_char, close_char):
    """
    Check if the open and close characters match
    """
    matches = {
        "{": "}",
        "[": "]",
        "(": ")"
    }
    return matches[open_char] == close_char

def is_balanced(word):
    """
    Check if a string has balanced parentheses, brackets, and braces
    Steps:
    1. Push opening brackets onto stack
    2. For closing brackets, pop from stack and check if it matches
    3. Return True if stack is empty at the end, else False
    """
    stack = deque()
    
    for ch in word:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack:
                return False
            if not does_match(stack.pop(), ch):
                return False
    
    return len(stack) == 0

# ------------------ Demo ------------------
print(reverse_string("We will conquere COVID-19"))  # Reversed string
print(is_balanced("({a+b})"))                      # Expected: True
