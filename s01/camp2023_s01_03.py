#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/26 21:35:21 (CST) daisuke>
#

# reading an integer from keyboard input
i_str = input ('Type an integer using keyboard: ')

# conversion from a string into an integer
i_int = int (i_str)

# if and else statement
if (i_int % 2 == 0):
    print (f'{i_int} is divisible by 2 and it is an even number.')
else:
    print (f'{i_int} is not divisible by 2 and it is an odd number.')
