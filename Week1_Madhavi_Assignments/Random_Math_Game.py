'''Random is something different every time like rolling a dice, it is randoly generated the numbers bet cetween 1 to 10 and 
 the operators(+,-) it produce the result differently every time we run the code.It is using predefined random function to generate the numbers & operators'''

# HW 2 Example : Return 2 random values and a random operator.
import random

def get_random_function_values():
    num1= random.randint(1, 10)
    num2= random.randint(1,10)
    op= random.choice(['+', '-'])
    return num1,num2,op
   # print(get_random_function_values())
print(get_random_function_values())
    

# HW 3: Return the result of number1 and number2 along with the operator.
import random
def get_random_function_values():
	
	num1= random.randint(1, 10)
	num2= random.randint(1, 10)
	op= random.choice(['+', '-', '*', '/'])
	return num1,num2,op

num1,num2,op = get_random_function_values()

if op =='+':
   result = num1+num2

elif op == '-':
   result=num1-num2
elif op == '*':
    result=num1 * num2   
else:
    result=num1/num2

print(num1,op,num2, "  =  ",  result) 