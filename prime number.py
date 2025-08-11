def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i==0:
            return False
        return True

while True:
    user_input=input("Enter a number to check (or type 'exit' to quit): ")
    if user_input.lower()== "exit":
        print("Exiting prime checker, goodbye!")
        break
    if not user_input.isdigit():
        print("please enter a valid positive integer.")
        continue
    number =int(user_input)
    if is_prime(number):
        print(number,"is a prime number")
    else:
        print(number,"is NOT a prime number")