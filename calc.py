# Defining Operations 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Main Logic Function 
def operation():
    cont = "y"
    while cont.lower() == "y":

        print("Please select an operation: ")
        print("add")
        print("subtract")
        print("multiply")
        print("divide")
        
        ops = input("Enter an operation: ")
        x = input("Please enter a number: ")
        y = input("Please enter a second number: ")
        x = int(x)
        y = int(y)
        acceptable_ops = ["add", "subtract", "multiply", "divide"]

    
        if ops.lower() not in acceptable_ops:
            raise ValueError("Sorry, available operators are: 'add', 'subtract', 'multiply', or 'divide'. -_-")
        else:
            if isinstance(x, int) and isinstance(y, int) == False:
                raise TypeError("Please enter a number. <.<")
            else: 
                if ops == 'add':
                    print(x, "+", y, "=", add(x,y))
                elif ops == 'subtract':
                    print(x,"-",y,"=", subtract(x,y))
                elif ops == 'divide':
                    if y == 0:
                        raise ZeroDivisionError("You can't divide by zero, dummy! <.<")
                    else:
                        print(x,"/",y,"=", divide(x,y))
                else:
                    print(x,"*",y,"=", multiply(x,y))
        cont = input("Would you like to enter another operation? (y/n):  ")
        if cont == "n":
            print("Thanks for using my Calculator!")
            break

# call operation function                
operation()