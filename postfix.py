from stack import Stack


operators = ['+', '-', '*', '/']
stack = Stack()

def evaluate_postfix(expression):
    """
    Evaluate a given postflix expession.
    :param expression: postflix expression to be evaluated.
    :return: evaluated postflix expession.
    """
    for token in expression.split():
        if token not in operators:
            stack.push(token)
        else:
            op2 = int(stack.pop())
            op1 = int(stack.pop())

            if token == '+':
                op = op1 + op2
            elif token == '-':
                op = op1 - op2
            elif token == '*':
                op = op1 * op2
            elif token == '/':
                op = op1 / op2

            stack.push(op)
    return stack.pop()

def user_input_expression(expression):
    """
    Evaluate a user given postflix adhering to the format given in expession,
    i.e if expression is of the form a b c + - the user will be asked to input
    values for a, b and c and the resuling expression is evaluated.
    :param expression: format of the postflix expression to be evaluated.
    :return: evaluated postflix expession.
    """
    tokens = expression.split()
    user_in =\
            [input(f'Input a number for variable {token}: ')\
                                for token in tokens if token.isalpha()]
    postflix = ' '.join(user_in + tokens[len(user_in):])
    return evaluate_postfix(postflix)



if __name__ == "__main__":
    print(evaluate_postfix("2 3 1 * + 9 -"))
    print(evaluate_postfix("1 2 4 * +"))
    print(evaluate_postfix("2 3 + 1 4 + *"))
    print(evaluate_postfix("4 5 + 3 *"))
    print(evaluate_postfix("4 2 3 * +"))
    print(evaluate_postfix("10 2 3 * -"))
    print(evaluate_postfix("10 2 - 3 *"))

    print(user_input_expression("a b d + -"))
