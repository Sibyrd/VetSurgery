import json

def test():
    x = {
        "db": [{
        }]
    }

    y = json.dumps(x)
    z = json.loads(y)

    z["db"].append({"name":"test"})

    print(z["db"])


choice = int(input("Welcome to Cats & Dogs Veterinary Surgery. Enter 1 to add a new animal, 2 to search, 3 to remove an animal and 4 to exit: "))
if choice == 1:

    with open("db.json", "r+") as f:
        parsed = json.loads(f.read())
        name = input("Enter the animal's name: ").lower()
        species = input("Enter the animal's species: ").lower()
        dob = input("Enter the animal's birthdate (dd.mm.yyyy): ").lower()
        owner = input("Enter the animal's owner: ").lower()
        parsed["db"].append({"name":name, "species":species, "dob":dob, "owner":owner})
        json = json.dumps(parsed)
        f.seek(0)
        f.write(json)
        f.close()
        print("Data has been written successfully.")
elif choice == 2:
    with open("db.json", "r") as f:
        parsed = json.loads(f.read())
        name = input("Enter the animal's name: ").lower()
        for i in parsed["db"]:
            if i["name"] == name:
                print("Animal under this name has been found!")
                print(i)
        f.close()
elif choice == 3:
    with open("db.json", "r+") as f:
        parsed = json.loads(f.read())
        name = input("Enter the animal's name: ").lower()
        for i in parsed["db"]:
            if i["name"] == name:
                parsed["db"].remove(i)
                print(parsed)
                json = json.dumps(parsed)
                print(json)
                f.seek(0)
                f.write(json)
                f.close()
                print("Data has been removed successfully.")
elif choice == 4:
    exit()