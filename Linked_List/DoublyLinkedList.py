# -*- coding: utf-8 -*-
# !/usr/bin/python3

# Getters and setters are used in many object oriented programming languages
# to ensure the principle of data encapsulation.


class Empty(Exception):
    pass


class _DoublyLinkedBase(object):

    class _Node(object):

        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next_el):
            self._element = element
            self._next = next_el
            self._prev = prev

        @property
        def prev_node(self):
            return self._prev

        @property
        def next_node(self):
            return self._next

        @property
        def element(self):
            return self._element

        @element.setter
        def element(self, el):
            self._element = el

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._header._next = self._tail
        self._tail._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node.prev_node
        successor = node.next_node
        predecessor._next = successor
        successor._prev = predecessor
        element = node.element
        node._next = node._prev = node.element = None
        self._size -= 1
        return element


class LinkedDeque(_DoublyLinkedBase):

    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header.next_node.element

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty.')
        return self._tail.prev_node.element

    def insert_first(self, el):
        self._insert_between(el, self._header, self._header.next_node)

    def insert_last(self, el):
        self._insert_between(el, self._tail.next_node, self._tail)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty.')
        self._delete_node(self._header.next_node)

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        self._delete_node(self._tail.prev_node)
