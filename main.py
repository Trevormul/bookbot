def wordcount(text):
    words = text.split()
    return len(words)

def charcount(text):
    charcount = {}
    for i in text:
        lower_string = i.lower()
        if lower_string not in charcount:
            charcount[lower_string] = 1
        else:
            charcount[lower_string] += 1
    return charcount

def sort_on(dict):

    return dict["num"]

def main():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
        char_counts = charcount(file_contents)
        chars_list =[]
        for char, count in char_counts.items():
            if char.isalpha():
                char_dict = {"char": char, "num": count}
                chars_list.append(char_dict)
        chars_list.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{wordcount(file_contents)} words found in the document\n")
        for char_dict in chars_list:
            print (f"The '{char_dict['char']}' character was found {char_dict['num']} times")
            print("--- End report ---")

if __name__ == "__main__":
    main()