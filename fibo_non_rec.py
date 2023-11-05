import time

def iter():
    n = int(input("Enter the number of terms: "))
    start_time = time.time()
    # first two terms
    a = 0
    b = 1
    f = 0
            # check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence upto", n, ":")
        print(a)
    else:
        
        for i in range(n):
            f = a
            c = a + b
            a = b
            b = c
    print(" fibonacci number at ", n ," index is ", f)
    end_time = time.time()
    print("Execution time: ", end_time - start_time)
iter()