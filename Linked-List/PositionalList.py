# -*- coding: UTF-8 -*-
# !/usr/bin/python3

from .DoublyLinkedList import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):

    class Position(object):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.element

        @property
        def node(self):
            return self._node

        @node.setter
        def node(self, node):
            self._node = node

        @property
        def container(self):
            return self._container

        @container.setter
        def container(self, c):
            self._container = c

        def __eq__(self, other):
            return type(other) is type(self) and other.node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, pos):
        if not isinstance(pos, self.Position):
            raise TypeError('pos is not valid Position type')
        if pos.container is not self:
            raise ValueError('pos does not belongs to this container.')
        if pos.node.element is None:
            raise ValueError('node pos is no longer valid.')
        return pos.node

    def _make_position(self, node):
        if node is self._header or node is self._tail:
            return None
        return self.Position(self, node)

    def first(self):
        return self._make_position(self._header.next_node)

    def last(self):
        return self._make_position(self._tail.prev_node)

    def before(self, pos):
        node = self._validate(pos)
        return self._make_position(node.prev_node)

    def after(self, pos):
        node = self._validate(pos)
        return self._make_position(node.next_node)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.node.element
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header.next_node)

    def add_last(self, e):
        return self._insert_between(e, self._tail.prev_node, self._tail)

    def add_before(self, pos, e):
        node = self._validate(pos)
        return self._insert_between(e, node.prev_node, node)

    def add_after(self, pos, e):
        node = self._validate(pos)
        return self._insert_between(e, node, node.next_node)

    def delete(self, pos):
        original = self._validate(pos)
        return self._delete_node(original)

    def replace(self, pos, e):
        original = self._validate(pos)
        old_element = original.element
        original.element = e
        return old_element
