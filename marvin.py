#!/usr/bin/python3

paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)

for char in letters[:6]:
    print('\t'*2,char)

for char in letters[-7:]:
    print('\t'*3,char)


for char in letters[12:20]:
    print('\t'*4,char)