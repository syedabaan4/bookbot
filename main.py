def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    word_list = text.split()
    count = len(word_list) 
    return count
    
def main():
    path = "./books/frankenstein.txt"
    # print(count_words(get_book_text(path)))
    num = count_words(get_book_text(path))
    print(f"Found {num} total words")

main()
