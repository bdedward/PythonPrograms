#This solution takes a string representation of an integer and returns a signed integer

#It also checks the bounds of a 32-bit signed integer. If the resultant integer is
#outside of the bounds 2**31 -1 & 2**31, then returns the lower or upper limit of the 
#32-bit signed integer

#This solution will also parse the first integer, even if this number is attached to a word
#which contains characters other than digits.  However, this solutions returns 0 if the first
#word begins with characters other than a digit

import string
class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if s == "":
            s = "0"
        sign = s[0:1]
        s = s.split()[0]
        if(sign == "-" and len(s) > 1):
            s = s[1:]
        elif(sign == "+" and len(s) > 1):
            s = s[1:]
        elif sign == "+" or sign == "-" and len(s) == 1:
            s = "0"
        s = s.split()[0]
        if not s[0].isdigit():
            s = "0"
        no_digits = string.printable[10:]
        trans = str.maketrans(no_digits, " " * len(no_digits))
        try:
            s = int(float(s.translate(trans).split()[0]))
        except ValueError:
            s = 0
        if sign == "-":
            s = -abs(s)
        if(s < -2 **31):
            s = -2 **31
        if(s > 2**31 -1):
            s = 2**31 -1
        return s
