import mysql.connector
from mysql.connector import Error
import configparser

config=configparser.ConfigParser()
config.read(r'C:\Users\Sourav\Documents\python\Data\simple.ini')
db={}
for item in config.items('DB1'):
    db[item[0]]=item[1]


try:
    conn=mysql.connector.MySQLConnection(**db)
    cur=conn.cursor()
    cur.execute("select * from employees")
    x=cur.fetchone()
    while x is not None:
        print(x)
        x=cur.fetchone()

except Error as e:
    print(e)

finally:
    cur.close()
    conn.close()
