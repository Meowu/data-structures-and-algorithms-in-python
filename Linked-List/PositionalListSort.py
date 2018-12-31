# -*- coding: UTF-8 -*-
# !/usr/bin/env python3


def insert_sort(p_list):

    if len(p_list) > 1:
        marker = p_list.first()
        while marker != p_list.last():
            pivot = p_list.after(marker)
            value = pivot.element
            if value > marker.element:
                marker = pivot
            else:
                walk = marker
                while walk != p_list.first() and walk.element > value:
                    walk = p_list.before(marker)
                p_list.delete(pivot)
                p_list.add_after(walk, value)
