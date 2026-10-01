# (13) Elements occurring more than k times
def more_than_k(L, k):
    result = []
    for x in L:
        if L.count(x) > k and x not in result:
            result.append(x)
            return result