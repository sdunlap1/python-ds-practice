def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    bal_parens = 0

    for paren in parens:
        if paren == "(":
            bal_parens += 1
        elif paren == ")":
            bal_parens -= 1
        if bal_parens < 0:
            return False
    
    return bal_parens == 0