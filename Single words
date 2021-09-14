# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
# Example:
#   Input:
#       'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
#   Output:
#       'alpha beta gamma delta'
# This algoritm must run in time n

words = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'


def single_words(words_string):
    unique_words = ''
    words_list = words_string.split()
    for word in words_list:
        if word not in unique_words:
            unique_words += word + ' '
    return unique_words


print(single_words(words))
