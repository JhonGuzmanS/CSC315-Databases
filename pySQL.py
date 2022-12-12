import mysql.connector
import easygui as gui


def login(user, passwd=None, db=None):
    database = mysql.connector.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        database=db
    )
    return database


def getUser():
    user = input("Enter in your username: ")
    passwd = input("Enter your password(None): ")
    if passwd == "None":
        passwd = None
    return user, passwd


def print_cursor(mycursor):
    for x in mycursor:
        print(x)


def findStudent():
    choice = input("Are you finding by (I)D or (N)ame? ")
    if choice == 'I':
        id = input("Enter in the sid: ")
        try:
            mycursor = db.cursor()
            mycursor.execute("SELECT * FROM students where sid = %s" % id)
            print_cursor(mycursor)
        except:
            print("There is no student with that ID")
    elif choice == 'N':
        name = input("Enter in first then last name: ")
        name = name.split()
        try:
            mycursor = db.cursor()
            mycursor.execute("SELECT * FROM students where sfirst = '%s' and slast = '%s'" % (name[0], name[1]))
            print_cursor(mycursor)
        except:
            print("There is no student with that name")
    else:
        print("Enter in the correct choice.")
        findStudent()


def orderStudents():
    choice = input("Order by (N)ame? (Y)ear? or (I)D? ")
    order = input("(A)scending or (D)escending? ")
    if order == 'A':
        order = 'ASC'
    elif order == 'D':
        order = 'DESC'
    else:
        print("Not the correct input")
        orderStudents()

    if choice == 'N':
        choice = input("Order by (F)irst name or (L)ast name? ")
        if choice == 'F':
            try:
                mycursor = db.cursor()
                mycursor.execute("SELECT * FROM students order by sfirst %s" % order)
                print_cursor(mycursor)
            except:
                print("Error categorizing students by name")
        if choice == 'L':
            try:
                mycursor = db.cursor()
                mycursor.execute("SELECT * FROM students order by slast %s" % order)
                print_cursor(mycursor)
            except:
                print("Error categorizing students by name")
        else:
            print("Error, input not recognized. Restarting...")
    elif choice == 'Y':
        try:
            mycursor = db.cursor()
            mycursor.execute("SELECT * FROM students order by syear %s" % order)
            print_cursor(mycursor)
        except:
            print("Error categorizing students by year")
    elif choice == 'I':
        try:
            mycursor = db.cursor()
            mycursor.execute("SELECT * FROM students order by sid %s" % order)
            print_cursor(mycursor)
        except:
            print("Error categorizing students by id")
    else:
        print("Not the correct input")
        orderStudents()


def groupStudents():
    print("Available columns that you are able to group by: \n1.Year \n2.Grade")
    choice = input("Enter in the number(s) you wish to group by(leave a space in between options): ")
    choice = int(choice.split())

    options = [1, 2]
    isYear = False
    isGrade = False
    if len(choice) > 1:
        for num in choice:
            if num == 1:
                isYear = True
            elif num == 2:
                isGrade = True

        if isYear:
            year = input("Select all that apply: ")
            year = year.split()
            
    else:
        if choice == 1:
            isYear = True
        elif choice == 2:
            isGrade = True


def main():
    user, passwd = getUser()

    try:
        db = login(user, passwd, "studentinfo")
        mycursor = db.cursor()
        # mycursor.execute("SELECT * FROM students")
    except:
        print("There was an error, restart the program...")


# start of main
db = mysql.connector.connect()

#user, password = getUser()

#db = login("root", "Math@2468", "studentinfo")
db = login("John", db="studentinfo")
mycursor = db.cursor()
mycursor.execute("SELECT * FROM students")
for x in mycursor:
    print(x)

#orderStudents()
#findStudent()
#groupStudents()

# mycursor.execute("INSERT INTO table (variables) VALUES (%s, %s)", (actual values))
# mycursor.execute("SELECT * FROM table")
