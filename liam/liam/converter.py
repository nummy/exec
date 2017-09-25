# File: converter.py
# Author:
# Saibt Id:
# Description:


MENU = """

*** Menu ***
1. Convert to binary
2. Convert to decimal
3. Binary counting
4. Quit
"""

print(MENU)
choice = input("What would you like to do [1,2,3,4]?")  # choice
while choice != "4":
    if choice == "1":
        # handle binary convert
        decimal = input("\nPlease enter number:") # decimal number
        while not decimal.isdigit():
            print("Please make sure your number contains digits 0-9 only.")
            decimal = input("\nPlease enter number:")
        decimal = int(decimal) # parse string to int
        binary = ""
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal = decimal // 2
        print("\nBinary number:", binary)
    elif choice == "2":
        binary = input("\nPlease enter binary number:") # binary string
        while not binary.isdigit() or (binary.count("0") + binary.count("1") != len(binary)):
            print("Please make sure your number contains digits 0-1 only.")
            binary = input("\nPlease enter binary number:")
        length = len(binary) # length of binary
        decimal = 0  # decimal number
        for i in range(length-1, -1, -1):
            decimal += (int(binary[i]))*pow(2,length-i-1)
        print("\nDecimal number:", decimal)
    elif choice == "3":
        decimal = input("\nPlease enter number:") # decimal number
        while not decimal.isdigit():
            print("Please make sure your number contains digits 0-9 only.")
            decimal = input("\nPlease enter number:")
        decimal = int(decimal)  # parse string to int
        print()
        for num in range(1, decimal+1):
            binary = ""
            temp = num  # store temp num for print
            while num > 0:
                binary = str(num % 2) + binary
                num = num // 2
            print("Decimal: ", temp, " = binary: ", binary)
    else:
        print("Invalid choice, please enter either 1, 2, 3 or 4.")
    print(MENU)
    choice = input("\nWhat would you like to do [1,2,3,4]?")
print("\nGoodbye")
