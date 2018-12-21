
from .array_stack import ArrayStack


def reverse_file(filename):

    S = ArrayStack()
    with open(filename) as f:
        for line in f:
            S.push(line.rstrip('\n'))

    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()