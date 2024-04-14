import mysql.connector

sql = mysql.connector

connection =  sql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'first_database'
)

my_cursor = connection.cursor()


# CREATE DATABASE 
# query1 = '''CREATE DATABASE FIRST_DATABASE'''
# my_cursor.execute(query1)


# DATABASE EXIST OR NOT
# query2 = '''SHOW DATABASES'''
# my_cursor.execute(query2)
# ava_db = my_cursor.fetchall()
# for x in ava_db:
#     print(x)

# CREATE TABLE
# query3 = '''CREATE TABLE user_data(
#   PHN INT NOT NULL,
#   PWD VARCHAR(45) NOT NULL,
#   PRIMARY KEY (PHN));'''
# my_cursor.execute(query3)

# INSERT DATA IN TABLE
# query4 = '''INSERT INTO USER_DATA(PHN,PWD) VALUES(%s,%s)'''
# val = (12345,"abc@123")
# my_cursor.execute(query4,val)
# connection.commit()

# READ 
# query5 = '''SELECT * FROM USER_DATA'''
# my_cursor.execute(query5)
# data = my_cursor.fetchall()
# print(data)

# UPDATE
# query6 = '''UPDATE USER_DATA SET PWD='bca@123' WHERE PHN=12345'''
# my_cursor.execute(query6)
# connection.commit()

#DELETE
# query7 = '''DELETE FROM USER_DATA WHERE PHN=1234'''
# my_cursor.execute(query7)
# connection.commit()

print(connection)