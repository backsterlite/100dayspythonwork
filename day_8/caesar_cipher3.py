alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def fix_position(position, shift):
    if shift == 'shift' and position > len(alphabet):
        position = position - len(alphabet)
    elif shift == 'unshift' and position < 0:
        position = len(alphabet) + position
    return position
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def ceasar(text, shift, direction):
    output_text = ""
    for letter in text:
        if direction == 'encode':
            position = fix_position(alphabet.index(letter) + shift, 'shift')
        else:
            position = fix_position(alphabet.index(letter) - shift, 'unshift')
        output_text += alphabet[position]
    print(f"The {direction}d text is {output_text}")



#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
ceasar(text, shift, direction)