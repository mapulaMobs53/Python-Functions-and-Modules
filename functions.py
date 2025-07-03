'''
def greet(name):
    print(f"Hello, {name}")
    
greet("Mapula")

def add(a,b):
    return a+b
result = add(2,5)
print(result)'''

def factorial(n):
    if n == 0:
        return 0
    else:
        return n*factorial(n-1)
factorial(5)
def greet(name, greeting="Hello"):
    print(f"{greeting},{name}")
    
greet("Bob","Good Morning")
