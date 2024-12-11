arr = [1, 2, 5, 7, 8, 9, 11, 22, 55]

f = 22

def bin_search(t, array):
    div = 2
    ind = len(array) // div
    div = div * 2
    for i in range(len(array)):
        if t > array[ind]:
            ind = ind + len(array) // div
            div = div * 2
        if t < array[ind]:
            ind = ind - len(array) // div
            div = div * 2
        if t == array[ind]:
            print(ind)
            break

bin_search(f, arr)
