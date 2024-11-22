def is_even(number):
    return number % 2 == 0

def main():
    number = int(input("Enter a number: "))
    if is_even(number):
        print("even number.")
    else:
        print("odd number.")

if _name_ == "_main_":
    main()
