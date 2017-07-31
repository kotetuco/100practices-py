# -*- coding: utf-8 -*-

"""
No.05
(http://www.cl.ecei.tohoku.ac.jp/nlp100/)
This code is executed in python3.6.1
"""

def n_gram(input, n):
    slice_list = []
    for i in range(len(input)):
        if i > (len(input) - n):
            break
        slice_list += [input[i:(i+n)]]
    return slice_list

def character_bigram(input_string):
    input_list = character_only_list(input_string)
    bigram = n_gram(input_list, 2)
    bigram_words = []
    #print(bigram)
    for word in bigram:
        bigram_words += [''.join(word)]
    return bigram

def word_bigram(input_string):
    input_list = word_only_list(input_string)
    bigram = n_gram(input_list, 2)
    bigram_words = []
    #print(bigram)
    for word in bigram:
        bigram_words += ['-'.join(word)]
    return bigram_words

def word_only_list(input):
    return input.replace('.', '').replace(',', '').split(' ')

def character_only_list(input):
    return input.replace('.', '').replace(',', '').replace(' ', '')

if __name__ == '__main__':
    input = u'I am an NLPer'
    print('Input:' + input)
    print('bi-gram for the character:' + str(character_bigram(input)))
    print('bi-gram for the word:' + str(word_bigram(input)))
