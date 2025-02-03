def search_number(number):
    with open("phonebook.txt", "r") as file:
        found = False
        for line in file:
            line = line.split(",")
            if len(line[1]) > 1 and line[1].rstrip().strip() == number:
                print(f"{line[0].strip()}: {line[1].rstrip()}")
                found = True
            else:
                continue
        if not found:
            print("No such number")


def search_name(name):
    with open("phonebook.txt", "r") as file:
        found = False
        for line in file:
            line = line.split(",")
            if len(line[0]) > 0 and line[0].strip().upper() == name.strip().upper():
                print(f"{line[0].strip()}: {line[1].rstrip()}")
                found = True
            else:
                continue
        if not found:
            print("No such name!")


def main():
    x = input("Input what you want to search: ")
    if x.lstrip("+").isdigit():
        search_number(x)
    else:
        search_name(x)
        
        
if __name__ == "__main__":
    main()
    