def insert_sort(S):

    for i in range(1, len(S)):
        curr = S[i]
        k = i
        while k > 0 and S[k - 1] > curr:
            S[k] = S[k - 1]
            k -= 1
        S[k] = curr


if __name__ == "__main__":

    li = [1, 4, 9, 2, 7, 0]
    insert_sort(li)
    print(li)
    assert li == [0, 1, 2, 4, 7, 9] # True