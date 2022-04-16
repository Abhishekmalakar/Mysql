#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
myd=mysql.connector.connect(
  host="localhost",user="root",password="abhi123",port=3300)
mycursor=myd.cursor()
print("Sab Thik Hai")


# In[2]:


mycursor.execute("show databases")
for x in mycursor:
    print(x)


# In[3]:


import mysql.connector
myd=mysql.connector.connect(
  host="localhost",user="root",password="abhi123",port=3300,database= "Indrustry")
mycursor=myd.cursor()

mycursor.execute("show tables")
for x in mycursor:
    print(x)


# In[4]:


import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Indrustry',
                                         user='root',
                                         password='abhi123',
                                         port= 3300)

    mySql_insert_query = """INSERT INTO Theamepark (Park_code, Park_name, Park_city,Park_country) 
                           VALUES (%s, %s, %s, %s) """

    records_to_insert = [(101, 'Bayer', 'Barvain', 'Germany'),
                         (102, 'TATA', 'Dheli', 'India'),
                         (103, 'jio', 'Mumbai', 'India')]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Theamepark table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))



# In[5]:


import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Indrustry',
                                         user='root',
                                         password='abhi123',
                                         port= 3300)

    mySql_insert_query = """INSERT INTO Theamepark (Park_code, Park_name, Park_city,Park_country) 
                           VALUES (%s, %s, %s, %s) """

    records_to_insert = [(104, 'Lefto', 'halvi', 'Zimbambe'),
                         (105, 'macticon inc', 'Hapara', 'UK'),
                         (106, "Telco Marbale", "Heli", "Zfri")]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Theamepark table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))


# In[6]:


import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Indrustry',
                                         user='root',
                                         password='abhi123',
                                         port= 3300)

    mySql_insert_query = """INSERT INTO Attraction (Attract_no, Park_code, Attract_name,Attract_age,Attract_capacity) 
                           VALUES (%s, %s, %s, %s,%s) """

    records_to_insert = [(1001, 101, 'Charu', 45,50000),
                         (1002, 102, 'Jamp', 34,56000),
                         (1003, 103,"Babu", 31, 90000),
                         (1004,104,"MiyaBhai",67,45000),
                          (1005,105,"haper",56,57000),
                          (1006,106,"Mapi",23,70000)]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Theamepark table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))


# In[7]:


import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Indrustry',
                                         user='root',
                                         password='abhi123',
                                         port= 3300)

    mySql_insert_query = """INSERT INTO Hours (Emp_num, Attract_no,Hours_per_attract,Hour_rate,Date_worked) 
                           VALUES (%s, %s, %s, %s, %s) """

    records_to_insert = [(1001, 1001, 2, 5,20210304),
                         (1002, 1002, 4, 4,20210305),
                         (1003, 1003, 3, 1, 20210306),
                         (1004, 1004, 6, 5,20210307),
                         (1005, 1005, 4,5,20210305),
                          (1006,1006, 3,3,20210304)]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Theamepark table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))


# In[8]:


import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Indrustry',
                                         user='root',
                                         password='abhi123',
                                         port= 3300)

    mySql_insert_query = """INSERT INTO Employee (Emp_num, Emp_title, Emp_Lname,Emp_Fname, Emp_dob,Emp_hire_date,Emp_arecode,Emp_phone,Park_code) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """

    records_to_insert = [(1001, "Sleschief", "Stark","Tom", 19850809,20200408,456575,985656565,1001),
                         (1002, "SalesManager", "mandlo","Jacsion",19870905, 20201204, 20214505, 98474748,1002),
                         (1003, "SalesMarketing", "julam","Khopta", 19750405,20201208, 3894848,984646464,1003),
                         (1004, "Dealer", "Misti","Jolly", 19920502,20210207,5658434,897656104,1004),
                         (1005, "Sales Head", "jafra","Arohi",19950601,20210305,738383,89878956,1005),
                          (1006,"SalerMan", "paki","Juli",19991203,20210306,647484,987765567,1006)]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Employee table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))


# In[9]:


import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Indrustry',
                                         user='root',
                                         password='abhi123',
                                         port= 3300)

    mySql_insert_query = """INSERT INTO Ticket (Ticket_no, Ticket_price,Ticket_Type,Park_code) 
                           VALUES (%s, %s, %s, %s) """

    records_to_insert = [(101, 340, "Local",101),
                         (102, 2000,  "Buisiness",102),
                         (103, 545,  "General", 103),
                         (104, 340, "Local", 104),
                         (105, 1340, "General",105),
                          (106,100, "Local",106)]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Ticket")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))


# In[10]:


import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Indrustry',
                                         user='root',
                                         password='abhi123',
                                         port= 3300)

    mySql_insert_query = """INSERT INTO Sales (Transaction_no, Park_code,Sales_date) 
                           VALUES (%s, %s, %s) """

    records_to_insert = [(1123,101,20210306),
                         (1124, 102,20210605),
                         (1125, 103, 20210506),
                         (1126, 104, 20210308),
                         (1127, 105, 20210605),
                          (1128,106, 20210304)]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Sales")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))


# In[11]:


import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='abhi123', host='localhost', database='Indrustry',port=3300)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing the query to update the records
sql = '''UPDATE Employee SET Emp_Fname = "Alam" WHERE Emp_num = 1005 '''
try:
   # Execute the SQL command
   cursor.execute(sql)
   
   # Commit your changes in the database
   conn.commit()
except:
   # Rollback in case there is any error
   conn.rollback()
   


# In[12]:


import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Indrustry',
                                         user='root',
                                         password='abhi123',
                                         port= 3300)

    mySql_insert_query = """INSERT INTO Sales_line (Transaction_no, Line_no,Ticket_no,Line_qty,Line_price) 
                           VALUES (%s, %s, %s, %s, %s) """

    records_to_insert = [(1123,51,101,"good",10000),
                         (1124, 52,102,"Bad",2000),
                         (1125, 53,103, "Bad",1000),
                         (1126,54, 104,"Mediam", 50000),
                         (1127,55, 105,"Good", 70000),
                          (1128,66,106, "Good",80000)]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Sales_line")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))


# In[13]:


#Join Two tables

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "abhi123",
    database = "Indrustry",
    port=3300
)

cursor = db.cursor()

sql = "SELECT Theamepark.Park_code, Theamepark.Park_name,Theamepark.Park_city,Theamepark.Park_country, Attraction.Attract_no,Attraction.Attract_name,Attraction.Attract_age,Attraction.Attract_capacity from Theamepark INNER JOIN Attraction ON Theamepark.Park_code=Attraction.Park_code;"
("")
cursor.execute(sql)

myresult = cursor.fetchall()

for x in myresult:
    print(x)


# In[14]:


#join Two tables 

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "abhi123",
    database = "Indrustry",
    port=3300
)

cursor = db.cursor()

sql = "SELECT Attraction.Attract,Hours.Emp_num,Hours.Hours_per_Attract,Hours.Hour_rate,Hours.Date_worked from Attraction INNER JOIN Hours ON Attraction.Attract_no=Hours.Attract_no ;"


cursor.execute(sql)

myresult = cursor.fetchall()

for x in myresult:
    print(x)


# In[ ]:


#join four tables
import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "abhi123",
    database = "Indrustry",
    port=3300
)

cursor = db.cursor()

sql = "SELECT Theamepark.Park_code,Theamepark.Park_name,Theamepark.Park_city,Theamepark.Park_country,Employee.Emp_num,Employee.Emp_title,Employee.Emp_Lname,Employee.Emp_Fname,Employee.Emp_phone,Hours.Hours_per_Attract,Hours.Hour_rate,Hours.Date_worked, Attraction.Attract_no,Attraction.Attract_name,Attraction.Attract_age,Attraction.Attract_capacity from Theamepark INNER JOIN Attraction ON Attraction.Park_code=Theamepark.Park_code INNER JOIN Hours ON Hours.Attract_no=Attraction.Attract_No INNER JOIN Employee ON Employee.Emp_num=Hours.Emp_num;"

cursor.execute(sql)

myresult = cursor.fetchall()

for x in myresult:
    print(x)


# In[ ]:


# Join All Tables

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "abhi123",
    database = "Indrustry",
    port=3300
)

cursor = db.cursor()

sql = "SELECT Theamepark.Park_code,Theamepark.Park_name,Theamepark.Park_city,Theamepark.Park_country,Employee.Emp_num,Employee.Emp_title,Employee.Emp_Lname,Employee.Emp_Fname,Employee.Emp_phone,Hours.Hours_per_Attract,Hours.Hour_rate,Hours.Date_worked, Attraction.Attract_no,Attraction.Attract_name,Attraction.Attract_age,Attraction.Attract_capacity,Sales.Transaction_no,Sales.Sales_date,Ticket.Ticket_no,Ticket.Ticket_price,Ticket.Ticket_type,Sales_line.Line_no,Sales_line.Line_qty,Sales_line.Line_price from Theamepark INNER JOIN Attraction ON Attraction.Park_code=Theamepark.Park_code INNER JOIN Hours ON Hours.Attract_no=Attraction.Attract_no INNER JOIN Employee ON Employee.Emp_num=Hours.Emp_num INNER JOIN Sales ON Sales.Park_code=Theamepark.Park_code INNER JOIN Ticket ON Ticket.Park_code=Theamepark.park_code INNER JOIN Sales_line ON Sales_line.Transaction_no=Sales.Transaction_no;"

cursor.execute(sql)

myresult = cursor.fetchall()

for x in myresult:
    print(x)


# In[ ]:


import mysql.connector as sql
import pandas as pd

db_connection = sql.connect(host='localhost', database='Indrustry', user='root', password='abhi123',port=3300)
db_cursor = db_connection.cursor()
db_cursor.execute("SELECT Theamepark.Park_code,Theamepark.Park_name,Theamepark.Park_city,Theamepark.Park_country,Employee.Emp_num,Employee.Emp_title,Employee.Emp_Lname,Employee.Emp_Fname,Employee.Emp_phone,Hours.Hours_per_Attract,Hours.Hour_rate,Hours.Date_worked, Attraction.Attract_no,Attraction.Attract_name,Attraction.Attract_age,Attraction.Attract_capacity,Sales.Transaction_no,Sales.Sales_date,Ticket.Ticket_no,Ticket.Ticket_price,Ticket.Ticket_type,Sales_line.Line_no,Sales_line.Line_qty,Sales_line.Line_price from Theamepark INNER JOIN Attraction ON Attraction.Park_code=Theamepark.Park_code INNER JOIN Hours ON Hours.Attract_no=Attraction.Attract_no INNER JOIN Employee ON Employee.Emp_num=Hours.Emp_num INNER JOIN Sales ON Sales.Park_code=Theamepark.Park_code INNER JOIN Ticket ON Ticket.Park_code=Theamepark.park_code INNER JOIN Sales_line ON Sales_line.Transaction_no=Sales.Transaction_no;"
)

table_rows = db_cursor.fetchall()

df = pd.DataFrame(table_rows)


# In[ ]:


df


# In[ ]:


sd=df.to_csv("result.csv")


# In[ ]:


sd


# In[ ]:




