import math
import collections


def pi_to_n_digit(num):
    # this function returns pi with precision of n numbers
    stringed_pi = str(math.pi)
    pi_to = stringed_pi[:num]
    return float(pi_to)


def fibonnaci(num):
    sequence = []
    for i in range(1, num):
        if i == 1 or i == 2:
            sequence.append(1)
        else:
            sequence.append(sequence[i-2]+sequence[i-3])
    return sequence


def prime_factors(num):
    # function that returns all prime factors of a given number
    prime_numbers = []
    prime_factor = []
    for i in range(num+1):  # for each number
        tab_of_factors = []  # find prime numbers lower or equal to this number
        for j in range(1, i+1):
            if i % j == 0:
                tab_of_factors.append(j)
        if len(tab_of_factors) == 2:
            prime_numbers.append(i)
    for i in prime_numbers:  # check if they are factors of the given number
        if num % i == 0:
            prime_factor.append(i)
    if len(prime_factor) == 0:
        return 'No prime factors'
    return prime_factor


def total_cost_of_tile(cost):
    cost_of_square = 10
    return 'YOu can cover ' + cost/cost_of_square + ' square meters'


def mortgage_payments(amount, years, interval='monthly'):
    # function that calculates mortgage payments for a given amount and time of mortgage
    annual_interest = -0.03
    if interval == 'yearly':
        number_of_payments = years
    elif interval == 'monthly':
        number_of_payments = years*12
    elif interval == 'quarterly':
        number_of_payments = years*4
    else:
        return 'Wrong interval at input'
    monthly_payment = (amount+(1+annual_interest)**number_of_payments)*(1-1-annual_interest)/(1-((1+annual_interest)**number_of_payments))
    return 'your monthly payment: ' + str(monthly_payment)


def change_return(cost, amount):
    # the user enters a cost and amount of money,
    # program calculates the change and the amount
    # of coins needed for it
    change = amount - cost
    spare_options = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    coins_given = []
    tmp = 0
    if change < 0:
        return 'The amount of money is too small to pay the cost'
    elif change == 0:
        return 'No change :('
    else:
        i = 0
        while i < len(spare_options):
            if tmp < change:
                coins_given.append(spare_options[i])
                tmp += spare_options[i]
            elif tmp == change:
                break
            else:
                coins_given.remove(spare_options[i])
                tmp -= spare_options[i]
                i += 1
    return collections.Counter(coins_given)


def binary_to_decimal(number, mode):
    # program converts given number from
    # decimal to binary or the other way
    # mode 1 is decimal -> binary
    # mode 2 is binary -> decimal
    if mode == 1:
        converted_number = []
        i = 0
        while 2**i <= number:
            i += 1
        size_of_decimal_number = i
        for i in range(size_of_decimal_number):
            converted_number.append(0)
        while number > 0:
            converted_number[len(converted_number)-int(math.log(number, 2)) - 1] = 1
            i = int(math.log(number, 2))
            number = number - 2**(i)
        return converted_number
    elif mode == 2:
        converted_number = 0
        num_as_list = list(str(number))
        for i in range(len(num_as_list)):
            if num_as_list[i] == '1':
                converted_number += 2**(len(num_as_list) - i - 1)
        return converted_number
    else:
        return "Choose the right mode"
# print(fibonnaci(100))
# print(pi_to_n_digit(10))
# print(prime_factors(66))
# print(mortgage_payments(100000, 2, 'quarterly'))
print(change_return(5, 111.39))
print(binary_to_decimal(937, 1))
print(binary_to_decimal(1110101001, 2))