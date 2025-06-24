contacts = {}

while True:
    print("\nContact Book App")
    print("1 . Create account")
    print("2 . View Contact")
    print("3 . Update Contact")
    print("4 . Delete Contact")
    print("5 . Search Contact")
    print("6 . Count Contact")
    print("7 . Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        try:
            name = input("Enter The Name: ")
            if name in contacts:
                print(f"Contact name {name} already exist! ")
            else:
                age = int(input("Enter Your Age = "))
                email = input("Enter email = ")
                mobile = int(input("Enter mobile number = "))
                contacts[name] = {'age':age, 'email':email, 'mobile':mobile}
                print(f"Contact name {name} registerd succesfully")
        except Exception as e:
            print(e)

        
    elif choice == 2:
        name = input("Enter The Contact Name to View = ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {age}, Mobile Number: {mobile}")
        else:
            print('Contact Not Found!')
            

    elif choice == 3:
        name = input('Enter name to update contact')
        if name in contacts:
            age = int(input('Enter updated age = '))
            email = input('Enter updated email = ')
            mobile = int(input("Enter updated Mobile Number"))
            contact[name] = {'age':age, 'email':email, 'mobile':mobile}

        else:
            print('Contact Not Found')

    elif choice==4:
        name  = input('Enter The Name of contact you want to delete = ')
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} has been deleted succesfully')
        else:
            print('Contact not found!')

    elif choice==5:
        name = input('Enter contact name to search')
        if name in contacts:
            print(f'Found - Name {name}, Age:{age}, Mobile Numberl: {mobile}, Email: {email}')
            found = True

        if not found:
            print('No contact with that name')

    elif choice==6:
        name = input(f'Total contact in your book : {len(contacts)}')

    elif choice == 7:
        print('Good bye..... Closing the Book')
        break
    
    else:
        print('Invalid input')


