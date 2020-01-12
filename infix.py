from stack import Stack


precedence = {'*':3, '/':3, '+':2, '-':2, '(':1}
stack = Stack()

def convert_infix_to_postfix(expression):
    """
    Function converting inflix expression to postflix
    :param expression: string inflix expression to be convertd to postflix.
    """
    out = []
    for token in expression.split():
        if token not in precedence and token != ')':
            out.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            element = stack.pop()
            while element != '(':
                out.append(element)
                element = stack.pop()
        else:
            pre = precedence[token]
            while not stack.is_empty() and precedence[stack.peek()] >= pre:
                out.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        out.append(stack.pop())

    return ' '.join(out)


if __name__ == "__main__":
    assert convert_infix_to_postfix("2 + 3 * 1 - 9") == "2 3 1 * + 9 -"
    print(convert_infix_to_postfix("2 + 3 * 1 - 9"))
    assert convert_infix_to_postfix("1 + 2 * 4") == "1 2 4 * +"
    print(convert_infix_to_postfix("1 + 2 * 4"))
    assert convert_infix_to_postfix("( 2 + 3 ) * ( 1 + 4 )") == "2 3 + 1 4 + *"
    print(convert_infix_to_postfix("( 2 + 3 ) * ( 1 + 4 )"))
    assert convert_infix_to_postfix("( 4 + 5 ) * 3") == "4 5 + 3 *"
    print(convert_infix_to_postfix("( 4 + 5 ) * 3"))
    assert convert_infix_to_postfix("4 + 2 * 3") == "4 2 3 * +"
    print(convert_infix_to_postfix("4 + 2 * 3"))
    assert convert_infix_to_postfix("10 - 2 * 3") == "10 2 3 * -"
    print(convert_infix_to_postfix("10 - 2 * 3"))
    assert convert_infix_to_postfix("10 - ( 2 * 3 )") == "10 2 3 * -"
    print(convert_infix_to_postfix("10 - ( 2 * 3 )"))
    assert convert_infix_to_postfix("( 10 - 2 ) * 3") == "10 2 - 3 *"
    print(convert_infix_to_postfix("( 10 - 2 ) * 3"))
