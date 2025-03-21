from functools import reduce

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


def anagram_detector(input_one, input_two):
    if input_one.lower()[::-1] ==  input_two.lower():
        return print(f"it`s anagram -\"{input_one}\" and \"{input_two}\"")
    else:
        return print(f"it is not anagram -\"{input_one}\" and \"{input_two}\"")
    
        

# a = (revert_str_4("abcd"))
# print(a)


anagram_detector("kot", "tok")
