def interchange(L):
    L = L[:]
    for i in range(0, len(L) - 1, 2):
        L[i], L[i + 1] = L[i + 1], L[i]
    return L

sample_list = [23, 32, 33, 44, 'BDBH101', 'hello', 'python', 15, 1e-10, True, 'hit']
print("Interchange List Elements")
print("Original list:", sample_list)
print("Interchanged list:", interchange(sample_list))