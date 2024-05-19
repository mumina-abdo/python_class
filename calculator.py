def add(x,y):
    result = x+y
    return result

def subtract(a,b):
    result = a-b
    return result

def divide(h,j):
    result = h/j
    return result

def multiply(c,d):
    result = c*d
    return result

def remainder(f,g):
    result = f%g
    return result

def powerof(i,h):
    result = i**h
    return result

def power(q,w):
    result = q**w
    return result

def sum(*numbers):
    total = 0
    for number in numbers:
        total+= number
    return total


def multiply(*nums):
    total = 1
    for num in nums:
        total*=num
    return total  

def create_sentence(**words):
    print(words)
    sentence = " "
    for word in words.values():
        sentence += word
        sentence += " "
    return sentence


def sum_and_greet(*args, **kwargs):
    total = 0
    for x in args:
        total += x
        
    f = kwargs["first_name"]
    l = kwargs["last_name"]
    greeting = f"Hello {f} {l} the sum of your number is {total}" 
    return greeting
       
    
        
    