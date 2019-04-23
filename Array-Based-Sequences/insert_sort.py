def insert_sort(S):

    for i in range(1, len(S)):  # 从第二个开始，总是把当前的元素跟它前面的进行比较。
        curr = S[i]
        k = i
        while k > 0 and S[k - 1] > curr:  # 此时当前元素前面的所有元素都是已经排序好的。不断往回比较，只要发现它比前面的元素小就交换位置。
            S[k] = S[k - 1]
            k -= 1
        S[k] = curr


if __name__ == "__main__":

    li = [1, 4, 9, 2, 7, 0]
    insert_sort(li)
    print(li)
    assert li == [0, 1, 2, 4, 7, 9]  # True
