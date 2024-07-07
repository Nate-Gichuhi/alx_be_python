num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /)")

match operation:
    case "+" : 
        result = num1 + num2
        print("The result is", result)
    case "-" :
        result = num1 - num2
        print("The result is", result)
    case "*" :
        result = num1 * num2
        print("The result is", result)
    case "/" :
        if num2 !=0 :
            result = num1 / num2 
            print("The result is", result)
        else :
            print("Error. Division by zero is not allowed.") 
    case _ :
        print("Invalid operation. Please choose one of the following operaions (+, -, *, /)")
        
