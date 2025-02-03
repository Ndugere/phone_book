def main():
    while True:
        info = input('Type "Name" to search by Name or "Number" to search by Number\n')
        info = info.upper().strip()

        if not info:
            print("You have not entered a choice, try again! \n")
            continue
        elif info == "NAME":
            name = input("Please enter the name you want to update: ").strip()
            get_name(name)
            break
        elif info == "NUMBER":
            number = input("Please enter the number you want to update: ").strip()
            get_number(number)
            break
        else:
            print("You have not entered a valid choice \n")

def get_name(name):
    
    temp = []
    found = False

    with open("phonebook.txt", "r") as file:
        for line in file:
            if line.strip():
                line = line.strip().split(",") 
                if line[0].strip().upper() == name.upper():
                    new_name = input("Enter the New Name: ").strip()
                    line[0] = new_name
                    found = True
                temp.append(line)

    if not found:
        print("No such name found\n")
    else:
        save(temp)
        print(f"{name} updated to {new_name} successfully")


def get_number(number):
    
    found = False
    temp = []

    with open("phonebook.txt", "r") as file:
        for line in file:
            if not line.strip():
                continue
            line = line.strip().split(",") 
            if line[1].strip() == number.strip():
                new_number = input("Enter the new number: ").strip()
                line[1] = new_number
                found = True
            temp.append(line)

    if not found:
        print("No such number in the phonebook")
    else:
        save(temp)
        print(f"The Number {number} updated to {new_number} successfully")


def save(temp):
    with open("phonebook.txt", "w") as file:
        for line in temp:
            file.write(f"{line[0]},{line[1]}\n")


if __name__ == "__main__":
    main()
