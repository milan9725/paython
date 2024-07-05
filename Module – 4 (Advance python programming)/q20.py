def get_odd_number():
    while True:
        try:
            num = int(input("Enter odd number: "))
            if num % 2 == 0:
                raise ValueError("Even number entered. Please enter odd number.")
            else:
                return num
        except ValueError as ve:
            print(ve)


try:
    odd_number = get_odd_number()
    print("You entered odd number:", odd_number)
except KeyboardInterrupt:
    print("\n Program terminated by user.")