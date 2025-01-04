def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("report of books/frankenstein.txt")
        print(f"{word_count(file_contents)} found in the document")
        for i in char_count(file_contents):
            print(f"The {i} character was found {char_count(file_contents)[i]} times")

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    characters = {}
    for i in range(0, len(text)):
        if text[i] in characters:
            characters[text[i]] += 1
        else:
            characters[text[i]] = 1
    return characters
main()