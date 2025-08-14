# Task 2
import math

# 1. Ask the user for a number
num = float(input("Enter a number: "))

# 2. Calculations using math module
sqrt_value = math.sqrt(num)
log_value = math.log(num)        
sine_value = math.sin(num)        

# 3. Display results
print(f"Square root of {num} = {sqrt_value}")
print(f"Natural log of {num} = {log_value}")
print(f"Sine of {num} radians = {sine_value}")
