#Kate Eurisse L. Martinez_BSCPE 1-5_OOP Assignment 2-Problem 2

#PROBLEM 3 - The Vigenère Cipher  
#A program that asks the user for the plaintext and the keyword and produce the ciphertext using the Vigenère cipher. 

#Importing color modules
import colorama
from colorama import Back, Fore, Style 
colorama.init(autoreset = True)

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
    key_list.append(key_value)
#Print the list of values (depending on user)
key_reveal = input("Do you want to see the equivalent value of your key?(Type 'y' if yes, any key if no): ").lower()
if key_reveal == 'y':
    print("The values of the characters in your key are " + str(key_list))
    print("="*100)
else:
    print("="*100)

#Repeat the values of the key until it matches the lenght of the message
while len(key_list) < len(message_list):
    key_list += key_list
key_list = key_list[:len(message_list)]

#Add the values of the message and key and get their mod 26
for i in range(0, len(message_list)):
    ciphertext_list.append((message_list[i] + key_list[i]) % 26)
#Printing the values (depending on user)
value_reveal = input("Do you want to see the numeric value of the cyphertext?(Type 'y' if yes, any key if no): ").lower()
if key_reveal == 'y':
    print("The values of the characters in the cyphertext are " + str(ciphertext_list))
    print("="*100)
else:
    print("="*100)

#Convert the values into their corresponding keys in the dictionary through iteration
ciphertext = '' #initializing ciphertext
for value in ciphertext_list:
    for key in letter_values:
        if letter_values[key] == value:
            ciphertext += key + ' '

#Print the cipher text as a string
print("The ciphertext of the given message (" + message_input , ") and key (" + key_input , ") is:\n")
#Printing instructions for output execution
print("="*25,("Please click the pygame window to see the output"),"="*25)
ciphertext = (ciphertext.replace(' ',''))

#Display the input with the use of pygame
#Importing modules
import pygame
import sys

#Initializing variables
pygame.init()
#Initializing display format(dimension)
display_width = 550
display_height = 350
display = pygame.display.set_mode((display_width,display_height))

#Set text formats(font and color), position and background
output_font = pygame.font.Font("Gamerock.otf", 30)
output_text = output_font.render(ciphertext, True, (250,250,250))
text_rect = output_text.get_rect()
text_rect.center = (display_width//2, display_height//2)
background = pygame.image.load("background.jpg")

#Running the program in pygame
#Using a loop to run the program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    display.fill((0,0,0))
    display.blit(background, (0,0))
    display.blit(output_text, text_rect)
    pygame.display.update()
#The output of the program will be displayed in the pygame window