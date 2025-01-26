temp = []

with open("phonebook.txt", "r") as file:
    for row in file:
        temp.append(row.strip())

name_to_delete = input("Enter the name of the person to delete: ")
updated_temp = [row for row in temp if not row.startswith(name_to_delete + ",")]

if len(updated_temp) < len(temp):
    with open("phonebook.txt", "w") as file:
        for row in updated_temp:
            file.write(row + "\n")
    print(f"{name_to_delete} has been deleted.")
else:
    print("Person not found.")