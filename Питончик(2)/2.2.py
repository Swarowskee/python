#coding=utf-8
text = input("текст:")
dct = {}

for letter in text:
    if letter != ' ':  
        letter = letter.lower()  
        if letter in dct:
            dct[letter] += 1
        else:
            dct[letter] = 1

print(dct)