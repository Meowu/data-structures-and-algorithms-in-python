from Priority_Queue.HeapPriorityQueue import HeapPriorityQueue
from Linked_List.PositionalList import PositionalList


def pq_sort(C: PositionalList) -> PositionalList:
    n = len(C)
    pq = HeapPriorityQueue()
    for i in range(n):
        element = C.delete(C.first())
        pq.add(element, element)
    for i in range(n):
        k, v = pq.remove_min()
        C.add_last(v)
    return C


if __name__ == '__main__':
    el = [23, 10, 39, 4, 9, 3]
    P = PositionalList()
    for i in el:
        P.add_last(i)
    assert len(P) == len(el), 'add all el to PositionList'
    P = pq_sort(P)
    assert len(P) == len(el), 'sorted succeed.'
    assert P.first().element == min(el), 'sorted List with min value as first element.'
    assert P.last().element == max(el), 'sorted list with max value as last element.'
