def main(): # Main program loop
    book_location = "books/frankenstein.txt" # path variable defines the location of the book text in the git repo
    word_total = word_count(get_text(book_location))
    char_total = char_count(get_text(book_location))
    #print(f"The total number of words in this book is: {word_total}")
    #print(f"Here is a break down of the character usage in the text: {char_total}")

    generate_report(book_location, word_total, char_total)


def word_count(text): # Calculates the length of the provided text, returns length.
    words = text.split()
    return len(words)

def get_text(path): # Uses provided path variable to open target .txt file and returns it's contents as a string
    with open(path) as f:
        return f.read()
    
def char_count(text): # Returns a dictionary of each time a character is used in the provided string. Output is always lowercase
    raw_text = text.split()
    char_counter = {}
    for word in raw_text:
        for letter in word:
            if letter.lower() in char_counter and letter.isalpha():
                char_counter[letter.lower()] += 1
            elif letter.lower() not in char_counter and letter.isalpha():
                char_counter[letter.lower()] = 1
    return char_counter

def dict_sort(dict):
    return dict["count"]

def generate_report(book_loc, words, chars): # Prints a report giving total words + total character counts.
    char_list = []
    for char in chars:
        char_list.append({"letter": char, "count": chars[char] })

    char_list.sort(reverse=True, key=dict_sort)
 


    print(f"@_______@ Python Report on {book_loc} @_______@")
    print("")
    print(f"The book @ {book_loc} contains a total of {words}.")
    print("\n")
    for i in range(len(char_list)):
        print(f"The {char_list[i]["letter"]} character was found {char_list[i]["count"]}")

    print("")
    print("Thank you for using this program for your report")
    print("")
    print("@_______@ Finish @_______@")


main()