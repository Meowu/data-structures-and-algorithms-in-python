
def build_expr(tree):
    if tree.getLeft() is None:
        return str(tree.getRoot())
    else:
        return '(' + build_expr(tree.getLeft()) + str(tree.getRoot()) + build_expr(tree.getRight()) + ')'
