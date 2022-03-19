users = {
    "id" : 1,
    "name" : "Leanne Graham",
    "username" : "Bret",
    "email" : "Sincere@april.biz",
    "addres" : {
        "street": "kulas night",
        "suite" : "Apt .567",
        "city" : "GwenBorough",
        "zipcode" : "92998-3874",
        "geo" : {
            "lat" : "-37.3159",
            "lng" : "81.1496"
        }
    }
}

print(users)
print(users["addres"]["geo"])

print("\nUbah dictionary ke JSon")
import json
result = json.dumps(users)
print(result)

with open('result.json', 'w') as file:
    json.dump(users, file)