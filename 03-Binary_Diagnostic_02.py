import numpy as np
import pandas as pd

# input="""00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010"""
input="""001000010101
010010111110
001010110111
001001011101
001001010011
001111100111
100000000101
010001011011
000101011010
101100010011
111011101101
101100100110
000101111011
101111000011
001100000101
010011111000
011001001111
101100100011
000110010011
011010111101
010011101010
111101111000
110111011110
101111100010
101000100011
011000011001
111101011101
010001101111
000010010010
101100010110
001001010010
010000000011
110000000000
101111101000
001111010110
010011101011
100001011111
111001110100
101000010000
110101001011
010000110101
001110000110
011000000010
101110010001
101010000010
011101100110
011111011100
000000111001
010110001010
010001111010
110111100110
101011000100
101100010101
000011111101
101011111001
011000001001
000001001001
100100101010
101110001011
111101110000
111101101100
010110100110
011110001110
001110011100
100101010010
100000001111
000010111111
101000011100
010100001000
010001010010
101100111111
010101010101
010011000111
111010010101
111010111111
100001011110
100111110111
010010111001
110100100110
111011110110
111110011111
011011111101
100011011100
000100101110
000110111110
111110010111
101100110110
010011010111
101101001110
010100010010
111101010111
111000100001
100011010000
111001110110
100100010100
011010001101
000110010111
001010101001
011000010011
010100011100
110001111101
111001110000
111100110101
111000101111
000010011111
011100110110
010111101000
011001110011
100101110101
011001010110
010101100110
000111001000
101110001111
110100000110
000111011111
010101111101
111010111011
100001101111
101110000110
111111111010
110111000010
100010101111
100111010010
010000001110
100110000011
110101011100
010100100100
001100011100
001100010000
100000101010
101111010100
001100001000
111100110100
011101111010
001011000010
110000010101
001011001111
000111011100
101101101110
110001011111
111111011101
100001001000
010001110110
000011101010
100011101000
000110111100
011100111100
101100101000
111110001100
100010010100
011011000011
010001101101
001110011010
011111101111
000010001110
010100101111
010010011010
000010010000
101000001000
011010010111
110111111110
111101001000
101100110111
001101000000
011010011001
111000100000
000000010101
110000011011
111100101000
000111010110
110000000010
111000100011
110110001100
011110000000
111011011111
101001000001
000010010110
011010101101
110001100111
100101110011
000110001011
000110011111
001100100010
001011000111
001000010110
001010011000
011001101110
001010000100
011010100111
111010100110
010100000010
010011100100
011101010110
100101000000
111100010110
001101101011
001100000111
001011010001
011101110010
000011111000
000000000111
111111110011
000101111000
110001010111
010001010001
001011000000
101110111011
101111100001
010110000010
011011101000
001100110101
101111101011
100001010111
010110110110
011101000101
110001110111
010101001101
100111010011
010011110110
010101110001
011011110011
110011101001
010001111011
110110000000
100001000110
011000101111
001100110000
001110010100
111011100100
000011100010
101010001101
101011111111
100001111110
011011100011
010011111011
000101001000
111101010110
111101000111
111111100001
100100100000
010000111110
110110000101
001110011011
010100101101
010100101110
100011010100
001001110101
011011111000
111111001101
011001110101
011001111111
010000010100
010110001001
100101000010
111101111001
010111111010
110011111000
000100111000
110101100101
010100001101
000111011110
011110000111
011000001101
110011000010
010010100001
000001101100
010000011100
100010001111
111010010100
001101111000
100111001111
111011101100
010011111110
111010001111
100111110110
100101110000
001001100110
001010011001
010100110000
100011101101
100000001101
110010000111
101001011001
101010010111
101011101110
011111101011
110100110110
000101010000
011101100011
100011100101
000001000111
011011110010
010001001010
001001101100
100101011100
111110100100
101101111000
101000101110
110101011000
101001111100
011001111000
110110101100
100010000010
100110100000
011010010110
100011100000
111100000000
001111111110
010000010010
100110000100
100000011010
010010011111
011001110001
001110100010
101011100000
011011011101
011100010011
011000111011
111010010111
000011011101
000100000001
110000001011
111000011111
111110111111
011111110111
000011000010
100111011101
010001010100
111100100101
111110100010
010101110100
001111111100
011000100010
011010111011
100010111110
011100000010
011111111110
110001001111
011001000111
101000000110
010010001100
001100010111
111110101010
110011011100
110011011010
110010011101
101001111111
111001111001
101101100101
100100111010
010110101100
100100100100
110110110001
000010001101
101001001100
010101010001
111001001000
001000110110
101100000101
010010100111
101001010010
011000001110
101101101000
110011110000
111110011100
010000011111
001001111111
001110110111
100110100110
011101100010
101101010011
001010101110
101001100111
110110101101
101100000000
100110101001
100110101010
100010110101
101101010100
001110111111
101110101110
111011001110
011000110110
000011111010
011111100100
111001100110
010110010101
001101011001
011010010101
110100101001
010100100111
111001100111
111110101011
000100110101
010000100011
000011100110
010111101111
010111001111
001011110000
110110010111
010000100000
011011010000
011101100100
111110010110
000110100000
111010101011
100000110001
001001111001
000001010111
011011100111
010100010100
011101101101
000000101110
100110111011
001110011001
000111001101
011010011111
100011111010
010110110111
000101111111
100000001110
010100000001
010111100010
100000110101
000110100100
100111100111
101011010111
100100110110
111111000010
101110101011
111100000110
010111110001
100111000100
111001011101
000011010011
101111010110
011000101100
111000000011
111101101001
101010111000
010010110001
010110101001
100110001000
011100111001
010111011100
001101110100
010100100010
111111111100
010011000110
000110100111
011011011011
111111011000
000100010001
011100001011
100110010110
010011110000
010001111110
000000011100
111000001110
000111000101
011100011011
000111101101
010101111010
100001111111
011101101100
000100000100
100010000110
101111110100
011100010000
110011100110
011011000111
111111000101
101010001001
010000111100
111001101001
000011100011
101000011101
000000101000
111011110010
001010111100
101000100001
011000001100
001011111101
101110100101
010001110001
000110101100
001000010011
011001011110
011011101001
000010111101
011001111010
101011000000
100101011011
100100010101
011010000010
111100110000
010101000001
101111100000
100110100100
010000101111
010001100100
000100011010
110001011100
100111100011
101101101100
101111011001
010100010011
001010001010
011100011111
110010111000
011100111000
100101000101
110111110000
110111010110
111000111100
110000011110
110111100011
010000010000
101110111100
100111001001
010011011111
100010110010
001011010110
110011000100
111011001000
101011100010
001110001001
010111001000
110100110101
101110101111
111001111011
010000011000
110100000100
100100110000
010000100110
100011001101
011001100110
010110000001
111110001111
000011111111
110000000110
000111010111
010011111100
001001000101
100101100110
000101000010
101011100001
100111010110
111100101001
000011110001
101001100101
110010000011
001110100001
110101101100
111100110010
100111100100
011110011100
011000011111
000100100100
011011100001
100001011001
010111111000
001000011110
111010010001
111111001100
011000110101
001010100110
110010000001
011111000101
001110000011
110001110110
000000011010
000010000000
001101011101
110110011101
000011011100
110011000011
100111010111
100111000111
110010110001
100011110101
101010101000
111000001101
111010100100
110001000000
011111001101
001110010011
110111011101
110111101000
100000111111
101110111000
000111111101
101001111101
100000110011
011100011110
111100110110
111100001101
101011011101
001000101010
011100100101
100001001001
100110011101
110111110111
101101100000
001010100000
010000111001
000100110111
000101100000
110000010001
101111111000
110001011110
001110010111
110100100011
111111101101
000001100101
100100110001
011100001001
111011000111
100001001100
000001111000
011011111011
001111100110
001111111000
000111110000
001001000010
110101000001
001001110011
110110010010
010001000001
001100011110
001011100001
000011110100
100000100011
110011100011
110111100000
010011110100
110000001100
011111111001
110001001110
110011001001
001010101000
000111110100
100001000101
111000110111
010010001011
000111011101
010110001110
011010001010
010000001011
011111110100
111000010100
001000011000
101001111010
110000001111
010100101010
000100011001
100011110111
001111101011
000010101010
010111110000
111111000000
001100000110
111000111010
010100100110
001000010001
000001111110
000010111010
110010011100
001110000100
010000110000
011101111100
011110101001
111100010100
101011111100
001001001101
000111110101
010101110000
010100001011
010100011101
011100111101
010010000011
010010111100
100001100011
010111010000
010100110001
100100010111
010100011000
111011111000
110011010010
100010100001
111110111100
000110101001
110100001010
001101100000
111110001110
011010100101
001110111100
101001100100
000110110110
000111011000
000000010111
110101011010
110100010011
101011010100
101100010100
110001110011
111100100010
011000001111
010000111011
011010100000
010000000111
000000001111
000101000000
110011100111
000011111100
011010001100
000111000100
101110011100
011011011111
110000100000
101001000111
101111111010
111011011001
111100010011
100011000001
011101100000
111101001001
101110101010
001100101111
001101001001
010101001110
101100110010
000101111001
101010101101
111001010000
001011111000
000111110001
100010001010
000101100100
010100111100
101110001101
100010010011
000011010010
100011110011
110001101000
011101011001
100101010101
010111011001
110001010001
011111011001
010111000000
011010110010
110110100110
001011011001
100101111001
000100100011
000111001001
000010000001
100111000101
010110111110
111010101100
110010100011
101010001000
111110100001
100000101111
110001111110
010001101110
010001001111
101111000001
101101010010
001101001111
100111011001
010111101101
111111001111
110110111000
011000000011
000100111101
001000000100
101000100010
011101001100
100001001011
100011100011
001110110000
110100001111
111001111100
001010001011
100000000111
101101110011
010110011101
111101011110
100100100111
011001001101
010110110100
000000111110
001101110000
101110000100
100010111000
110101010011
101101001001
100010000011
011000000100
001101010110
010100011001
100011101001
011001010010
010001100111
111100011110
010101110111
101100110101
100101011111
100101101100
101000001110
011110110011
011011001100
101000111101
001011110111
100000010101
111001111101
111011010001
111101001111
010010011110
000110010001
111000000110
110010101010
001110110001
100111011000
111101001010
011100101110
001100100000
100110010101
011110111111
111110110101
000000111100
101010011001
100011110001
001011011100
101111100110
001010100010
001111000110
100100101110
101011001100
010111100110
110100100100
100111001000
010001011110
110100111101
101011110000
110011111001
000001100010
011010101001
010001111001
001110100000
101111011011
010010100100
100000001010
010110011111
010010100101
100000010001
111110111000
000101110100
010100000101
101101010001
001000111110
011111101101
110011010101
110101111110
011110101110
110111101011
111111111000
011100001000
011000000101
011011110111
011000001010
001011010011
101001010110
111000110011
111110011011
110111011000
101101011110
000110010000
111101101101
001100011101
110110010101
100011011010
010011001000
100010111010
111110010001
001001011010
010101001011
100110001101
000100101000
001101111011
110110010100
011010000101
011000010000
110101110011
100110110001
000111100111
000001010101
001011110100
010101000101
110110010000
101010111110
111010011100
010000001010
001001100111
000000100001
110100001110
100110011111
111011110000
000001110010
111101111101
010101100001
100100000101
100000010010
100000001100
011000011010
000010010111
110010100111
101010000111
001010010011
110101001000
101100000110
001110101100
001101110001
101100001010
111111110100
010101010100
101110111111
000001111010
110110000111
000100000000
011000010100
011100011010
100011111100
001011011010
111101101011
011101000100
011111010011
111011010010
110000001110
010101010011
100010110111
111111000011
001110001000
110001000010
001010111101
000000101010
100011101111
100001000001
000000110010
101100011011
011001000101
111010110101
010100111111
100011111101
010010110111
110100000101
101000100100
010100111001
100001000111
111101000010
000100000111
100000011101
101101001101
000111101000
011010010001
001101011010
110001011011
000000011111
111001000100
100111101110
110010010010
101010101111
000100001100
000111000000
001001000100
010101110011
001101111111
111001010001
100110101101
100010011100
010101010010
011010101011
000011110011
101001001000
101111100100
011011001110
001110010001
110011001100
011000111001
110111000111
100100001101
100101111100
101110111101
001011111010
100110010011
100111111011
000010010011
100111101100"""

def get_most_frequent(input, idx):
    zero_freq=sum([1 for i in input if i[idx]=='0'])
    one_freq=sum([1 for i in input if i[idx]=='1'])
    if zero_freq>one_freq:
        return '0'
    else:
        return '1'

def get_least_frequent(input, idx):
    zero_freq=sum([1 for i in input if i[idx]=='0'])
    one_freq=sum([1 for i in input if i[idx]=='1'])
    if zero_freq>one_freq:
        return '1'
    else:
        return '0'

def get_int(binary_str):
    k=len(binary_str)
    val=0
    for i in range(k):
        power=k-i-1
        val+=int(binary_str[i])*2**power
    return val

input=input.splitlines()
# print(get_most_frequent(input,1))

g=''
e=''
for i in range(len(input[0])):
    g+=get_most_frequent(input,i)
    e+=get_least_frequent(input,i)

# print(g)
# print(get_int(e))
# # e=''
g_int = get_int(g)
e_int = get_int(e)
print(g_int*e_int)