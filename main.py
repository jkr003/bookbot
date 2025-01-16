def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_count = character_count(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    report = sort_dict(char_count)
    for c, count in report:
        if c.isalpha():
            print(f"The '{c}' character was found {count} times")
            
    print("--- End report ---")

def sort_dict(dict):
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)

def character_count(text):
    character_count = {}
    lowered_text = text.lower()
    for character in lowered_text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()