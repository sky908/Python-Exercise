# number = int(input('Enter your Number'))
# sum = 0
#
# temp = number
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
#
# if number == sum:
#     print(number, 'It is an armstrong number')
# else:
#     print(f'{number} is not an armstrong number')

# leap year
# Year = int(input('Enter your year: '))
#
# if (Year % 400 == 0) or (Year % 100 == 0):    #no which are divisble 4 or add by 4 in it ( 4 8 16 32etc)
#     print(f'{Year} is a leap year.')
#
# else:
#     print(f'{Year} is not a leap year.')


# Factorial No
number = int(input('Enter number: '))
factorial = 1
if number < 0:
    print('factorial does  not exist negative numbers')

elif number == 0:
    print('factorial of 0 is 1')

else:
    for i in range(1, number + 1):
        factorial = factorial*i
    print(f'The factorial of {number}, is {factorial}.')

# number = int(input('Enter your number: '))
# fact = 1
# for i in range(number,0,-1):
#         fact = fact*i
# print('fact')


















































