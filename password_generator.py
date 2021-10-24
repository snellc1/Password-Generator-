# Create a password that is 8 - 16 long. 
import random as rm 

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
uppercase = []
nums_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_letters = ['!', '@', '#', '$', "%"]

# Making uppercase list
for lower in lowercase:
    uppercase.append(lower.upper())

#Randomly select a character from above list
rand_lower = rm.choice(lowercase)
rand_upper = rm.choice(uppercase)
rand_letter = rm.choice(special_letters)
rand_number = rm.choice(nums_list)

#Combine all list
combine_list = lowercase + uppercase + special_letters + nums_list

#Creating password string to include 1 upper, 1 lower, 1 special letter, and 1 number
password = rand_upper + rand_lower + rand_letter + rand_number

for x in range(rm.randint(4, 12)):
    password += rm.choice(combine_list)

print(password)