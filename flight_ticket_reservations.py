total_tickets = 100
ticket_price = 2500
booked_tickets = 0
passengers = {}
cashier_id = 4862
cashier_password = 987
def guna():
    print("1.sign up")
    print("2.login")
    print("3.Go back")
    a=int(input("Enter your choice:"))
    if a==1:
        passenger()
    if a==2:
        login()
    if a==3:
        natraj()
    else:
        print("!!!!!!!-Invalid choice-!!!!!!!")
        guna()
def passenger():
    print("Enter your name: ")
    name = input()
    print("Enter your age: ")
    age = int(input())
    if age > 18:
        print("Enter your password: ")
        password = int(input())
        print("Enter your gender: ")
        gender = input()
        if gender not in ("male", "female", "others"):
            print("!!!!!!!-Invalid-!!!!!!!")
            return
        username = name[0] + gender[0]
        passengers[username] = {
            'name': name,
            'age': age,
            'gender': gender,
            'password': password,
            'tickets': 0,
            'status': "No ticket booked"
        }
        print(passengers)
        print("*********Signup successfully*********")
        print("Your username is:", username)
        print("Your password is:", password)
        print("-------------------------------")
        guna()
    else:
        print("!!!!!!!-Not eligible-!!!!!!!")
def login():
    username = input("Enter your username: ")
    password = int(input("Enter your password: "))
    if username in passengers and passengers[username]['password'] == password:
        print("*********Login successfully*********")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        details(username)
    else:
        print("!!!!!!!-Wrong username or password-!!!!!!!")
        guna()
def details(username):
    global booked_tickets
    while True:
        print("1. Check availability and fare")
        print("2. Book ticket")
        print("3. Check booking status")
        print("4. Go back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Total tickets:", total_tickets)
            print("Booked tickets:", booked_tickets)
            print("Available tickets:", total_tickets - booked_tickets)
            print("Ticket price:", ticket_price)
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        elif choice == 2:
            tickets = int(input("Enter number of tickets: "))
            if tickets < total_tickets - booked_tickets:
                booked_tickets += tickets
                passengers[username]['tickets'] = tickets
                passengers[username]['status'] = "Waiting list"
                print("*********Ticket booked successfully*********")
            else:
                print("!!!!!!-Insufficient tickets available-!!!!!!")
        elif choice == 3:
            print("Booking status:", passengers[username]['status'])
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        elif choice == 4:
            guna()
        else:
            print("Invalid choice")
            details()
def cashier():
    cashier_id_input = int(input("Enter cashier ID: "))
    password = int(input("Enter password: "))
    if cashier_id_input == cashier_id and password == cashier_password:
        print("******Login successful*********")
        print("----------------------------------")
        puvi()
    else:
        print("!!!!!!-Wrong username or password-!!!!!!-")
        cashier()
def approve():
    print(passengers)
    username = input("Enter passenger username: ")
    if username in passengers:
        if passengers[username]['status']=="Waiting list":
            passengers[username]['status'] = "Approved"
            print("*-*-*-*-*-*-Ticket approved*-*-*-*-*-*-")
            puvi()
        else:
            print("No tickets booked for approval or Tickets already approved")
            puvi()
    else:
        print("!!!!!!-Passenger not found-!!!!!!")
        puvi()
def cancel():
    global  booked_tickets
    print(passengers)
    username = input("Enter passenger username: ")
    if username in passengers:
        if passengers[username]['status']=="Approved" or passengers[username]['status']=="Waiting list":
            booked_tickets-=passengers[username]['tickets']
            passengers[username]['status'] = "Cancelled"
            print("!!!!!!-Ticket cancelld-!!!!!!")
            puvi()
        else:
            print("Tickets already cancelled")
            puvi()
    else:
        print("!-!-!-!-Passenger not found-!-!-!-!")
        puvi()
def report():
    print("*******Report View*********")
    print("Total tickets:", total_tickets)
    print("Booked tickets:", booked_tickets)
    print("Available tickets:", total_tickets - booked_tickets)
    print("Ticket price:", ticket_price)
    print(passengers)
    print("--------------------------------")
    puvi()
def puvi():
    while True:
        print("1. Approve ticket")
        print("2. Cancel ticket")
        print("3. View report")
        print("4. Logout")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            approve()
        if choice==2:
            cancel()
        if choice==3:
            report()
        if choice == 4:
            natraj()
        else:
            print("Invalid choice")
            puvi()
def natraj():
    while True:
        print("-*-*-*-*-*-*-*-*-*-*-*-WELCOME GUNASEKAR FLIGHT RESERVATION SYSTEM-*-*-*-*-*-*-*-*-*-*-*-")
        print("1. Passenger")
        print("2. Cashier")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            guna()
        if choice == 2:
            cashier()
        if choice == 3:
            print("THANK YOU")
            natraj()
        else:
            print("Invalid choice")
            natraj()
natraj()

