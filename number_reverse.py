def reverse_number(number):
    negative = number < 0
    number_str = str(abs(number))
    reversed_str = number_str[::-1]
    
    if '.' in reversed_str:
        reversed_number = float(reversed_str)
    else:
        reversed_number = int(reversed_str)
    
    if negative:
        reversed_number = -reversed_number
    
    return reversed_number

def main():
    user_input = input("Enter a number: ")
    
    if '.' in user_input:
        try:
            number = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return
    else:
        try:
            number = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

    reversed_num = reverse_number(number)
    print(f"Original number: {number}")
    print(f"Reversed number: {reversed_num}")

if __name__ == "__main__":
    main()