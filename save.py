while True:
    name = input("Enter Name: ").strip()
    if not name:
        print("You have not entered a name, Try again \n")
    else:
        break
 
    
while True:
    number = input("Enter Number: ").strip()
    if not number:
        print("You have not entered a number, Try again \n")
        continue
    elif not number.isdigit():
        print("You have not entered a valid number, number must contain only digit numbers \n ")
        continue
    elif len(number) != 10:
        print("Number must be exactly ten digits! \n")
        continue
    else:
        break


with open("phonebook.txt", "a") as file:
    file.write(f"{name}, {number}\n")

print()
print("Number saved sucessfully!")