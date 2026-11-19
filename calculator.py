first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

operation = input("Choose an operation (+, -, *, /): ")

if    operation == "+":
    result = first_number + second_number
    print("Result:", result)

elif operation == "-":
    result = first_number - second_number
    print("Result:", result) 

elif operation == "*":
    result = first_number * second_number
    print("Result:", result)

elif operation == "/":
    if second_number == 0:
        print("Error: You cannot divide by zero.")
    else:
        result = first_number / second_number
        print("Result:", result)
else:        
    print("Error: Invalid operation.")

## Python Implementation

I successfully implemented the Simple Calculator using Python.

### What I learned

- `input()` receives information from the user.
- `float()` converts input into decimal numbers.
- `if` checks a condition.
- `elif` checks another condition when the previous condition is false.
- `else` runs when none of the previous conditions is true.
- Nested conditions allow me to check for special situations.
- Division by zero must be prevented.
- Error handling helps the program respond safely to invalid operations.

### Calculator Operations

1. Addition (`+`)
2. Subtraction (`-`)
3. Multiplication (`*`)
4. Division (`/`)

### Testing Results

| Test | Expected Result | Status |
|---|---|---|
| Addition: 10 + 5 | 15.0 | Passed |
| Division: 10 / 0 | Error message | Passed |
| Invalid operation: % | Error message | Passed |

**Tier 3 Status: COMPLETED** 
