# -*- coding: utf-8 -*-

#
# No.02
# (http://www.cl.ecei.tohoku.ac.jp/nlp100/)
# This code is executed in python2.7.x
#

# 
def join_alternately(input1, input2):
    """
    output: [input1[0], input2[0], input1[1], input2[2], ...]
    reference to : http://python.civic-apps.com/zip-enumerate/
    """
    
    input1_list = list(input1)
    input2_list = list(input2)
    output = []
    for (even, odd) in zip(input1_list, input2_list):
        output += [even, odd]
    return ''.join(output)

if __name__ == '__main__':
    input1 = u'パトカー'
    input2 = u'タクシー'
    print join_alternately(input1, input2)
