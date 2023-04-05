#!/usr/bin/env python
import psycopg2
from projects_menu import projectmenu

def signin():
    name=input("please enter your name: ")
    password=input("please enter your password: ") 

    conn_params={
        "dbname" : "iti",
        "user" : "postgres",
        "password" : "iti",
        "host" : "localhost",
        "port" : 5432
        }
    con=psycopg2.connect(**conn_params)
    cursor=con.cursor()
    sql=f"SELECT * FROM new_users WHERE fname = '{name}' AND password = '{password}'"
    cursor.execute(sql)
    found = cursor.fetchone()
    if found:
        print(f"WELCOME BACK {name} \U0001F600")
        projectmenu()
    else :
        print("you are not a member, please sign up!")
        print("-------------------------------------")
        
        
        
        
    con.commit()
    cursor.close()
    con.close()    