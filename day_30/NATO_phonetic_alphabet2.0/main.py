import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet = {row.letter:row.code for title, row in df.iterrows()}


def gen_phonetic():
    word = input("Enter a word: ")
    try:
        result = [phonetic_alphabet[letter.upper()] for letter in word]
    except KeyError:
        print("You must enter characters from alphabet only")
        gen_phonetic()
    else:
        print(result)

gen_phonetic()
