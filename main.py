import pandas

# Get the data
file_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Create a dictionary of letter-code
letter_code_dict = {row.letter: row.code for (index, row) in file_data.iterrows()}


def generate_word_code():
    # Ask the user an input
    word = input("Enter a word: ").upper()
    try:
        # Search each letter of the word in the dictionary and get the code
        word_code_list = [letter_code_dict[letter] for letter in word]
    except KeyError:
        print("Please, only enter alphabet letters")
        generate_word_code()
    else:
        print(word_code_list)


generate_word_code()
