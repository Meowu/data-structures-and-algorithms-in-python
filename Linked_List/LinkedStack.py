# -*- coding: utf-8 -*-
# !/usr/bin/python


class Empty(Exception):
    pass


class LinkedList(object):  # use ultimate object class as parent class is introduced new-style class since python 2.2

    class _Node(object):

        __slots__ = '_element', '_next'

        def __init__(self, element, next_el):
            self._element = element
            self._next = next_el

        @property
        def element(self):
            return self._element

        @property
        def next_el(self):
            return self._next

    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def top(self):
        if self._head is None:
            raise Empty('Stack is empty.')
        return self._head.element

    def push(self, el):
        self._head = self._Node(el, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        answer = self._head.element
        self._head = self._head.next_el
        self._size -= 1
        return answer
