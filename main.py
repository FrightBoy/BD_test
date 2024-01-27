# import SQL
import sqlite3
# connect to Database \ Create one
connect = sqlite3.connect("my_users.db")
# create new executer for SQL
sql = connect.cursor()
# giving commands to Database
# sql.execute("CREATE TABLE IF NOT EXISTS my_cars(model TEXT, name TEXT, year INTEGER);")
# sql.execute("CREATE TABLE IF NOT EXISTS cars_1(nevermore TEXT, shadowfiend TEXT, lvl INTEGER);")
sql.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER, username TEXT);")
sql.execute("INSERT INTO users(user_id) VALUES (1151);")
sql.execute("INSERT INTO users(user_id, username) VALUES (1151, 'nigger John');")
connect.commit()
SQL_USERS = sql.execute("SELECT user_id FROM users;").fetchall()
SQL_Name = sql.execute("SELECT * FROM users WHERE user_id = 1;").fetchone()

connect.commit()
# def Deleting():
#    sql.execute('DELETE FROM users Where user_id = 1151')
# Deleting()
connect.commit()
#connect.close()
# execute("CREATE TABLE cars_1 (nevermore TEXT, shadowfiend TEXT, lvl INTEGER);")
sql.execute("UPDATE my_cars SET year = 2011 WHERE model ='tesla';")
connect.commit()
sql.execute('UPDATE users SET user_id = "1" WHERE username = "nigger_John" ;')
connect.commit()
print(SQL_Name)