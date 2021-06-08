seq = input("Enter a string to create pyramid: ")
for i in range(1,len(seq)+1):
    print(' '*(len(seq)-i),f'{seq[i-1]} '*i)
for i in range(1,len(seq)):
    print(' '*i,f'{seq[((-1)*i)-1]} '*(len(seq)-i))