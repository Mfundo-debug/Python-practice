x = [1,2,3,4,5,6,7,8,9,10]
even_nums = []
for i in x:
    if i % 2 == 0:
        even_nums.append(i)
print(even_nums)

#Alternative method

even_nums = [i for i in x if i % 2 == 0]
print(even_nums)