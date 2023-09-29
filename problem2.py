def rec_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + rec_sum(lst[1:])


my_list = [1, 2, 5]
result = rec_sum(my_list)
print(result)
