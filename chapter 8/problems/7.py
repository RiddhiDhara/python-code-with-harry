words = ["  apple  ", "  orange", "grape ", "banana "]

word = "apple"


def striper(words, word):
    return [item.strip() for item in words if word != item.strip()]


print(striper(words,"apple"))
