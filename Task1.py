# Task 1
# Finding factorial with recursion function
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        factorial=n*fact(n-1)
    return factorial
n=int(input("Enter the number! "))
a=fact(n)
print(f"factorial of {n} is: {a}")