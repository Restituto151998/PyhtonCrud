import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python"
)

def showData(conn):
    print("Showing")
    cursor = conn.cursor();
    sql = "SELECT * FROM tasks"        
    cursor.execute(sql)
    for x in cursor:
        print(x)
       

def insertData(conn):
    print("insert")
    cursor = conn.cursor();
    sql = "INSERT INTO tasks (task_name, task_description) VALUES (%s,%s)"
    val = ("Washing", "Washing")
        
    cursor.execute(sql, val)
    conn.commit()

def updateData(conn):
    print("updated")
    cursor = conn.cursor();
    sql = "UPDATE tasks set task_name = %s, task_description = %s WHERE id = %s"
    val = ("Driving", "Driving", 2)
        
    cursor.execute(sql, val)
    conn.commit()

def deleteData(conn):
    print("deleted")
    cursor = conn.cursor();
    sql = "DELETE FROM tasks WHERE id = 2"
        
    cursor.execute(sql)
    conn.commit()

# insertData(conn)
# updateData(conn)
deleteData(conn)
showData(conn)
