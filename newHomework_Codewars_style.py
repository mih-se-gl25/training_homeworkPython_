import datetime
from functools import reduce
import math
import re
from collections import Counter

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
    
    
# print(result())




def input_legacy_string(input_str):
    pattern = r'"LegacyBatteryInfo"\s*\[\s*[^]]*?"Capacity"\s*-\s*(\d+)[^]]*?"Current"\s*-\s*(\d+)[^]]*?\)'    
    legacy_bock = re.search(pattern, input_str)
    if legacy_bock:
        max_capacity = int(legacy_bock.group(1))
        current_capacity = int(legacy_bock.group(2))
        output = (current_capacity/max_capacity) * 100


    return f"{output:.2f}"

def get_battery_percentage(input_string):
    pattern_max = r'"MaxCapacity":\s*[+-]?(\d+)'
    pattern_current = r"'CurrentCapacity'=\s*(\d+)"
    match1 = re.search(pattern_max, input_string)
    match2 = re.search(pattern_current, input_string)

    max_capacity = int(match1.group(1))  
    current_capacity = int(match2.group(1))  
    percentage = (current_capacity / max_capacity) * 100
    return f"{percentage:.2f}"
data = '''
        "SuperMaxCapacity" =0
        "MaxCapacity": +4540;
        'CurrentCapacity'=   2897,
        "LegacyBatteryInfo" = {"Amperage"=18446744073709550521,"Flags"=4,"Capacity"=4540,"Current"=2897,"Voltage"=7283,"Cycle Count"=406}
        "MegaMaxCapacity" = 6700
'''
# input_legacy_string(data)
# print(get_battery_percentage(data))

list1 = [
    {"id": "3456", "message": "Service started OK", "datetime": 1474624881},
    {"id": "123124", "message": "DB stopped! Whatta hell!", "datetime": 1474456391},
    {"id": "12353", "message": "MQ broker is not brokering!", "datetime": 1474624591},
    {"id": "1223134", "message": "U hev bin pwned by hax0r tim!", "datetime": 1474624799},
    {"id": "1213234", "message": "Need more vespene gas!", "datetime": 1474624791},
]

list2 = [
    {"id": "3456", "message": "Service started OK", "datetime": 1474624881},
    {"id": "12353", "message": "MQ broker is not brokering!", "datetime": 1474624591},
    {"id": "3334113", "message": ""'; DELETE FROM customers WHERE 1 or username = '"; ", "datetime": 1474624789},
    {"id": "1213235", "message": "Require more minerals!", "datetime": 1474624792},
]

def merge_logs(list1, list2):
    temp_set = set()
    for i in list1:
        st= tuple((i.items()))
        temp_set.add(st)
    for j in list2:
        st = tuple((j.items()))
        temp_set.add(st)

    result = sorted([dict(items) for items in temp_set], key= lambda x: x['datetime'])
    return (result)

# print(merge_logs(list1, list2))

test_data = ["az", "toto", "picaro", "zone", "kiwi"]

def partlist(list_):
    number = 0
    out_list=[]
    separator = " "
    while number < len(list_):
        for word in list_:
            one_tup =  (separator.join(list_[:number+1]))
            two_tup  = (separator.join(list_[number+1:]))
            if two_tup == "":
                number = number+1
                break
            step_tuple = (one_tup, two_tup)
            out_list.append(step_tuple)
            number = number +1
    return out_list
	
# print(partlist(test_data))
                               
songs_db = [ {
 'artist': 'Led Zeppelin', 
 'title': 'Stairways to heaven', 
 'playback': '09:20' 
}, {
 'artist': 'Metallica', 
 'title': 'Master of puppets', 
 'playback': '04:30' 
}, {
 'artist': 'Nirvana', 
 'title': 'The Man who sold the world', 
 'playback': '03:10' 
}, {
 'artist': 'Stepan Galyabarda', 
 'title': 'Lyst do mamy', 
 'playback': '02:20' 
}]

def get_song(db, len_seconds):
    # ...
    sorted_ = []
    for track in db:
        min,sec = map(int, track['playback'].split(':'))
        int_sec = min*60 + sec
        print(int_sec)
        if int_sec < len_seconds:
            temp_dict = {int_sec : track}
            sorted_.append(temp_dict)
    # print(sorted_)
    sorted(sorted_,key=lambda x: list(x.keys())[0], reverse=True)
    result = list(sorted_[0].values())[0]
    return f"Best possible song: {result['artist']}/{result['title']}"    # return "Best possible song: {}/{}".format(
    #     db[-1]['artist'],
    #     db[-1]['title'])

# print(get_song(songs_db, 145))
def anagram_d(str1, str2):
    set1 = set(str1.lower())
    set2 = set(str2.lower())
  
    if Counter(set1) == Counter(set2):  # compare character counts
        return True
    else:
        return False



test_list = ["tsar", "rat", "tar", "star", "tars", "cheese"]

def group_anagrams(test_list):

    result =[]
    for word in test_list:

        temp_list =[word]
        for i in test_list:
            if word != i:
                if anagram_d(word,i) == True:
                    temp_list.sort(reverse=False)
                    temp_list.append(i)
        result.append(temp_list)
    for j in result:
        i =0
        for j1 in result[::-1]:
            
            if sorted(j) == sorted(j1):
                i = i+1
            if i == 2:
                result.remove(j1) 
                i = 0
                
                    
    return result

# print(group_anagrams(test_list))
                                    
def an_groups(test_list):
    anagrams_group ={}
    for word in test_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in anagrams_group:
            anagrams_group[sorted_word] = []
        anagrams_group[sorted_word].append(word)
    return list(anagrams_group.values())

print(an_groups(test_list))