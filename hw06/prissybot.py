#!/usr/bin/env python
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""

# Step 1:
# -----------------------
# Program the following.
# 
#    $ python prissybot.py
#    Enter your name:  Paul
#   
#    PrissyBot: Hello there, Paul
#    Paul: hi bot
#    PrissyBot: You mean, "hi bot, sir!"
# 
# Make sure the user inputs their own name and responses.



# Step 2:
# -----------------------
# Keep adding to the conversation. Make sure that your program 
# includes the following:
# 
#  * get and use input from the user
#  * 3 math problems
#     * at least one should get numbers from the user
#  * at least 3 insults


# Advanced
# -------------------------
# Make sure your prissy bot uses string formatting throughout.  
# Also, create new programs for the following:
#  
#  1. draw some kind of ascii art based on user input
#  2. print a decimal/binary/hexidecimal conversion table 
#     * well formated and labeled
#     * reads 5 numbers from the input (all less than 256)
#  3. reduce a fraction
#     * read a numerator and denominator from the user
#     * ex.  6/4 = 1 2/4

#Defining variables
prissy = "Prissybot: "
name = raw_input("Enter your name: ")
prompt = name + ": "

print prissy, "Hello there,", name

reply1 = raw_input(prompt)

print prissy, "You mean " + "'" + reply1 + ", sir!'"
print prissy, "Math is fun! Don't you agree?"

reply2 = raw_input(prompt)

print prissy, "I'm not really interested in your opinion,", name + "."
print prissy, "What is 3 divided by 2?"

reply3 = raw_input(prompt)

print prissy, "No, stupid. 3/2 is obviously equal to", 3/2
print prissy, "Maybe your clearly inferior human brain needs something simpler. How about 3+4?"

reply4 = raw_input(prompt)

print prissy, "3+4 is", 3 + 4
print prissy, "Well you'll never be able to compete with my intellect. Try me. I'm going to ask you for 3 numbers, which I will multiply together."

birthyr = int(raw_input("Enter the year you were born: "))
fave_num = float(raw_input("Enter your favorite number (decimals make it even more fun!): "))

print prissy, birthyr, "*", fave_num, "=", birthyr*fave_num, "That was easier than your mother."

reply5 = raw_input(prompt)

print prissy, "First, that's '" + reply5 + ", sir!' Second, talking to you has been utterly mundane. Goodbye."
print "Application 'prissybot.py' terminated."
