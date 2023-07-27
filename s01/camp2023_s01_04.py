#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/26 21:57:44 (CST) daisuke>
#

# initialisation of a variable "total"
total = 0

# for each number between 1 and 1000
for i in range (1, 1001):
    # adding "i" to "total"
    total += i

# printing result
print (f'1 + 2 + 3 + ... + 998 + 999 + 1000 = {total}')
