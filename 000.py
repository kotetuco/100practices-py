# -*- coding: utf-8 -*-

#
# No.00
# (http://www.cl.ecei.tohoku.ac.jp/nlp100/)
# This code is executed in python2.7.x
#

def reverse(input):
    # "s[i:j:k]" is "slice of s from i to j with step k"
    # reference to : http://d.hatena.ne.jp/redcat_prog/20111104/1320395840
    output = input[::-1]
    return output

if __name__ == '__main__':
    input = "stressed"
    print reverse(input)
