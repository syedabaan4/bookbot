from stats import count_words, get_book_text

def main():
    path = "./books/frankenstein.txt"
    # print(count_words(get_book_text(path)))
    num = count_words(get_book_text(path))
    print(f"Found {num} total words")

main()
