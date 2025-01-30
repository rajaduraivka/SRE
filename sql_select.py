import psycopg2
import csv
import sys


host_name = 'rms-p-rackrate-master-pg.com'
db_port = '6432'
db_name = 'rackrate_db'
db_user = 'rackrate_admin'

conn = psycopg2.connect(host=host_name, dbname=db_name,  user=db_user, port=db_port)

cur = conn.cursor()

sql = "COPY (SELECT name FROM property) TO STDOUT WITH CSV DELIMITER ';'"
with open("/Users/rajadurai/B2B_projects/Property_Name.csv", "w") as file:
    cur.copy_expert(sql, file)
