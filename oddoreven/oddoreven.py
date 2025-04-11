def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

def main():
    try:
        num = int(input("Enter a number: "))
        result = check_odd_even(num)
        print(f"The number {num} is {result}.")
    except ValueError:
        print("Please do not enter anything besides a number.")

if __name__ == "__main__":
    main()