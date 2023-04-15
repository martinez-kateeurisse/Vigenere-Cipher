#Kate Eurisse L. Martinez_BSCPE 1-5_OOP Assignment 2-Problem 2

#PROBLEM 3 - The Vigenère Cipher  
#A program that asks the user for the plaintext and the keyword and produce the ciphertext using the Vigenère cipher. 

#Create a dictionary for the keys and values
letter_values = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

#Initialize lists
message_list = []
key_list = []
ciphertext_list = []

#Ask the user for the message
message_input = str(input("Please enter the message (all uppercase letters, no spaces): ")).upper()
#Iterate over the user's input
for i in message_input:
    #Get the values of each character in the dictionary
    message_value = letter_values.get(i)
    #Append the value to a list
    message_list.append(message_value)
#Print the list of values (depending on user)
message_reveal = input("Do you want to see the equivalent value of your message?(Type 'y' if yes, any key if no): ").lower()
if message_reveal == 'y':
    print("The values of the characters in your message are " + str(message_list))
    print("="*100)
else:
    print("="*100)

#Ask the user for the key
key_input = str(input("Please enter the key (all uppercase letters): ")).upper()
#Iterate over the user's input 
for i in key_input:
    #Get the values of each character in the dictionary
    key_value = letter_values.get(i)
    #Append the value to a list
#Print the list of values

#Repeat the values of the key until it matches the lenght of the message
#Add the values of the message and key and get their mod 26
#Convert the keys into their corresponding values in the dictionary

#Print the cipher text as a string

#Display the input with the use of pygame