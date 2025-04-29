def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    char_count = {}

    text = text.lower()

    for char in text:
        if char in char_count:
            char_count[char] = char_count[char] +1
        else:
            char_count[char] = 1
    return char_count

def sorted_list(char_count):
    chars_list = []
    for char, count in char_count.items():
        chars_list.append({"char": char, "num": count})
    chars_list.sort (reverse=True, key=lambda x: x["num"])

    return chars_list





