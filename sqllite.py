import sqlite3

##connect to SQlite database

connection= sqlite3.connect('student.db')

## Create a cursor object to insert record, create table

cursor= connection.cursor()

## Create a table

table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);"""

cursor.execute(table_info)

##Insert Some more records

cursor.execute(''' Insert into STUDENT values('Devang', 'Data Science', 'A', 85);''')
cursor.execute(''' Insert into STUDENT values('Pratham', 'Data Science', 'B', 90);''')
cursor.execute(''' Insert into STUDENT values('Yash', 'Data Science', 'A', 78);''')
cursor.execute(''' Insert into STUDENT values('Neel', 'Generative AI', 'A', 92);''')
cursor.execute(''' Insert into STUDENT values('Drashti', 'Generative AI', 'A', 88);''')

##Display all the records

print("The inserted records are: ")
data= cursor.execute(''' Select * from STUDENT;''')
for row in data:
    print(row)

## Commit your changes into the database

connection.commit()
connection.close()

