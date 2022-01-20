# SOURCE CODE FOR BANK MANAGEMENT
import datetime
import mysql.connector

print("****BANK TRANSACTION****")
print("--Welcome to the Bank--")
print("========================")

# Connecting to MySQL
mydb = mysql.connector.connect(host="localhost",  user="root", passwd="root")
mycursor = mydb.cursor()

# CREATING DATABASE
mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")


# CREATING REQUIRED TABLES
mycursor.execute("create table if not exists bank_master(acno varchar(16) primary key,name varchar(20) not null,city char(20) not null,mobileno char(10) not null,balance int(10))")
mycursor.execute("create table if not exists banktrans(acno varchar (16) not null,amount int(10) not null,date date not null,_type char(10),foreign key (acno) references bank_master(acno))")
mydb.commit()


# MENU OPTIONS
while True:
    print("*___Option Menu___*")
    print("===================")
    print("1. Create account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Display account")
    print("5. Exit")
    ch = int(input("Enter your choice:"))

    # PROCEDURE FOR CREATING A NEW ACCOUNT OF THE APPLICANT
    if ch == 1:
        print("*All information prompted are mandatory to be filled")
        acno = str(input("Enter account number:"))
        name = input("Enter name(limit 20 characters):")
        city = str(input("Enter city name:"))
        mn = str(input("Enter mobile number:"))
        balance = 0
        mycursor.execute("insert into bank_master values('" + acno + "','" +
                         name + "','" + city + "','" + mn + "','" + str(balance) + "')")
        mydb.commit()
        print("!!!Account is successfully created!!!")

    # PROCEDURE FOR UPDATIONG DETAILS OF ACCOUNT AFTER THE DEPOSITION OF MONEY BY THE APPLICANT
    elif ch == 2:
        acno = str(input("Enter your account number:"))
        dp = int(input("Enter amount to be deposited:"))
        date = str(datetime.datetime.now())
        _type = "Credit"
        mycursor.execute("insert into banktrans values('" + acno +
                         "','" + str(dp) + "','" + date + "','" + _type + "')")
        mycursor.execute("update bank_master set balance=balance+'" +
                         str(dp) + "' where acno='" + acno + "'")
        mydb.commit()
        print("money has been deposited successully!!!")

    # PROCEDURE FOR UPDATING THE DETAILS OF ACCOUNT AFTER THE WITHDRAWL OF MONEY BY THE APPLICANT
    elif ch == 3:
        acno = str(input("Enter your account number:"))
        wd = int(input("Enter amount to be withdrawn:"))
        date = str(datetime.datetime.now())
        _type = "Debit"
        mycursor.execute("insert into banktrans values('" + acno +
                         "','" + str(wd) + "','" + date + "','" + _type + "')")
        mycursor.execute("update bank_master set balance=balance-'" +
                         str(wd) + "' where acno='" + acno + "'")
        mydb.commit()

    # PROCEDURE FOR DISPLAYING THE ACCOUNT OF THE ACCOUNT HOLDER AFTER HE/SHE ENTERS HIS/HER ACCOUNT NUMBER
    elif ch == 4:
        acno = str(input("Enter your account number:"))
        mycursor.execute("select * from bank_master where acno='" + acno + "'")
        for i in mycursor:
            print(i)

    # EXITING THE CODE
    elif ch == 5:
        print("*****Exiting*****")
        print("Thanks for using")
        break
    else:
        print("Wrong input")
