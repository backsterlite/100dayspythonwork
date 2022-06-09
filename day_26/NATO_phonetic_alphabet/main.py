import pandas as pd
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet = {row.letter:row.code for title, row in df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
result = [phonetic_alphabet[letter.upper()] for letter in list(word)]
print(result)
