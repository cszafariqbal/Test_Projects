print("Register  account  ")
first_name = input("First name : ")
last_name = input("last name :")
cnic = int(input("CNIC : "))
Password = int(input("Password :"))
def account_login():
    print("Login Account :")
    CNIC = int(input("CNIC :"))
    while 1:
        if CNIC == cnic:
            break
        else:
            print("wrong CNIC, again try")
            CNIC = int(input("CNIC :"))

    password = int(input("Password :"))
    while 1:
        if password == Password:
            break
        else:
            print("wrong password, agian try")
            password = int(input("Password :"))
account_login()
current_balance = 100000
def option():
    global current_balance
    print("send money Enter 1 ")
    print("Recieved money Enter 2 ")
    print("check balance Enter 3 ")
    print("logout System Enter 4 ")
    x = int(input("Select any option : " ))
    if x==1:
        send_money = int(input("Send Money :"))
        account_number = input("Accout Number :")
        current_balance = current_balance - send_money
        print("You have sent money", send_money, " to ", account_number)
        print("your remaining current balance is :", current_balance)

    elif x == 2:
        recieved_money = int(input("Recived Money :"))
        recieved_account = input("Accout number :")
        current_balance = current_balance + recieved_money
        print("you recived ", recieved_money, "money from", recieved_account, "Account")
        print("Your Current balance is : ", current_balance)
    elif x == 3:
        print("current balance  :", current_balance)
    else:
        print("1 for login Account :")
        print("2 for Exit :")
        y = int(input(": "))
        if y == 1:
            account_login()
            option()
        else:
            pass
option()