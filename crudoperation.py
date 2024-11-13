import mysql.connector
# Replace these with your actual database credentials
def insertstudent(a,b,c,d,e,f):
    config = {'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'database': 'website'
    }
    # Establish the connection
    cnx = mysql.connector.connect(**config)
    # Create a cursor object
    cursor = cnx.cursor()
    sql = f"insert into studentweb values({a},'{b}',{c},'{d}','{e}','{f}')"
    print(sql)
    cursor.execute(sql)
    cnx.commit()
    cursor.close()
#insertstudent(2,'sureshK','6379991294','vandalur,chennai','2003-06-24','2023-07-03')
def readsinglestudent(a):
    config = {'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'database': 'website'
    }
    # Establish the connection
    cnx = mysql.connector.connect(**config)
    # Create a cursor object
    cursor = cnx.cursor()
    sql = f"select *from studentweb where id={a}"
    cursor.execute(sql)
    #for a in cursor.fetchall():
     #   print(a)
    a=cursor.fetchall()
    return a
#readsinglestudent(1)
def readallstudent():
    config = {'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'database': 'website'
    }
    # Establish the connection
    cnx = mysql.connector.connect(**config)
    # Create a cursor object
    cursor = cnx.cursor()
    sql = f"select * from studentweb"
    cursor.execute(sql)
    a=cursor.fetchall()
    return a
#readallstudent()
def deletestudent(a):
    config = {'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'database': 'website'
    }
    # Establish the connection
    cnx = mysql.connector.connect(**config)
    # Create a cursor object
    cursor = cnx.cursor()
    sql = f"delete from studentweb where id={a}"
    cursor.execute(sql)
    cnx.commit()
    return "successfully deleted"
    # for a in cursor.fetchall():    #     print(a)
#deletestudent(2)

def updatestudent(a,b,c,d,e,f):
    config = {'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'database': 'website'
    }
    # Establish the connection
    cnx = mysql.connector.connect(**config)
    # Create a cursor object
    cursor = cnx.cursor()
    sql = f"update studentweb set name='{b}',phone='{c}',address='{d}',dob='{e}',doj='{f}' where id={a}"
    print(sql)
    cursor.execute(sql)
    cnx.commit()
    cursor.close()
    return "student updated successfully"