# (7) Trim leading whitespace
def trim_leading(S):
    i = 0
    while i < len(S) and S[i].isspace():
        i += 1
        return S[i:]
# same as
    S.lstrip()