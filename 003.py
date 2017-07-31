# -*- coding: utf-8 -*-

"""
No.03
(http://www.cl.ecei.tohoku.ac.jp/nlp100/)
This code is executed in python3.6.1
"""

def words_count(input):
    """
    reference to : http://python.civic-apps.com/map-reduce-filter/
    """
    
    return list(map(lambda n:len(n), input))

def words(input):
    """
    reference to : http://python.civic-apps.com/string-split-join/
    """
    
    return input.replace('.', '').replace(',', '').split(' ')

if __name__ == '__main__':
    input = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    print(words_count(words(input)))
