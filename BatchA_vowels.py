'''
Docstring for vowels
print yes if the provided string s is a vowel and no otherwise
constraint: s should have length 1
'''

s = input("Enter s: ")

if len(s) == 1:
    if s in ["a","b","c","d","e"]:
        print("yes")
    else:
        print("no")
else:
    print("Length not 1")



