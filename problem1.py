import math
def num_to_dig(num):
    dig = []
    while num>0:
        dig.append(num%10)
        num = num//10
    return dig

def payload(card_number):
    mult = 2
    arr_mult = num_to_dig(int(card_number))
    sum_digits = 0
    for i in range(len(arr_mult)):
        each_num_mult = arr_mult[i]*mult
        arr_mult_nums = num_to_dig(each_num_mult)
        sum_for_test = 0
        for nums in arr_mult_nums:
            sum_for_test += nums
        sum_digits += sum_for_test
        if(mult==2):mult=1
        else:mult=2
    ceil_sum = 0
    if sum_digits%10 != 0:
        ceil_sum = sum_digits // 100
        last_digit = sum_digits // 10
        last_digit = last_digit % 10
        ceil_sum *= 10
        ceil_sum += last_digit+1
        ceil_sum *= 10
    else:
        ceil_sum = sum_digits
    return ceil_sum - sum_digits

card_number = int( input("Input card number:") )
print(f"Checker is: {payload(card_number)}")
#7992739871