import mysql.connector
import easygui as gui
import pandas as pd


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
    index = ['ID', 'First', 'Last', 'Year', 'Address', 'Grade']
    df = pd.DataFrame(columns=index)

    for x in mycursor:
        df.loc[len(df)] = x
    gui.msgbox(df)

# Finds an individual student by searching based on his name or student ID
def findStudent():
    title = "Find Student"
    selectid = "SELECT * FROM students where sid = %s"
    selectname = "SELECT * FROM students where sfirst = '%s' and slast = '%s'"
    test = "select * from students where sfirst = 'Joe'"
    choice = gui.choicebox("Choose how to find Student:", title, choices=["ID", "Name"])
    if choice == "ID":
        id = gui.enterbox("Enter in the ID of the student", title)
        try:
            mycursor.execute(selectid, id)
            print_cursor(mycursor)
        except:
            output = gui.msgbox("Invalid information.", title, "Continue")
            findStudent()
    elif choice == "Name":
        name = gui.multenterbox("Enter in the correct information", title, fields=("First", "Last"))
        value = name
        try:
            mycursor.execute(selectname, value)
            print_cursor(mycursor)
        except:
            output = gui.msgbox("Invalid information.", title, "Continue")
            findStudent()

# Shows all students in a specific order(by name or year or ID number)
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

# shows students that meet the requirement of the users. Whether they're a Freshman, Junior, or if they have a certain grade
def groupStudents():
    title = "Group Students"
    select = "select * from students where sgrade between %s and %s and ("
    grouplist = ("Year", "Grade")
    choices = gui.multchoicebox("Choose all that apply:", title, choices=grouplist)
    if len(choices) == len(grouplist):
        year = gui.multchoicebox("Choose all that apply:", "Group Students", choices=('FRES', 'SOPH', 'JUN', 'SEN'))
        grade = gui.enterbox("Enter in a range for Grade. Ex: 0,100", title)
        grade = grade.split(',')
        num = len(year)
        if num != 0:
            for i in range(num - 1):
                select = select + "syear = %s or "
        select = select + "syear = %s) "
        values = grade + year
        try:
            mycursor.execute(select, values)
            print_cursor(mycursor)
        except:
            output = gui.msgbox("Invalid information.", title, "Continue")
            groupStudents()

# adds a new Student into the database
def insertStudent():
    insert = "INSERT INTO students (sfirst, slast, syear, saddress, sgrade) VALUES (%s, %s, %s, %s, %s)"
    msg = "Enter in Student Info"
    title = "Student Information"
    fieldName = ["First Name", "Last Name", "Year", "Address", "Current Grade"]
    info = gui.multenterbox(msg, title, fieldName)
    print(info)
    if info[0] == "" or info[1] == "" or info[2] == "" or info[4] == "":
        output = gui.msgbox("Information missing.", title, "Continue")
        insertStudent()
    else:
        try:
            mycursor.execute(insert, info)
            db.commit()
        except:
            output = gui.msgbox("Invalid information.", title, "Continue")
            insertStudent()


def main():
    user, passwd = getUser()

    try:
        db = login(user, passwd, "studentinfo")
        mycursor = db.cursor()
        # mycursor.execute("SELECT * FROM students")
    except:
        print("There was an error, closing the program...")


# start of main
db = mysql.connector.connect()

# user, password = getUser()
# db = login("root", "Math@2468", "studentinfo")

db = login("root", "Math@2468", db="studentinfo")
mycursor = db.cursor()
mycursor.execute("SELECT * FROM students")
print_cursor(mycursor)

# orderStudents()
findStudent()
# groupStudents()
#insertStudent()
db.close()
