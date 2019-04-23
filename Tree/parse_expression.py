from .BinaryTree import BinaryTree


def parse_expr(expression):
    n = expression
    stacks = []
    current = BinaryTree(None)
    for i in n:
        if i == '(':
            current.insertLeft(None)
            parent = current
            stacks.append(parent)
            current = current.getLeft()
        elif i.isdigit():
            current.setRoot(int(i))
            current = stacks.pop()
        elif i in ['+', '-', '*', '/']:
            if current.getRoot():
                t = BinaryTree(i)
                t.insertRight(None)
                t.left = current
                if len(stacks):
                    p = stacks[-1]
                    if p.left == current:
                        p.left = t
                    else:
                        p.right = t
                    stacks.append(t)
                    current = t.getRight()
                else:
                    t.left = current
                    stacks.append(t)
                    current = t.getRight()
            else:
                current.setRoot(i)
                current.insertRight(None)
                stacks.append(current)
                current = current.getRight()
        elif i == ')':
            if len(stacks):
                current = stacks.pop()
            else:
                print('finished.')
        else:
            raise ValueError
    return current, stacks


if __name__ == '__main__':
    expr, s = parse_expr('(3*(4+5))')
    print(expr.getRoot(), expr.getLeft().getRoot(), len(s))
