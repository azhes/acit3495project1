from asyncore import write
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import yaml
import mysql.connector

def write_to_mysql(path):

    db = mysql.connector.connect(
        host="localhost",
        user="videouser",
        password="Password",
        database="project1",
        port=3600
    )

    mycursor = db.cursor()

    sql = "INSERT INTO videos (path) VALUES (%s)"

    val = [path]
    mycursor.execute(sql, val)

    db.commit()

    print(mycursor.rowcount, "record inserted")

