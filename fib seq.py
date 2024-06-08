#fib
n_terms = int(input('first how much to be displayed? '))
n1, n2 = 0, 1
count = 0
if n_terms <= 0:
    print("enter valid number of terms")
elif n_terms <= 1:
    print("sequence is 0") 
elif n_terms >=4300:
    print("pick less")
else:
    print("The sequence is:")
    while count < n_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1