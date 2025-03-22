phonebook = {  
    'Jim': ('209 Trafalgar Road', '905-666-7676'),  
    'Shawn': ('1439 Falgore Road', '487-423-7225'),
    'Patrick': ('123 Banana St', '416-535-1234'),
    'David': ('678 Oakville Ave', '915-555-6419')
}


with open('SpeedDial.txt', 'w') as file:
   
    for details in phonebook.values():
        phone_number = details[1]
        file.write(phone_number + '\n')

print("The Phone book has been updated")
