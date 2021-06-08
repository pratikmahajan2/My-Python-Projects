def prime_range(num):

    count = 2
    while num+1 > count:
        i = 2
        IsPrime = True
        while count/2 > i:
            if count % i == 0:
                IsPrime = False
                break
            i += 1
        if IsPrime == True:
            print(f'Prime number: {count}')
        count += 1

prime_range(int(input("Enter a number: ")))