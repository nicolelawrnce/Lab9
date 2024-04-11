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
    if option == 1:
        password = input("Please enter your password to encode: ")
        encoded = ""
        for i in range(len(password)):
            encoded += str((int(password[i]) + 3)%10)
        print("Your password has been encoded and stored!")
        print()

    elif option == 2:
        decoded = ''
        for i in range(len(encoded)):
            decoded += str((int(encoded[i]) - 3)%10)
        print(f"The encoded password is {encoded}, and the original password is {decoded}.")
        print()

    elif option == 3:
        break
