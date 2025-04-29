import sys 
from stats import count_words, count_char, sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_count = count_char(book_text)
    sorted_chars = sorted_list(char_count)  # Use the correct function name

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Loop through the sorted characters and print only alphabetical ones
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
