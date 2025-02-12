def is_anagrams(s,n):
    
    str1 = s.replace(" ","").lower()
    str2 = n.replace(" ","").lower()
    
    return sorted(str1) == sorted(str2)

string1 = "Listen"
string2 = "Silent"
if is_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
