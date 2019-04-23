from .array_stack import ArrayStack


def is_match(expr):

    lefty = '({['
    right = ')}]'

    S = ArrayStack()

    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in right:
            if S.is_empty():
                return False
            if right.index(c) != lefty.index(S.pop()):  # 不能直接 return right.index(c) == lefty.index(S.pop())，匹配正确应该继续遍历。
                return False
    return S.is_empty()  # 是否全部都匹配上。