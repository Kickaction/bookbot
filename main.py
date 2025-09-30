from stats import get_num_words, characters, build_sorted_char_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")


    char_counts = characters(text)
    sorted_chars = build_sorted_char_list(char_counts)

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
if __name__ == "__main__":
    main()    