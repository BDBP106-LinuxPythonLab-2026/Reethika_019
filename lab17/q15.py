# (15) Words starting with character k
def words_starting_with(L, k):
    return [w for w in L if w.startswith(k)]
if __name__ == "__main__":
    print("1:",binary_to_decimal("101101"))
    print("2:", power(2, 5))
    print("3:", is_prime(29), is_prime(30))
    print("4:"); print_digits(4096)
    print("5:",first_half("bioinformatics"))
    print("6:",alternate_chars("bioinformatics"))
    print("7:", repr(trim_leading("helloworld")))
    print("8:", count_word("is", "this is it and it is fine"))
    print("9:", is_anagram("listen","silent"), is_anagram("gram", "arm"))
    print("10:", evens([1, 2, 3, 4, 5, 6,10]))
    print("11:", duplicates([1, 2, 3, 2, 4,1, 5, 1]))
    print("12:", subtract_matrices([[5, 6],[7, 8]], [[1, 2], [3, 4]]))
    print("13:", more_than_k([1, 2, 2, 3,3, 3, 4], 1))
    print("14:", remove_all([1, 2, 3, 2, 4,2], 2))
    print("15:",words_starting_with(["kite", "apple","king", "bat"], "k"))