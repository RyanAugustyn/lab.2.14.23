#Task 1: Reverse a String 

#start with an initial string
#create a new string placeholder
#remove the last letter of the string and add to the new string
#repeat until reaching the first letter of the initial word

#inefficient version: works by translating string into a list, then looping through with pop() function and putting those in a new list to be returned 
def reverse_string(initial_string):
    length = len(initial_string)
    string_placeholder = ""
    string_list = []
    for letter in range(length):
        string_list += initial_string[letter]
    for letter in range(length):
        string_placeholder += string_list.pop()
    return string_placeholder

# sample = reverse_string("Hello")
# print(sample)


#Task 2: Capitalize a Letter

#take a string of any length such as a sentence or paragraph
#loop through each letter
#if is is the first letter, or it is the letter immediately following a space, change to capital 
#looked up method: .upper() translates a string to uppercase

def capitalize_first_letters(input_string):
    new_string = input_string[0].upper()
    previous_letter = input_string[0]
    for x in range(1, len(input_string)):
        if previous_letter != " ": 
            new_string += input_string[x]
            previous_letter = input_string[x]
        elif previous_letter == " ":
            new_string += input_string[x].upper()
            previous_letter = input_string[x]
    return new_string

# test = capitalize_first_letters("this is a sentence testing the function, please work")
# print(test)


#Task 3: Palindrome

#take user input 
#reverse the string and save as a variable
#compare the two strings for equivalance and return true if so
#user lower() function to make sure capitalization isn't messing it up

def is_palindrome(input_string):
    input_string = input_string.lower()
    reversed_input = ""
    for letter in range(len(input_string) - 1, -1, -1):
        reversed_input += input_string[letter]
    if input_string == reversed_input:
        return True
    else:
        return False

# test = is_palindrome("Tacocat")
# print(test)


#Task 4 : Compress a string of characters

#take string input 
#identify first letter
#loop through and count how many times that letter appears in a row
#add the count and the letter into a return string 
#repeat until sequence is finished

def compress_string(input_string):
    result = ""
    current_letter = input_string[0]
    count = 1
    for x in range(1, len(input_string)):
        if input_string[x] == current_letter:
            count += 1
        elif input_string[x] != current_letter:
            letter_count = str(count)
            result += letter_count + current_letter
            current_letter = input_string[x]
            count = 1       
    letter_count = str(count)
    result += letter_count + current_letter
    current_letter = input_string[x]

    return result

# test = compress_string("aaabbbbbccccaacccbbbaaabbbaaa")
# print(test)



