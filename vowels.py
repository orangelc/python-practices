#!/usr/bin/python3

#Declaramos las variables
word = input("Provide a word to search for vowels: ")
vowels = ['a','e','i','o','u']
found = []

for letter in word:            
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for letter in found:
    print(letter)