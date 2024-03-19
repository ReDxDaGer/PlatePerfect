import random

def range_calc(num1, num2):
    a = int(input(f"""
              Do you want to have a random number generated from the range of {num1} to {num2} 
              or do you want to perform some kind of sum?
              ** Press 1 for random numbers
              ** Press 2 for summing digits.
              """))

    if a == 1:
        random_numbers = [random.randint(num1, num2) for _ in range(30)]
        print(f"""
                The random numbers that you requested are below: \n
                {random_numbers}
             """)
    elif a == 2:
        choice = int(input("""
                  Please enter the sum of the digits you want from the number: \n
                  1, 2, 3, 4, 5, 6, 7, 8, 9
                  """))
        filtered_numbers = [num for num in range(num1, num2 + 1) if sum_digits(num) == choice]
        print(f"""
            Random numbers with sum of digits equal to {choice}: \n
            {filtered_numbers}
         """)
    else:
        print("Please enter a valid response")

def sum_digits(num):
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num

num1 = 0
print(f"The intial part of range is {num1}")
num2 = int(input("Enter the ending of the range !!"))

range_calc(num1,num2)
