import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the number of terms: "))
start_time = time.time()
print("Series")
f = 0
for i in range(n):
    #f = fibonacci(i)
    print(fibonacci(i))
print(" fibonacci number at ", n ," index is ", f)
end_time = time.time()
print("Execution time: ", end_time - start_time)
