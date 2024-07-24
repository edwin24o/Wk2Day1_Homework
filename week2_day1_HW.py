# Calculator

def addition():
    while True:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Please enter the second number you would like to add: "))
        except ValueError:
            print("Error no number was determined")
        except Exception as e:
            print(f"Unexpected error: {e}")
        else:
            print(f"The sum of {a} + {b} = {a + b}")
            break
        
def subtraction():
    while True:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Please enter the second number you would like to subtract: "))
        except ValueError:
            print("Error no number was determined")
        except Exception as e:
            print(f"Unexpected error: {e}")
        else:
            print(f"The result of subrtacting {a} - {b} = {a - b}")
            break
        
def division():
    while True:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Please enter the second number you would like to divide: "))
        except ValueError:
            print("Error no number was determined")
        except ZeroDivisionError:
            print("Error you can not divide by 0..")
        except Exception as e:
            print(f"Unexpected error: {e}")
        else:
            print(f"The result of dividing {a} / {b} = {a / b}")
            break
        
def multiply():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Please enter the second number you would like to divide: "))
        except ValueError:
            print("Error no number was determined")
        except Exception as e:
            print(f"Unexpected error: {e}")
        else:
            print(f"The result of multiplying {a} * {b} = {a * b}")
            break        
                
        

def main():
    while True:
        action = input('''
Calculator Menu:
                       
1. Addition 
2. Subtracting
3. Division                       
4. Multiplication
5. Exit    
''' )
        
        if action == "1":  
            addition() 
        elif action == "2": 
            subtraction()
        elif action == "3":
            division()
        elif action == "4":
            multiply()
        elif action == "5":
            break

main()