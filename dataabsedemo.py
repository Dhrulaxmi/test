import pymysql
con=pymysql.connect(host="localhost",user="root",passwd="",db='inyty_24',port=3306)
print("Database Connected")
con.close()
print("Database closed")
