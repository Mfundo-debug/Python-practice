x = [0,1,0,3,2]
move_zeros = [x for x in x if x!=0] + [0] * sum(1 for x in x if x==0)
print(move_zeros)