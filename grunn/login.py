import sqlite3, time

def login():
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        with sqlite3.connect("quiz.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(username),(password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("Welcome "+i[2])
            #return("exit")
            break

        else:
            print("Username and password not recognised")
            again = input("Do you want to try again? (y/n): ")
            if again.lower() == "n":
                print("Goodbye")
                time.sleep(1)
                #return("exit")
                break

def newuser():
    found = 0
    while found == 0:
        username = input("Please enter a username: ")
        with sqlite3.connect("quic.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM user WHERE username = ?")
        cursor.execute(findUser,[(username)])

        if cursor.fetchall():
            print("Username Taken, please try again.")
        else:
            found = 1

    firstName = input("Enter your first name: ")
    surName = input("Enter your surname: ")
    password = input("Please Enter your password: ")
    password1 = input("Please reEnter your password: ")
    while password != password1:
        print("Your passwords didn´t match, please try again.")
        password = input("Please Enter your password: ")
        password1 = input("Please reEnter your password: ")
    insertData = '''INSERT INTO user(username,firstname,surname,password)
    VALUES(?,?,?,?)
    cursor.execute(executional)
    '''
    cursor.execute(insertData,[(username),(firstName),(surName),(password)])
    db.commit()



def menu():
        while True:
            print("Welcome to my system ")
            menu = ('''
            1 - create new layout
            2 - login to system
            3 - exit system\n''')

            userchoice = input(menu)

            if userchoice == "1":
                newuser()

            elif userchoice == "2":
                login()

            elif userchoice == "3":
                print("goodbye")
                exit()

            else:
                print("Command not recognized: ")

menu()




