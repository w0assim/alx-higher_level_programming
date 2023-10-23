#!/usr/bin/python3
def remove_char_at(str, n):
    strDup = ""
    for i in range(len(str)):
        print(i)
        if i != n:
            strDup += str[i]
        return strDup
