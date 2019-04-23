import operator


def evaluate(tree):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left = tree.getLeft()
    right = tree.getRight()
    if left and right:
        val = tree.getRoot()
        fn = operators[val]
        return fn(evaluate(left), evaluate(right))
    else:
        return tree.getRoot()  # 叶节点则返回当前的值。
