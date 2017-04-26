##推导式
推导式是从一个或者多个迭代器快速简洁地创建数据结构的一种方法。 它可以将循环和条
件判断结合， 从而避免语法冗长的代码。会使用推导式有时可以说明你已经超过 Python 初
学者的水平。也就是说，使用推导式更像 Python 风格。

###列表推导式
你可以从 1 到 5 创建一个整数列表，每次增加一项，如下所示：

	>>> number_list = []
	>>> number_list.append(1)
	>>> number_list.append(2)
	>>> number_list.append(3)
	>>> number_list.append(4)
	>>> number_list.append(5)
	>>> number_list
	[1, 2, 3, 4, 5]

或者，可以结合 range() 函数使用一个迭代器：

	>>> number_list = []
	>>> for number in range(1, 6):
	... number_list.append(number)
	...
	>>> number_list
	[1, 2, 3, 4, 5]

或者，直接把 range() 的返回结果放到一个列表中：

	>>> number_list = list(range(1, 6))
	>>> number_list
	[1, 2, 3, 4, 5]
上面这些方法都是可行的 Python 代码，会得到相同的结果。然而，更像 Python 风格的创
建列表方式是使用列表推导。最简单的形式如下所示：

	[ expression for item in iterable ]
下面的例子将通过列表推导创建一个整数列表：

	>>> number_list = [number for number in range(1,6)]
	>>> number_list
	[1, 2, 3, 4, 5]
在第一行中，第一个 number 变量为列表生成值，也就是说，把循环的结果放在列表
number_list 中。第二个 number 为循环变量。其中第一个 number 可以为表达式，试试下面
改编的例子：

	>>> number_list = [number-1 for number in range(1,6)]
	>>> number_list
	[0, 1, 2, 3, 4]


列表推导把循环放在方括号内部。这种例子和之前碰到的不大一样，但却是更为常见的方
式。同样，列表推导也可以像下面的例子加上条件表达式：

	[expression for item in iterable if condition]
现在，通过推导创建一个在 1 到 5 之间的偶数列表（当 number % 2 为真时，代表奇数；为
假时，代表偶数）：

	>>> a_list = [number for number in range(1,6) if number % 2 == 1]
	>>> a_list
	[1, 3, 5]
于是，上面的推导要比之前传统的方法更简洁：

	>>> a_list = []
	>>> for number in range(1,6):
	... if number % 2 == 1:
	... a_list.append(number)
	...
	>>> a_list
	[1, 3, 5]

最后，正如存在很多嵌套循环一样，在对应的推导中会有多个 for ... 语句。我们先来看
一个简单的嵌套循环的例子，并在屏幕上打印出结果：

	>>> rows = range(1,4)
	>>> cols = range(1,3)
	>>> for row in rows:
	... for col in cols:
	... print(row, col)
	...
	1 1
	1 2
	2 1
	2 2
	3 1
	3 2
下面使用一次推导，将结果赋值给变量 cells，使它成为元组 (row,col):

	>>> rows = range(1,4)
	>>> cols = range(1,3)
	>>> cells = [(row, col) for row in rows for col in cols]
	>>> for cell in cells:
	... print(cell)
	...
	(1, 1)
	(1, 2)
	(2, 1)
	(2, 2)
	(3, 1)
	(3, 2)
另外，在对 cells 列表进行迭代时可以通过元组拆封将变量 row 和 col 的值分别取出：

	>>> for row, col in cells:
	... print(row, col)
	...
	1 1
	1 2
	2 1
	2 2
	3 1
	3 2
其中，在列表推导中 for row ... 和 for col ... 都可以有自己单独的 if 条件判断



###字典推导式

除了列表，字典也有自己的推导式。最简单的例子就像：

	{ key_expression : value_expression for expression in iterable }
类似于列表推导，字典推导也有 if 条件判断以及多个 for 循环迭代语句：

	>>> word = 'letters'
	>>> letter_counts = {letter: word.count(letter) for letter in word}
	>>> letter_counts
	{'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}
程序中，对字符串 'letters' 中出现的字母进行循环，计算出每个字母出现的次数。对于
程序执行来说， 两次调用 word.count(letter) 浪费时间，因为字符串中 t 和 e 都出现了两
次，第一次调用 word.count() 时已经计算得到相应的值。下面的例子会解决这个小问题，
更符合 Python 风格：
	
	>>> word = 'letters'
	>>> letter_counts = {letter: word.count(letter) for letter in set(word)}
	>>> letter_counts
	{'t': 2, 'l': 1, 'e': 2, 'r': 1, 's': 1}
字典键的顺序和之前的例子是不同的，因为是对 set(word) 集合进行迭代的，而前面的例
子是对 word 字符串迭代。

###集合推导式
集合也不例外，同样有推导式。最简单的版本和之前的列表、字典推导类似：

	{expression for expression in iterable }
最长的版本（ if tests, multiple for clauses）对于集合而言也是可行的：

	>>> a_set = {number for number in range(1,6) if number % 3 == 1}
	>>> a_set
	{1, 4}