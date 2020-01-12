class Stack:
    """
    Class implementing the abstract data type for collecting
    elements.
    """

    def __init__(self):
        self.stack = []

    def push(self, item):
        """
        Add an item to the stack.
        :param item: item to be added to stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Remove the most recently added item from the stack
        and return it.
        :return: most recently added item from the stack.
        """
       return self.stack.pop()

    def peek(self):
        """
        Return the most recently added item from the stack
        wothout removing it from the stack.
        :return: most recently added item from the stack.
        """
        return self.stack[-1]

    def is_empty(self):
        """
        Check if the stack is empty.
        :return: if stack is empty:---> True, else: ---> False
        """
       return len(self.stack) == 0
