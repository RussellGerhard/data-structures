"""
Author:  Russell Gerhard
Purpose: Evaluate simple algebra expressions in infix or postfix notation.
"""

from stacks import DoublyLinkedStack

def first_arg_precedes(op1, op2):
    """Check if first argument takes precedence over second in order of ops."""
    if op1 == '*':
        return True
    elif op1 == '/' and op2 != '*':
        return True
    elif op1 == '+' and op2 not in "*/":
        return True
    elif op1 == '-' and op2 == '-':
        return True
    else:
        return False

def eval_postfix(expr = "7 4 * 5 - 4 3 + *"):
    """
    Calculate value of postfix expression.

    Arg:
        expr (str): Whitespace-separated postfix expression.

    Returns:
        int: Value of expr.
    """
    # Check argument
    if type(expr) != str:
        raise TypeError("expr must be a string!")
    
    stack = DoublyLinkedStack()
    expr = expr.strip().split()
    
    for char in expr:
        if char.isdigit():
            stack.push(char)
        elif char in "*-+/":
            if len(stack) < 2:
                raise ValueError("Invalid expression!")
            op2 = float(stack.pop())
            op1 = float(stack.pop())
            if char == '*':
                stack.push(op1 * op2)
            elif char == '/':
                stack.push(op1 / op2)
            elif char == '+':
                stack.push(op1 + op2)
            else:
                stack.push(op1 - op2)
        else:
            raise ValueError("Invalid expression!")
        
    if len(stack) != 1:
        raise ValueError("Invalid expresion!")
    
    return float(stack.pop())

def infix_to_postfix(expr = "( 3 * 4 + 2 ) * 9 / 7 + 19"):
    """
    Translate whitespace-separated infix expression to postfix expression.

    Arg:
        expr (str): Whitespace-separated infix expression.

    Returns:
        str: Whitespace-separated postfix expression.
    """
    # Check argument
    if type(expr) != str:
        raise TypeError("expr must be a string!")
    
    op_stack = DoublyLinkedStack()
    result = ""
    expr = expr.strip().split()
    for char in expr:
        # append digits to result
        if char.isdigit():
            result += f" {char} "
        # push open bracket onto stack
        elif char == '(':
            op_stack.push(char)
        # pop higher precedence ops off stack and append to result
        # before pushing new op onto stack
        elif char in "*-+/":
            while not op_stack.is_empty():
                if first_arg_precedes(op_stack.peek(), char):
                    out = op_stack.pop()
                    result += f" {out} "
                else:
                    break
            op_stack.push(char)
        # pop and append ops to results until matching open bracket is found
        elif char == ')':
            if op_stack.is_empty():
                raise ValueError("Invalid expression!")
            out = op_stack.pop()
            while out != '(':
                result += f" {out} "
                if op_stack.is_empty():
                    raise ValueError("Invalid expression!")
                out = op_stack.pop()
        # bad inputs
        else:
            raise ValueError("Invalid expression!")

    # pop and append the rest of the ops
    while not op_stack.is_empty():
        result += f" {op_stack.pop()} "

    # if infix isn't valid, postfix won't be valid
    return result
    
def eval_infix(expr = "( 3 * 4 + 2 ) * 9 / 7 + 19"):
    """
    Calculate value of infix expression.

    Arg:
        expr (str): Whitespace-separated infix expression.

    Returns:
        int: Value of expr.
    """
    postfix_expr = infix_to_postfix(expr)
    return eval_postfix(postfix_expr)
