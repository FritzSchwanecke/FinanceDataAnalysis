from mysql.connector import connect

db = connect(host="localhost",user="root",passwd="SCHNov15")
db1 = db.cursor()
#sql = "CREATE DATABASE IF NOT EXISTS securities_master"
#db1.execute(sql)
sql = "USE securities_master"
db1.execute(sql)
#Throws errors...
#sql="CREATE USER IF NOT EXISTS 'sec_user'@'localhost' IDENTIFIED BY 'Oe2Ey(LY(k)D'"
#db1.execute(sql)
#sql="GRANT ALL PRIVILEGES ON securities_master.* TO 'sec_user'@'localhost'"
#sql = "FLUSH PRIVILEGES"
#db1.execute(sql)


#Create Table for Exchanges
sql = "CREATE TABLE exchange (id int NOT NULL AUTO_INCREMENT, abbrev varchar(64) NOT NULL, name varchar(255) NOT NULL, PRIMARY KEY (id)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8"

db1.execute(sql)
