import sys
from stats import get_num_words, get_num_char, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1] 
    num_words = get_num_words(get_book_text(filepath))
    num_char = get_num_char(get_book_text(filepath))
    my_list = sort_dict(num_char)
    count = 0
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for x in my_list:
        print(f"{my_list[count]['char']}: {my_list[count]['num']}")
        count += 1
    print("============= END ===============")

main()
