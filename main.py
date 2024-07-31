def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(character_count(text))


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def character_count(text):
    lowered_text = text.lower()
    text_dict = {}

    for t in lowered_text:
        if t in text_dict:
            text_dict[t] += 1
        else:
            text_dict[t] = 1
    text_list = [{"char": k, "num": v} for k, v in text_dict.items()]

    def sort_on(dict):
        return dict["num"]

    text_list.sort(reverse=True, key=sort_on)

    print("--- Begin report ---")
    total_words = get_num_words(text)
    print(f"{total_words} words found in the document")
    print("")

    for item in text_list:
        if item["char"].isalpha():
            print(f"The {item['char']} character was found {item['num']} times")
    print("--- End report ---")


main()
