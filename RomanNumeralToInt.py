#Function takes a valid Roman Numeral String and returns its' integer representation
class Solution(object):
    def romanToInt(s):
        dict = {'I':'1', 'V':'5', 'X':'10', 'L':'50', 'C':'100', 'D':'500', 'M':'1000',
                'IV':'4', 'IX':'9',
                'XL':'40', 'XC':'90',
                'CD':'400', 'CM':'900'}
        intTotal = 0
        i = 0
        while s[i:i+1] != "":
            currentNumeral = s[i:i+1]
            if currentNumeral == "I" or currentNumeral == "X" or currentNumeral == "C":
                nextNumeral = ""
                try:
                    nextNumeral = s[i+1:i+2]
                except ValueError:
                    nextNumeral = False
                    
                if currentNumeral == "I" and nextNumeral != "V" and nextNumeral != "X":
                    nextNumeral = False
                if currentNumeral == "C" and nextNumeral != "D" and nextNumeral != "M":
                    nextNumeral = False
                if currentNumeral == "X" and nextNumeral != "L" and nextNumeral != "C":
                    nextNumeral = False
                    
                if nextNumeral is not False:
                    currentNumeral = s[i:i+2]
                    i += 1

            intTotal += int(dict[currentNumeral])
            i += 1
        return intTotal

    #Driver Code to test method romanToInt
    result = romanToInt("MCMXCIV")
    print(result)
