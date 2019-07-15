import mysql.connector
db_connection = mysql.connector.connect(
  host="mysqlinstance.chn43vccw8jq.us-west-2.rds.amazonaws.com",
  user="saiteja",
  passwd="jbsRVgn1!",
)
my_database = db_connection.cursor()
my_database.execute("DROP DATABASE testdb")
my_database.execute("CREATE DATABASE testdb")
my_database.execute("USE testdb")
my_database.execute("CREATE TABLE testTable (name VARCHAR(255), gender VARCHAR(10), age VARCHAR(10))")
sql_statement = "INSERT INTO testTable (name,gender,age) values(%s,%s,%s)"
values = ("saiteja","male","21")
my_database.execute(sql_statement,values)
db_connection.commit()
print ("Before Updating...");
sql_statement = "SELECT * FROM testTable"
my_database.execute(sql_statement)
output = my_database.fetchall()
for x in output:
  print(x)
sql_statement = "UPDATE testTable set age='25' where name='saiteja'"
my_database.execute(sql_statement)
db_connection.commit()
print ("After Updating...");
sql_statement = "SELECT * FROM testTable"
my_database.execute(sql_statement)
output = my_database.fetchall()
for x in output:
  print(x)
sql_statement = "DROP table testTable"
my_database.execute(sql_statement)
db_connection.commit()
print ("Table deleted successfully!!!!")