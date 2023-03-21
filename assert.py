# Assert for testing and debugging. 
# Assert statements are used to check if the code is working as expected.
# assert <boolean expression>, <error message>

# Example 1
def first_letter(word_list):
    first_letters = []

    for word in word_list:
        assert type(word) == str, f'{word} is not a string'
        assert len(word) > 0, 'Empty string not allowed'

        first_letters.append(word[0])

    return first_letters


