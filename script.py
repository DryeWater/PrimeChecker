def prime_checker(n):
    i = 2
    prime = True
    while i < n:
        if n % i == 0:
            prime = False
            break
        else:
            i += 1
    return prime

inputted_num = input("Enter a number: ")
try:
    num = int(inputted_num)
    if isinstance(num, int):
        r = prime_checker(num)
        if r:
            print(str(num) + " is prime")
        else:
            print(str(num) + " is not prime")
except ValueError:
        print("please input a number")




