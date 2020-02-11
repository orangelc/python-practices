#!/usr/bin/python3

#Declaramos las variables
word="Milliways"
vowels = ['a','e','i','o','u']
found = []

for letter in word:            
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for letter in found:
    print(letter)