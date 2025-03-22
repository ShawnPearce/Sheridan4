import json
phonebook = {  
    'Jim': ('209 Trafalgar Road', '905-666-7676'),  
    'Shawn': ('1439 Falgore Road', '487-423-7225'),
    'Patrick': ('123 Banana St', '416-535-1234'),
    'David': ('678 Oakville Ave', '915-555-6419')
}


with open('Speeddial.json', 'w') as json_file:
    json.dump(phonebook, json_file, indent=4)

print("Phonebook has been written to Speeddial.json.")

with open('Speeddial.json', 'r') as json_file:
    updatedPhonebook = json.load(json_file)

    print("Output:")
    for name, details in updatedPhonebook.items():
        address, phone_number = details #unpacks Tuples
        print(f"{name}:\n  Address: {address}\n  Phone Number: {phone_number}\n")
