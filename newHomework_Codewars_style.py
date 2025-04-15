from functools import reduce
import math

def revert_str_1(input_str) -> str:
    out :str = ""
    for i in reversed(input_str):
        out += i
    return out

def revert_str_2(input_str):
    return input_str[::-1] # it`s usable 

def revert_str_3(input_str):
    return "".join(reversed(input_str)) # it`s usable 

def revert_str_4(input_str):
    return reduce(lambda akm, char: char+ akm, input_str, "") 


def anagram_detector(str1, str2):
    set1 = set(str1.lower())
    set2 = set(str2.lower())
    fl = True
    fl2 = True
    for char in set1:
        if char in set2:
            fl = True
        else: 
            fl = False
    for char in str1:
        if char in str2:
            fl2 = True
        else: 
            fl2 = False
    if fl and fl2 == True:
        return True
    elif (fl == False) and (fl2 == True):
        return True
    elif (fl == True) and (fl2 == False):
        return False
    else:
        return False


        
    # if input_one.lower()[::-1] ==  input_two.lower():
    #     return print(f"it`s anagram -\"{input_one}\" and \"{input_two}\"")
    # else:
    #     return print(f"it is not anagram -\"{input_one}\" and \"{input_two}\"")
    

def shwalengthimeter_word(inp_str):
    with_out1char = inp_str[1:]
    # print(with_out1char)

    if with_out1char[0] in {"a", "e", "o", "i", "u", "y"}:
        with_out1char = with_out1char[1:]
    # print(with_out1char)
    return f"shwa{with_out1char} {len(inp_str)}"


def shwalengthimeter(test_strings):
    out = []
    for word in test_strings:
        out.append(shwalengthimeter_word(word))
    return out


def gcd(one_int,two_int):
    return math.gcd(one_int,two_int)

# a = (revert_str_4("abcd"))
# # print(a)
# print(shwalengthimeter("aabcs"))
# print(gcd(12,15))
# anagram_detector("kot", "tok")
# print(anagram_detector("Good", "gooOD"))

# print(shwalengthimeter(["kawabunga", "metro2013", "moon", "orange"]))

# def count_rabbits_chickens(heads, legs):
#     if legs % 2 != 0:
#         return "error"
#     if 
    
#     return 1, 1
    
    
# print(count_rabbits_chickens(3, 10))
# print(list(range(1, 11)))

def result():
    sec_in_year = 365*24*60*60
   
    return set(str(sec_in_year)).__len__()
    
    
print(result())