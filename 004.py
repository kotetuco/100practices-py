# -*- coding: utf-8 -*-

"""
No.04
(http://www.cl.ecei.tohoku.ac.jp/nlp100/)
This code is executed in python2.7.x
"""

def extract_characters(input):
    one_character_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    output = {}
    
    for index, value in enumerate(input):
        if (index + 1) in one_character_list:
            output[index + 1] = value[0:1]
        else:
            output[index + 1] = value[0:2]
        
    return output

def words(input):    
    return input.replace('.', '').replace(',', '').split(' ')

if __name__ == '__main__':
    input = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    print extract_characters(words(input))
