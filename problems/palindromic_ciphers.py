def convert_char_to_julius_cipher_value(char):
    ascii_value = ord(char)
    cipher_value = ascii_value - 96
    return cipher_value


def check_if_string_is_palindrome(word_string):
    return word_string == word_string[::-1]


def print_cipher_product_or_palindrome(word_string):
    if check_if_string_is_palindrome(word_string):
        print("palindrome")
    else:
        product = 1
        for c in word_string:
            product *= convert_char_to_julius_cipher_value(c)
        print(product)


if __name__ == "__main__":
    no_of_inputs = int(input())
    inputs = [input() for _ in range(no_of_inputs)]
    [print_cipher_product_or_palindrome(i) for i in inputs]