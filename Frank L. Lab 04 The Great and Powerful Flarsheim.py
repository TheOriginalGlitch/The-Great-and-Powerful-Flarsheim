########################################################################
##
## CS 101 Lab
## Program # 4
## Name Frank Lopez
## Email fel5mm@mail.umkc.edu
##
## PROBLEM : Describe the problem
##  Must create a program to determine a number between 0 and 100 with only the remainder when divided by 3, 5, and 7.
## ALGORITHM : 
##      1. Gather the remainders of the number when divided by 3, 5, and 7
##      2. Handle the errors if input is incorrect/out of bounds with while statements
##      3. Use for loops and if statements to narrow the possibilities to one number
##      4. Create the 'play again' loop
## ERROR HANDLING:
##      Set 3 while loops, one for each input, and make the loop iterate again whenever an invalid input is given.
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

print('I am the Great and Powerful Flarsheim!')

keep_playing = 'y'
while keep_playing == 'Y' or keep_playing == 'y':
    list3 = []
    list5 = []
    list7 = []
    print('Think of a number between 1 and 100')
    remainder_3 = int(input('What is the remainder when you divide your number by 3? : \n'))
    while remainder_3 < 1 or remainder_3 >= 3:
        print('Oops! This number must be greater than or equal to 1 and less than 3.')
        remainder_3 = int(input('What is the remainder when you divide your number by 3? : \n'))
        if remainder_3 >= 3:
            print('Oops! This number must be less than 3.')
            remainder_3 = int(input('What is the remainder when you divide your number by 3? : \n'))
            continue
    remainder_5 = int(input('What is the remainder when you divide your number by 5? : \n'))
    while remainder_5 < 1 or remainder_5 >= 5:
        print('Oops! This number must be greater than or equal to 1 and less than 5.')
        remainder_5 = int(input('What is the remainder when you divide your number by 5? : \n'))
        if remainder_5 >= 5:
            print('Oops! This number must be less than 5.')
            remainder_5 = int(input('What is the remainder when you divide your number by 5? : \n'))
            continue
    remainder_7 = int(input('What is the remainder when you divide your number by 7? : \n'))
    while remainder_7 < 1 or remainder_7 >= 7:
        print('Oops! This number must be greater than or equal to 1 and less than 7.')
        remainder_7 = int(input('What is the remainder when you divide your number by 7? : \n'))
        if remainder_7 >= 7:
            print('Oops! This number must be less than 7.')
            remainder_7 = int(input('What is the remainder when you divide your number by 7? : \n'))
            continue
    for num in range(1,101):
        if num % 3 == remainder_3:
            list3 += [num]
    for num in list3:
        if num % 5 == remainder_5:
            list5 += [num]
    for num in list5:
        if num % 7 == remainder_7:
            list7 += [num]
    print('Your number was {}'.format(list7[0]))
    print('Your thoughts are like a book to me...')

    
    keep_playing = str(input('Would you like to play again? Y to continue, N to quit: '))
    if keep_playing == 'Y' or keep_playing == 'y':
        continue
    elif keep_playing == 'N' or keep_playing == 'n':
        break
    else:
        print('Oops! Something didn\'t make sense...')
        keep_playing = str(input('Would you like to play again? Y to continue, N to quit: '))
print("See you next time!")
