def duplicates(L):
    seen, dup = set(), []
    for x in L:
        if x in seen and x not in dup:
            dup.append(x)
        seen.add(x)
    return dup