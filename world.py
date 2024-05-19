def my_vowels(name, vowels):
     
    count = sum(name.count(vowel) for vowel in vowels)
    print(count)
    
    # removing duplicates in int
def remove_duplicate():
    integers = set(integers)
    integers = list(integers)
    print(integers)
    integers[1,2,4,6,3,5,4,5,5,6,7,6]
    remove_duplicate(integers)
     
     
     # multiplying the num by itself   
n = 10
d =dict()
for x in range(1,n+1):
     d[x] = x * x
print(d)


# checks for anagram
def check_anagram(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    if sorted(str1) == sorted(str2):
        print(f"{str1} and {str2} are anagrams")
    else:
        print(f"{str1} and {str2} are not anagrams")

     #  reversing a string /string methods dont have reverse for you to reverse you change them to a list
def reverse_string(str3):
    str3 = list(str3)
    str3.reverse()
    str3 = " ".join(str3)
    print(str3)
    str3 = "Hapiness"
    reverse_string(str3)
    
    # counts the vowels in a string
def my_vowels(name,vowels):
     
    count = sum(name.count(vowel) for vowel in vowels)
    print(count)
    
name = "mumina abdo" 
vowels = "aeiouAEIOU"
my_vowels(name,vowels)  

