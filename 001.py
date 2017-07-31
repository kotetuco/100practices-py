# -*- coding: utf-8 -*-

"""
No.01
(http://www.cl.ecei.tohoku.ac.jp/nlp100/)
This code is executed in python3.6.1
"""

def pull_odd(input):
    """
    reference to : http://dev.chrisryu.com/2008/07/python_array_slice.html
    """

    output = input[0::2]
    return output

if __name__ == '__main__':
    input = u'パタトクカシーー'
    print(pull_odd(input))
