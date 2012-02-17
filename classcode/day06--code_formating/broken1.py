#!/usr/bin/env python

#variables
input_list = []
input_number = None

#Get list of numbers from user
while input_number != "":
    input_number = raw_input()
    if input_number.isdigit():
        input_list.append(float(input_number))

#Total the list of numbers
total = 0
for num in input_list:
    total += num

#Print average of list
print total/len(input_list)
