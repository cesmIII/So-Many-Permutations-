def perms(arr: str) -> list:
    arr_lst = list(arr)
    results = []

    def perm(sz: int):
        if sz == 1:
            # Base case: store a copy of the current permutation
            results.append(list(arr_lst))
            return

        for i in range(sz):
            # If we are on the last iteration, skip swapping
            perm(sz - 1)

            if i < sz - 1:
                if sz % 2 == 0:
                    # Even sz: swap the current index i with the last element
                    arr_lst[i], arr_lst[sz - 1] = arr_lst[sz - 1], arr_lst[i]
                else:
                    # Odd sz: swap 0-th element with last element
                    arr_lst[0], arr_lst[sz - 1] = arr_lst[sz - 1], arr_lst[0]

    (perm(len(arr)))
    return list(set(["".join(array) for array in results]))


string = 'aabc'
print(str(perms(string)))
