from stats import *

def main():
    path = "./books/frankenstein.txt"
    num = count_words(get_book_text(path))
    print("============ BOOKBOT =============")
    print(f"analyzing book found at {path}")
    print("--------- Word Count ----------")
    print(f"Found {num} total words")
    print("------- Character Count -------")

    char_count = count_characters(get_book_text(path))    
    # print(char_count)
    final_list =  sort_dict(char_count)
    for item in final_list:
        char = item["char"]
        number = item["num"]
        print(f"{char}: {number}")

    print("============ END =============")

main()
