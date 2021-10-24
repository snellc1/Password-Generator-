# Create a password that is 8 - 16 long. 
import random as rm 


lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
uppercase = [ ]
nums_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
special_letters = ['!', '@', '#', '$', "%"]
password = ''

for lower in lowercase:
    uppercase.append(lower.upper())

for x in range(rm.randint(8, 17)):
    password += rm.choice([rm.choice(lowercase), rm.choice(uppercase), str(rm.choice(nums_list)), rm.choice(special_letters)])

print(password)