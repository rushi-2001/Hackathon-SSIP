#import mysql.connector
import MySQLdb
mydb=MySQLdb.connect(host= "192.168.13.49", user="id11667953_gtest", passwd="pdpugtest",database="id11667953_gtest", port=3306)
#mydb = mysql.connector.connect(host='localhost',port = 3306, user="id11667953_gtest", passwd="pdpugtest",database="id11667953_gtest")
mycursor = mydb.cursor()
print("Cursor start")
sql=("SELECT * FROM authority;")
mycursor.execute(sql)
#print("\n\nThe details of restaurants with city %s is : \n\n " % city_name)
result = mycursor.fetchall()
for i in result:
    if(i): print(i)
    else: print("No data found!!")
	
print("DSDSD")