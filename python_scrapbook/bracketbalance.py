"""
Author:  Russell Gerhard
Purpose: Provide function for checking whether brackets balance in a string.
"""

from stacks import DoublyLinkedStack
from lists import ArrayList

def bracket_balance(expr: str = "mylist = ['a', {}, ['b']]",
                    open_brackets: list = ['[', '}'],
                    close_brackets: list = [']', '}']) -> False:
    """
    Check that all brackets in the expression string input are balanced.
    If balanced, return True, else return False.
    """

    # Instantiate stack and decide on what we consider to be brackets
    stack = DoublyLinkedStack()
    
    for char in expr:
        if char in open_brackets:
            stack.push(char)
        elif char in close_brackets:
            if stack.is_empty():
                return False
            open_brack = stack.pop()
            index = open_brackets.index(open_brack)
            if char != close_brackets[index]:
                return False
    if stack.is_empty():
        return True
    else:
        return False

if __name__ == "__main__":
    openers = input("Enter all characters considered to be open brackets:\n")
    print("Okay, considering these to be open brackets:")
    open_brackets = list(openers)
    for char in open_brackets:
        print(char)
    print()

    msg = "Enter all characters considered to be close brackets in \
the same order as their corresponding open brackets were entered:\n"
    closers = input(msg)

    # Catch errors
    if len(openers) != len(closers):
        raise ValueError("Length of opening and closing brackets lists must match.")
    
    print("Okay, considering these to be close brackets:")
    close_brackets = list(closers)
    for char in close_brackets:
        print(char)
    print()
    
    expr = input("Enter a bracketed expression:\n")
    if bracket_balance(expr, open_brackets, close_brackets):
        print("OK")
    else:
        print("Not OK")
    
            
    
