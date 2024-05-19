def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print (number)

def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 == 0:
            print(number)
            
def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is even") 
        else:
            print(f"{number} is odd")   
            
def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number % 3 == 0:
            print(f"{numbers} is divisible by 3")
        elif number % 5 == 0:
            print(f"{number} is divible by 5")
        elif number % 7 == 0:
            print(f"{number} is divisible by 7")
        else:
            print(f"{number} is not divisible by 3,5 or 7")  
            
def count_down(n):
    x = 0
    while n > x:
        print(n)
        n -= 1  
        
def count_down_to_five(n):
    x =  0
    while n > x:
        print(n)
        if n == 5:
            break
        n-=1
        
def divisible_by_seven(n):
    x = 1
    while x < n:
        x +=1 
        if x % 7 != 0:
            continue
        print(f"{x} is divisible by 7")  
        
# Using while, contine and if statement , write a function that print all the odd numbers between 0 and 100 
# fizz for number % 3
# buzz fro number% 5
# fizzbuzz for number % 3 and 5

def fizzbuzz(n):
    numbers = range(n)
    for number in numbers:
        if number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        elif number % 3 and 5 == 0:
            print("fizzbuzz")
        else:
            print("fizzbuzz")  
            
      
                                                                        
    