import operator

def calculate():
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow
    }
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /, **): ")
            num2 = float(input("Enter second number: "))
            
            if op in ops:
                result = ops[op](num1, num2)
                print(f"Result: {result}")
            else:
                print("Invalid operator!")
        except ValueError:
            print("Invalid input! Please enter numbers only.")
        except ZeroDivisionError:
            print("Error! Division by zero.")
        
        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    calculate()
