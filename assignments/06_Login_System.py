# Login System (Mini)
users ={
    "charlie@23":"mnbvcxz123", "emily@23":"potato12"
}

user_input = input("Enter the Username: ")
user_pass = input("Enter the password: ")

if user_input in users and users[user_input] == user_pass:
    print("Asscess granted")
else:
    print("Access denied, Wrong username or password.")