# (1) Binary to decimal
def binary_to_decimal(B):
    dec = 0
    for bit in str(B):
        dec = dec * 2 + int(bit)
    return dec
print("1:", binary_to_decimal("10110"))