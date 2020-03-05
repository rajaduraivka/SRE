import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="ops", user='ops', password='7sfEeEHHggvGvitFhDoa', host='data-p-ops-master.cwbpdp5vvep9.ap-south-1.rds.amazonaws.com', port= '5432'
)

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Fetching all the rows before the update
print("Contents of the sku_room_price_config: ")
sql = "SELECT * from v2.sku_room_price_config WHERE applicability ='0019919';"
cursor.execute(sql)
print(cursor.fetchall())

#Updating the records
sql = "UPDATE v2.sku_room_price_config SET acacia='0',oak='0', maple='200', mahogany='400' WHERE applicability ='0019919';"
cursor.execute(sql)
print("Table updated...... ")

#Fetching all the rows after the update
print("Contents of the sku_room_price_config table after the update operation: ")
sql = "SELECT * from v2.sku_room_price_config WHERE applicability ='0019919';"
cursor.execute(sql)
print(cursor.fetchall())

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()
       
