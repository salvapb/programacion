letter = input().strip()


vowels = {'a', 'e', 'i', 'o', 'u'}
uppercase_vowels = {v.upper() for v in vowels}


if letter.isupper():
    print("uppercase")
else:
    print("lowercase")

if letter in vowels or letter in uppercase_vowels:
    print("vowel")
else:
    print("consonant")