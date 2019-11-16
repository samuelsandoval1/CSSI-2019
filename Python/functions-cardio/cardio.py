# Example 1

def longest_word(string1, string2, string3):
    thelongest_word = ''
    if len(string1) > len(string2) and len(string1) > len(string3):
        print(string1)
    elif len(string2) > len(string3) and len(string2) > len(string1):
        print(string2)
    else:
        print(string3)

longest_word("cat" , "horse" , "elephant")
