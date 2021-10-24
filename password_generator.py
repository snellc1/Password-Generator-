# Create a password that is 8 - 16 long. 
import random

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
uppercase = []
nums_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
special_letters = ['!', '@', '#', '$', "%"]

for lower in lowercase:
    uppercase.append(lower.upper())