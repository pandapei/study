#数据库操作：

* 新建数据库

###windows sqlclient连接数据库:
	
	C:\Users\pjx>mysql -u root -p
	Enter password: *****
	Welcome to the MySQL monitor.  Commands end with ; or \g.
	Your MySQL connection id is 4
	Server version: 5.6.21-log MySQL Community Server (GPL)
	
	Copyright (c) 2000, 2014, Oracle and/or its affiliates. All rights reserved.
	
	Oracle is a registered trademark of Oracle Corporation and/or its
	affiliates. Other names may be trademarks of their respective
	owners.
	
	Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
	
	mysql>

###查询数据库：

	mysql> show databases;
	+--------------------+
	| Database           |
	+--------------------+
	| information_schema |
	| day03              |
	| jtm                |
	| mybatis            |
	| mydb               |
	| mysql              |
	| performance_schema |
	| sakila             |
	| spd-hc             |
	| test               |
	| test_test          |
	| timdb              |
	| world              |
	+--------------------+
	13 rows in set (0.00 sec)
	
	mysql> use day03;
	Database changed
	mysql> show tables;
	Empty set (0.00 sec)

###查询表：

	mysql> show tables
	    -> ;
	+-----------------+
	| Tables_in_day03 |
	+-----------------+
	| cmdb            |
	+-----------------+
	1 row in set (0.00 sec)

###查询：

	mysql> select * from cmdb;
	+----+----------+-------------+
	| id | name     | ip          |
	+----+----------+-------------+
	|  1 | server01 | 192.168.1.1 |
	|  2 | server02 | 192.168.1.2 |
	+----+----------+-------------+
	2 rows in set (0.00 sec)
	
	mysql> create table admin(id int,username varchar(50),passwd varchar(50));
	Query OK, 0 rows affected (0.33 sec)

###创建表，插入数据
	mysql> create table admin(id int,username varchar(50),passwd varchar(50));
	Query OK, 0 rows affected (0.33 sec)
	
	mysql> insert into admin(id,username,passwd) values(2,'admin2','admin123');
	Query OK, 1 row affected (0.06 sec)

	mysql> select * from admin;
	+------+----------+----------+
	| id   | username | passwd   |
	+------+----------+----------+
	|    1 | admin    | admin123 |
	|    2 | admin2   | admin123 |
	+------+----------+----------+
	2 rows in set (0.00 sec)


#MySQLdb
	
	# 导入MySQLdb模块
	>>> import MySQLdb
	# 创建一个Connect连接
	>>> conn = MySQLdb.Connect(host='127.0.0.1', user='root', passwd='as', db='USER', port=3306, charset="utf8")
	>>> cursor = conn.cursor()
	>>> print(cursor)
	<MySQLdb.cursors.Cursor object at 0x7f4af5e15550>
	>>> print(conn)
	<_mysql.connection open to '127.0.0.1' at 15b1518>
	# 关闭连接
	>>> conn.close()
	>>> print(conn)
	<_mysql.connection closed at 15b1518>


###查询数据

	import MySQLdb
	
	conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='mysql',port=3306,db = 'day03')
	cursor = conn.cursor()
	SQL = 'select * from admin;'
	
	print cursor.execute(SQL)
	#修改数据的行数
	
	print cursor.fetchall()
	
	cursor.close()
	conn.close()


###插入数据
	
	import MySQLdb
	
	conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='mysql',port=3306,db = 'day03')
	cur = conn.cursor()
	  
	reCount = cur.execute('insert into admin(username,passwd) values(%s,%s)',('A1','usa'))
	  
	conn.commit()
	  
	cur.close()
	conn.close()
	  
	print reCount

2条数据一起插入：
	
	import MySQLdb

	conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='mysql',port=3306,db = 'day03')
	
	cur = conn.cursor()
	
	li =[
	     ('A1','usa'),
	     ('A2','usD'),
	]
	reCount = cur.executemany('insert into UserInfo(Name,Address) values(%s,%s)',li)
	
	conn.commit()
	cur.close()
	conn.close()
	
	print reCount




###删除数据

	import MySQLdb
	
	conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='mysql',port=3306,db = 'day03')
	cursor = conn.cursor()
	SQL = 'select * from admin'
	#SQL = 'select * from admin where id = %s'
	print cursor.execute(SQL)
	#修改数据的行数
	
	print cursor.fetchall()
	conn.commit()
	
	cursor.close()
	conn.close()

###修改数据

	import MySQLdb
	
	conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='mysql',port=3306,db = 'day03')
	cursor = conn.cursor()
	SQL = 'update admin set username = %s where id = 1'
	
	print cursor.execute(SQL,'yibo')
	
	
	print cursor.fetchall()
	conn.commit()
	
	cursor.close()
	conn.close()

事务

访问额更新数据库的一个程序执行单元,执行单元指的就是很多操作的集合,里面的每个操作都是用来访问个更新数据库.

原子性: 事务中包括的诸多操作要么都做要么都不做

比如银行转账,A用户向B用户转账100,A-100和B+100这两个操作,要么都做,要么都不操作

* 一致性: 事务必须使数据库从一致性状态变到另一个一致性状态
* 隔离性: 一个事务的执行不能被其他事务干扰
* 持久性: 事务一旦提交,他对数据库的改变是永久性的
* 开发中怎样使用事务?

关闭自动commit: 设置conn.autocommit(False),MySQLdb默认已经为False

正常结束事务: conn.commit()

异常结束事务: conn.rollback()


###查询mysql数据返回字典类型数据：

	import MySQLdb
	
	conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='mysql',port=3306,db = 'day03')
	cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
	reCount = cur.execute('select * from admin')
	data = cur.fetchall()
	
	conn.commit()
	
	cur.close()
	conn.close()
	
	print reCount
	print data
	
输出

	5
	({'username': 'yibo', 'passwd': 'admin123', 'id': 1L}, {'username': 'admin2', 'passwd':
	 'admin123', 'id': 2L}, {'username': 'A1', 'passwd': 'usa', 'id': 3L}, {'username': 'A2', 
	'passwd': 'usa', 'id': 4L}, {'username': 'A3', 'passwd': 'usa', 'id': 5L})

###fetchone or scroll
	import MySQLdb
	
	conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='mysql',port=3306,db = 'day03')
	cur = conn.cursor()
	 
	reCount = cur.execute('select * from admin')
	 
	print cur.fetchone()
	print cur.fetchone()
	#相对定位
	cur.scroll(-1,mode='relative')
	print cur.fetchone()
	print cur.fetchone()
	#相对定位
	cur.scroll(0,mode='absolute')
	print cur.fetchone()
	print cur.fetchone()
	 
	cur.close()
	conn.close()
	 
	print reCount


###获取自增ID

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
