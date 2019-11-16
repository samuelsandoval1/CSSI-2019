
def first_vowel(word):
    """
    Find the index of the first vowel
    """
    vowels = ['a' , 'e' , 'i' , 'o' , 'u']
    for i in range(len(word)):
        if word[i].lower() in vowels:
            return i
print first_vowel("Hello")
print first_vowel("qqqqq")
print first_vowel("HELLO")
print first_vowel("word word")
print first_vowel("345")
print first_vowel("aaaaa")



def get_words():
    """
    Return list of words from the user.
    """
    #TODO: RETURN SOMETHING
    words = raw_input("Enter a word or phrase: ")
    word_list = words.split(" ")
    return word_list

words = get_words()
print words

def rotate(word):
    """
        Return a version that is in pig latin.
    """
    new_word = ""
    letters = list(word)
    for letter in word:
        letter += letter
    if (first_vowel(word) !=0):
        letters.append(letters[0].lower())
        letters.remove(letters[0])
        letters.extend(['a' , 'y'])
    else:
        letters.extend(['y' , 'a' , 'y'])
    for i in range(0, len(letters)):
            new_word += letters[i]
    return new_word

print rotate("qqqqq")
print rotate("OWL")
print rotate("Hello")
print rotate("345")
print rotate("HOWDY")
print rotate("A")
print rotate("B")
#


def combine_words(word_list):
    """
    Combine a list of words into a phase that
    """
    phrase = ""
    for i in word_list:
        phrase = phrase + i + ""
    return phrase

print combine_words(['test' , 'word' , 'list'])
print combine_words([])
print combine_words(['test' , 'word' , 'list'])
print combine_words(['3' , '4' , '5'])



words =get_words()
pig_phrase = []
for word in words:
    pig_word = rotate(word)
    pig_phrase.append(pig_word)
print combine_words(pig_phrase)
