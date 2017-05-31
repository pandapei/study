import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='mysql',port=3306,db = 'day03')
cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
SQL = "insert into admin(username,passwd) values(%s,%s)"
reCount = cur.execute(SQL,("user1","p1"))
#data = cur.fetchall()
print cur.lastrowid
conn.commit()

cur.close()
conn.close()
