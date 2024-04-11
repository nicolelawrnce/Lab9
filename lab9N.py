# nicole
def menu():
    print("Menu")
    print("-------------")
    print("""1. Encode
2. Decode
3. Quit""")


option = 0
while option != -1:
    menu()
    option = int(input("Please enter an option: "))
    password = input("Please enter your password to encode: ")
    if option == 1:
        encoded = ""
        for i in range(len(password)):
            encoded += str((int(password[i]) + 1))
        print("Your password has been encoded and stored!")
        print()

    elif option == 2:
        continue

    elif option == 3:
        break
