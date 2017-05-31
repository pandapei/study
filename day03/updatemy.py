import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='mysql',port=3306,db = 'day03')
cursor = conn.cursor()
SQL = 'update admin set username = %s where id = 1'

print cursor.execute(SQL,'yibo')


print cursor.fetchall()
conn.commit()

cursor.close()
conn.close()