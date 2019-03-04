# -*- coding: utf-8 -*-
# !/usr/bin/python


class Empty(Exception):
    pass


class LinkedQueue(object):

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
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head.element

    def last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._tail.element

    def enqueue(self, el):
        newest = self._Node(el, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head
        self._head = answer.next_el
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer.element
