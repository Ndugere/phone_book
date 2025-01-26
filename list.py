temp = []

with open("phonebook.txt", "r") as file:
    for row in file:
        row = row.split(",")
        temp.append(row)
        print(f"Name: {row[0].rstrip().strip()}, Number: {row[1].rstrip().strip()}")
print(temp)

def get_name(person):
    print(person[1])
    return person[1].rstrip()


for person in sorted(temp, key=get_name):
    print(f"Name: {person[0]}, Number: {person[1].rstrip()}")
