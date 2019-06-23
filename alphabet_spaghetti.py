"""
What letter of the alphabet is the one which comes eight letters before the letter which comes five letters after the fourth appearance of the first letter to occur four times in this sentence?

Odpowiedz to "r"!! :D:D:D
"""

sentence = "What letter of the alphabet is the one which comes eight letters before the letter which comes five letters after the fourth appearance of the first letter to occur four times in this sentence?"

def alphabet_spaghetti(
    sentence,
    letters_before,
    letters_after,
    nth_appearance,
    letter_appears_this_many_times):

    letters = {}

    # 8 letters before
    # 5 letters after
    # 4th appearance
    # of letter that appears 4 times ("t" in this case)

    """
    Firstly strip all whitespace.
    """
    sentence = sentence.replace(" ", "").lower()
    letter_we_are_trying_to_find = ""
    letter_that_appears = ""
    letter_that_appears_alphabetised = ""

    for index in range( len(sentence) ):
        letter = sentence[index]

        if letter in letters:
            letters[letter]['appearances']['total'] += 1
            letters[letter]['appearances']['instances'].append(index)
            
        else:
            letters[letter] = {'appearances': {'total': 1, 'instances': [ index ]}}
        
        # letters[letter]['appearances'] = {
        #     letters[letter]['total']: index
        # }
        
        if index >= 3 and letter_that_appears == "":
            for key, value in letters.items():
                # print(value)
                if value['appearances']['total'] == letter_appears_this_many_times:
                    letter_that_appears = letters[key]
                    letter_that_appears_alphabetised = key
                    break
        
        if letter_that_appears != "":
            break

    letter_instances = letter_that_appears['appearances']['instances']
    index = 0

    # print(letters)

    if nth_appearance <= len(letter_instances):
        letter_index_to_start_from = letter_instances[nth_appearance - 1]
        index = letter_index_to_start_from

        print("index at 1st if: " + str(index))
    else:
        print("nth_appearance doesn't exist as an index in letter_instances array.")

    if (index + letters_after) < len(sentence):
        index += letters_after
        print("index at 2nd if: " + str(index))
    else:
        print("letters_after conditional skipped due to index sum being more than maximum array offset.")
    
    if (index - letters_before) >= 0:
        index -= letters_before
        print("index at 3rd if: " + str(index))
    else:
        print("letters_before conditional skipped due to index sum being less than minimum array offset.")
        
    letter_we_are_trying_to_find = sentence[index]

    print("")
    print("The letter that comes " + str(letters_before) + " letters before the letter that comes " + str(letters_after))
    print("letters after appearance number " + str(nth_appearance) + " of the first letter to occur " + str(letter_appears_this_many_times))
    print("times in the sentence above ("+ letter_that_appears_alphabetised +") is: the letter '" + letter_we_are_trying_to_find + "'")





alphabet_spaghetti(sentence, 8, 5, 4, 4)