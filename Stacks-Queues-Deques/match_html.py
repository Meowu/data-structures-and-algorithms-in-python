
from .array_stack import ArrayStack


def is_matched_html(raw):

    S = ArrayStack()
    b = raw.find('<')
    while b != -1:
        c = raw.find('>', b + 1)
        if c == -1:
            return False
        tag = raw[b+1:c]
        if not tag.startswith('/'):  # 开始标签。
            S.push(tag)
        else:
            if S.is_empty():  # 结束标签没有匹配的开始标签名。
                return False
            if tag[1:] != S.pop():  # 匹配开始结束标签。
                return False
        b = raw.find('<', c+1)
    return S.is_empty()