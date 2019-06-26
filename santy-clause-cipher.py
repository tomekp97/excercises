"""
https://www.mathsisfun.com/puzzles/christmas-pudding.html

Father Christmas spends 364 days of the year as a taster of Christmas puddings (which is why he is so round and jolly). Recently he came across a Magic Pudding.

If you eat some of this pudding, the next thing you say comes out in a magic code.

Father Christmas tried it, liked it, and said:

"IP! IP! IP! XIBU B MPWFMZ QVEEJOH! NFSSZ DISJTUNBT BOE B IBQQZ OFX ZFBS UP ZPV BMM!"
"""

import string

sentence = "IP! IP! IP! XIBU B MPWFMZ QVEEJOH! NFSSZ DISJTUNBT BOE B IBQQZ OFX ZFBS UP ZPV BMM!"

def decrypt(sentence, offset):
    alphabet_string = string.ascii_uppercase
    alphabet = list(alphabet_string)
    decrypted_sentence = ""

    iteration = 0
    for char in sentence[iteration:]:
        if char in alphabet:
            original_index = alphabet.index(char)
            updated_index = original_index + offset
            char = alphabet[updated_index]
        
        decrypted_sentence += str(char)
        iteration += 1

    print(decrypted_sentence)

decrypt(sentence, -1)