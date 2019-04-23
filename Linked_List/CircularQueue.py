# -*- coding: utf-8 -*-
# !/usr/bin/python3


class Empty(Exception):
    pass


class CircularQueue(object):

    class _Node(object):

        __slots__ = '_element', '_next'

        def __init__(self, element, _next):
            self._element = element
            self._next = _next

        @property
        def element(self):
            return self._element

        @property
        def next_el(self):
            return self._next

    def __init__(self):

        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        head = self._tail.next_el
        return head.element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        head = self._tail.next_el
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = head.next_el
        self._size -= 1
        return head.element

    def enqueue(self, e):
        new = self._Node(e, None)
        if self._size == 0:
            new._next = new
        else:
            new._next = self._tail.next_el
        self._size += 1
        self._tail = new

    def rotate(self):  # 不同于单向链表，从表头移动到表尾需要执行 dequeue 和 enqueue 两部操作，循环链表只需要把尾部指针指向它的下一个节点也即之前到头节点。
        if self._size > 0:
            self._tail = self._tail.next_el
