name = input("Enter name: ")
number = input("Enter Number: ")


with open("phonebook.txt", "a") as file:
    file.write(f"{name}, {number}")
    file.close
