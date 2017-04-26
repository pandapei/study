#函数

到目前为止，我们的 Python 代码已经实现了小的分块。它们都适合处理微小任务，但是我
们想复用这些代码，所以需要把大型代码组织成可管理的代码段。
代码复用的第一步是使用函数，它是命名的用于区分的代码段。 函数可以接受任何数字或
者其他类型的输入作为参数，并且返回数字或者其他类型的结果。
你可以使用函数做以下两件事情：

* 定义函数
* 调用函数

为了定义 Python 函数，你可以依次输入 def、函数名、带有函数参数的圆括号，最后紧跟
一个冒号（ :）。函数命名规范和变量命名一样（必须使用字母或者下划线 _ 开头，仅能含
有字母、数字和下划线）。

我们先定义和调用一个没有参数的函数。下面的例子是最简单的 Python 函数：

	>>> def do_nothing():
	... 	pass
即使对于一个没有参数的函数，仍然需要在定义时加上圆括号和冒号。下面的一行需要像
声明 if 语句一样缩进。 Python 函数中的 pass 表明函数没有做任何事情。和这一页故意留
白有同样的作用（即使它不再是）。

通过输入函数名和参数调用此函数，像前面说的一样，它没有做任何事情：

	>>> do_nothing()
	>>>
现在，定义一个无参数，但打印输出一个单词的函数：

	>>> def make_a_sound():
	... 	print('quack')
	...
	>>> make_a_sound()
	quack
当调用 make_a_sound() 函数时， Python 会执行函数内部的代码。在这个例子中，函数打印
输出单个词，并且返回到主程序。

下面尝试一个没有参数但返回值的函数：

	>>> def agree():
	... 	return True
	...
或者，调用这个函数，使用 if 语句检查它的返回值：

	>>> if agree():
	... 	print('Splendid!')
	... else:
	... 	print('That was unexpected.')
	...
	Splendid!
学到现在已经迈出了很大的一步。在函数中，使用 if 判断和 for/while 循环组合能实现之
前无法实现的功能。

这个时候该在函数中引入参数。 定义带有一个 anything 参数的函数 echo()。它使用
return 语句将 anything 返回给它的调用者两次，并在两次中间加入一个空格：

	>>> def echo(anything):
	... 	return anything + ' ' + anything
	...
	>>>

然后用字符串 'Rumplestiltskin' 调用函数 echo()：

	>>> echo('Rumplestiltskin')
	'Rumplestiltskin Rumplestiltskin'


传入到函数的值称为参数。当调用含参数的函数时， 这些参数的值会被复制给函数中的对
应参数。在之前的例子中， 被调用的函数 echo() 的传入参数字符串是 'Rumplestiltskin'，
这个值被复制给参数 anything , 然后返回到调用方（在这个例子中，输出两次字符串，中
间有一个空格）。

上面的这些函数例子都很基础。 现在我们写一个含有输入参数的函数，它能真正处理一些
事情。在这里依旧沿用评论颜色的代码段。调用 commentary 函数，把 color 作为输入的参
数，使它返回对颜色的评论字符串：

	>>> def commentary(color):
	... 	if color == 'red':
	... 		return "It's a tomato."
	... 	elif color == "green":
	... 		return "It's a green pepper."
	... 	elif color == 'bee purple':
	... 		return "I don't know what it is, but only bees can see it."
	... 	else:
	... 		return "I've never heard of the color " + color + "."
	...
	>>>
传入字符串参数 'blue'，调用函数 commentary()：

	>>> comment = commentary('blue')
这个函数做了以下事情：

* 把 'blue' 赋值给函数的内部参数 color
* 运行 if-elif-else 的逻辑链
* 返回一个字符串
* 将该字符串赋值给变量 comment

我们如何得到返回值呢？

	>>> print(comment)
	I've never heard of the color blue.
一个函数可以接受任何数量（包括 0）的任何类型的值作为输入变量，并且返回任何数量
（包括 0）的任何类型的结果。如果函数不显式调用 return 函数，那么会默认返回 None。

	>>> print(do_nothing())
	None

###位置参数
Python 处理参数的方式要比其他语言更加灵活。其中，最熟悉的参数类型是位置参数，传
入参数的值是按照顺序依次复制过去的。

下面创建一个带有位置参数的函数，并且返回一个字典：

	>>> def menu(wine, entree, dessert):
	... 	return {'wine': wine, 'entree': entree, 'dessert': dessert}
	...
	>>> menu('chardonnay', 'chicken', 'cake')
	{'dessert': 'cake', 'wine': 'chardonnay', 'entree': 'chicken'}
尽管这种方式很常见，但是位置参数的一个弊端是必须熟记每个位置的参数的含义。在调
用函数 menu() 时误把最后一个参数当作第一个参数，会得到完全不同的结果：

	>>> menu('beef', 'bagel', 'bordeaux')
	{'dessert': 'bordeaux', 'wine': 'beef', 'entree': 'bagel'}
###关键字参数
为了避免位置参数带来的混乱，调用参数时可以指定对应参数的名字，甚至可以采用与函
数定义不同的顺序调用：

	>>> menu(entree='beef', dessert='bagel', wine='bordeaux')
	{'dessert': 'bagel', 'wine': 'bordeaux', 'entree': 'beef'}
你也可以把位置参数和关键字参数混合起来。首先，实例化参数 wine，然后对参数 entree
和 dessert 使用关键字参数的方式：

	>>> menu('frontenac', dessert='flan', entree='fish')
	{'entree': 'fish', 'dessert': 'flan', 'wine': 'frontenac'}
如果同时出现两种参数形式，首先应该考虑的是位置参数。
###指定默认参数值
当调用方没有提供对应的参数值时，你可以指定默认参数值。这个听起来很普通的特性实
际上特别有用，以之前的例子为例：

	>>> def menu(wine, entree, dessert='pudding'):
	... 	return {'wine': wine, 'entree': entree, 'dessert': dessert}
这一次调用不带 dessert 参数的函数 menu()：

	>>> menu('chardonnay', 'chicken')
	{'dessert': 'pudding', 'wine': 'chardonnay', 'entree': 'chicken'}
如果你提供参数值，在调用时会代替默认值：

	>>> menu('dunkelfelder', 'duck', 'doughnut')
	{'dessert': 'doughnut', 'wine': 'dunkelfelder', 'entree': 'duck'}

###使用*收集位置参数
Python 是没有指针概念的。

当参数被用在函数内部时， 星号将一组可变数量的位置参数集合成参数值的元组。在下面
的例子中 args 是传入到函数 print_args() 的参数值的元组：

	>>> def print_args(*args):
	... print('Positional argument tuple:', args)
	...
无参数调用函数，则什么也不会返回：

	>>> print_args()
	Positional argument tuple: ()
给函数传入的所有参数都会以元组的形式返回输出：

	>>> print_args(3, 2, 1, 'wait!', 'uh...')
	Positional argument tuple: (3, 2, 1, 'wait!', 'uh...')
这样的技巧对于编写像 print() 一样接受可变数量的参数的函数是非常有用的。如果你的
函数同时有限定的位置参数，那么 *args 会收集剩下的参数：

	>>> def print_more(required1, required2, *args):
	... print('Need this one:', required1)
	... print('Need this one too:', required2)
	... print('All the rest:', args)
	...
	>>> print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
	Need this one: cap
	Need this one too: gloves
	All the rest: ('scarf', 'monocle', 'mustache wax')
当使用 * 时不需要调用元组参数 args，不过这也是 Python 的一个常见做法。


###使用**收集关键字参数
使用两个星号可以将参数收集到一个字典中，参数的名字是字典的键，对应参数的值是字
典的值。下面的例子定义了函数 print_kwargs()，然后打印输出它的关键字参数：

	>>> def print_kwargs(**kwargs):
	... print('Keyword arguments:', kwargs)
	...
现在，使用一些关键字参数调用函数：

	>>> print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
	Keyword arguments: {'dessert': 'macaroon', 'wine': 'merlot', 'entree': 'mutton'}
	在函数内部， kwargs 是一个字典。
如果你把带有 *args 和 **kwargs 的位置参数混合起来，它们会按照顺序解析。和 args 一
样，调用时不需要参数 kwargs，这也是常见用法。

###文档字符串
正如《 Python 之禅》（ the Zen of Python）中提到的， 程序的可读性很重要。建议在函数体
开始的部分附上函数定义说明的文档，这就是函数的文档字符串：

	>>> def echo(anything):
	... 'echo returns its input argument'
	... return anything
可以定义非常长的文档字符串，加上详细的规范说明，如下所示：

	def print_if_true(thing, check):
	'''
	Prints the first argument if a second argument is true.
	The operation is:
	1. Check whether the *second* argument is true.
	2. If it is, print the *first* argument.
	'''
	if check:
		print(thing)
调用 Python 函数 help() 可以打印输出一个函数的文档字符串。把函数名传入函数 help()
就会得到参数列表和规范的文档：
	
	>>> help(echo)
	Help on function echo in module __main__:
	echo(anything)
	echo returns its input argument
如果仅仅想得到文档字符串：

	>>> print(echo.__doc__)
	echo returns its input argument
看上去很奇怪的 __doc__ 是作为函数中变量的文档字符串的名字。 4.10 节的“名称中 _ 和
__ 的用法”会解释所有下划线背后的原理。


### 函数高级用法
之前提过 Python 中一切都是对象，包括数字、 字符串、元组、列表、字典和函数。函数是
Python 中的一等公民， 可以把它们（返回值）赋给变量，可以作为参数被其他函数调用，
也可以从其他函数中返回值。它可以帮助你在 Python 中实现其他语言难以实现的功能。

为了测试，现在定义一个简单的函数 answer()，它没有任何参数，仅仅打印输出数字 42：

	>>> def answer():
	... print(42)

运行该函数，会得到下面的结果：

	>>> answer()


再定义一个函数 run_something。它有一个参数 func，这个参数是一个可以运行的函数的
名字：

	>>> def run_something(func):
	... func()
将参数 answer 传到该函数，在这里像之前碰到的一样，把函数名当作数据使用：

	>>> run_something(answer)
	42
注意，你传给函数的是 answer , 而不是 answer()。在 Python 中圆括号意味着调用函数。在
没有圆括号的情况下， Python 会把函数当作普通对象。这是因为在其他情况下，它也仅仅
代表一个对象：

	>>> type(run_something)
	<class 'function'>
我们来运行一个带参数的例子。定义函数 add_args()，它会打印输出两个数值参数（ arg1
和 arg2）的和：

	>>> def add_args(arg1, arg2):
	... print(arg1 + arg2)
那么， add_args() 的类型是什么？

	>>> type(add_args)
	<class 'function'>
此刻定义一个函数 run_something_with_args()，它带有三个参数：
* func——可以运行的函数
* arg1——func 函数的第一个参数
* arg2——func 函数的第二个参数

	>>> def run_something_with_args(func, arg1, arg2):
	... func(arg1, arg2)
当调用 run_something_with_args() 时，调用方传来的函数赋值给 func 参数，而 arg1 和
arg2 从参数列表中获得值。然后运行带参数的 func(arg1, arg2)。

将函数名 add_args 和参数 5、 9 传给函数 run_something_with_args()：

	>>> run_something_with_args(add_args, 5, 9)
	14
在函数 run_something_with_args() 内部，函数名 add_args 被赋值给参数 func， 5 和 9 分
别赋值给 arg1 和 arg2。程序最后执行：

	add_args(5, 9)

同样可以在此用上 *args（位置参数收集）和 **kwargs（关键字参数收集）的技巧。

我们定义一个测试函数， 它可以接受任意数量的位置参数，使用 sum() 函数计算它们的和，并返回这个和：
	
	>>> def sum_args(*args):
	... return sum(args)
之前没有提到 sum() 函数，它是 Python 的一个内建函数，用来计算可迭代的数值（整型或
者浮点型）参数的和。

下面再定义一个新的函数 run_with_positional_args() , 接收一个函数名以及任意数量的位
置参数：

	>>> def run_with_positional_args(func, *args):
	... return func(*args)
现在直接调用它：

	>>> run_with_positional_args(sum_args, 1, 2, 3, 4)
	10
同样可以把函数作为列表、元组、集合和字典的元素。函数名是不可变的，因此可以把函
数用作字典的键。

###内部函数
在 Python 中，可以在函数中定义另外一个函数：
	
	>>> def outer(a, b):
	... 	def inner(c, d):
	... 		return c + d
	... 	return inner(a, b)
	...
	>>>
	>>> outer(4, 7)
	11
当需要在函数内部多次执行复杂的任务时，内部函数是非常有用的，从而避免了循环和代
码的堆叠重复。 对于这样一个字符串的例子，内部函数的作用是给外部的函数增加字符串
参数：
	
	>>> def knights(saying):
	... 	def inner(quote):
	... 		return "We are the knights who say: '%s'" % quote
	... 	return inner(saying)
	...
	>>> knights('Ni!')
	"We are the knights who say: 'Ni!'"




##命名空间和作用域
一个名称在不同的使用情况下可能指代不同的事物。 Python 程序有各种各样的命名空
间，它指的是在该程序段内一个特定的名称是独一无二的，它和其他同名的命名空间
是无关的。

每一个函数定义自己的命名空间。 如果在主程序（ main）中定义一个变量 x，在另外一个
函数中也定义 x 变量，两者指代的是不同的变量。但是，天下也没有完全绝对的事情，需
要的话，可以通过多种方式获取其他命名空间的名称。

每个程序的主要部分定义了全局命名空间。因此，在这个命名空间的变量是全局变量。
你可以在一个函数内得到某个全局变量的值：

	>>> animal = 'fruitbat'
	>>> def print_global():
	... 	print('inside print_global:', animal)
	...
	>>> print('at the top level:', animal)
	at the top level: fruitbat
	>>> print_global()
	inside print_global: fruitbat
但是，如果想在函数中得到一个全局变量的值并且改变它，会报错：

	>>> def change_and_print_global():
	... 	print('inside change_and_print_global:', animal)
	... 	animal = 'wombat'
	... print('after the change:', animal)
	...
	>>> change_and_print_global()
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	File "<stdin>", line 2, in change_and_report_it
	UnboundLocalError: local variable 'animal' referenced before assignment


实际上，你改变的另外一个同样被命名为 animal 的变量，只不过这个变量在函数内部：

	>>> def change_local():
	... 	animal = 'wombat'
	... 	print('inside change_local:', animal, id(animal))
	...
	>>> change_local()
	inside change_local: wombat 4330406160
	>>> animal
	'fruitbat'
	>>> id(animal)
	4330390832
这里发生了什么？在函数第一行将字符串 fruitbat 赋值给全局变量 animal。函数 change_
local() 也有一个叫作 animal 的变量。不同的是，它在自己的局部命名空间。

我们使用 Python 内嵌函数 id() 打印输出每个对象的唯一的 ID 值，证明在函数 change_
local() 中的变量 animal 和主程序中的 animal 不是同一个。

为了读取全局变量而不是函数中的局部变量， 需要在变量前面显式地加关键字 global（也
正是《 Python 之禅》中的一句话： 明了胜于隐晦） ：

	>>> animal = 'fruitbat'
	>>> def change_and_print_global():
	... 	global animal
	... 	animal = 'wombat'
	... 	print('inside change_and_print_global:', animal)
	...
	>>> animal
	'fruitbat'
	>>> change_and_print_global()
	inside change_and_print_global: wombat
	>>> animal
	'wombat'
如果在函数中不声明关键字 global， Python 会使用局部命名空间，同时变量也是局部的。
函数执行后回到原来的命名空间。



###名称中_和__的用法
以两个下划线 __ 开头和结束的名称都是 Python 的保留用法。因此，在自定义的变量中不
能使用它们。选择这种命名模式是考虑到开发者一般是不会选择它们作为自己的变量的。

例如，一个函数的名称是系统变量 function.__name__，它的文档字符串是 function.__
doc__：

	>>> def amazing():
	... 	'''This is the amazing function.
	... 	Want to see it again?'''
	... 	print('This function is named:', amazing.__name__)
	... 	print('And its docstring is:', amazing.__doc__)
	...
	>>> amazing()
	This function is named: amazing
	And its docstring is: This is the amazing function.
	Want to see it again?
如同之前 globals 的输出结果所示，主程序被赋值特殊的名字 __main__。

##使用try和except处理错误
在一些编程语言中， 错误是通过特殊的函数返回值指出的，而 Python 使用异常，它是一段只有错误发生时执行的代码。

之前已经接触到一些有关错误的例子， 例如读取列表或者元组的越界位置或者字典中不存
在的键。所以，当你执行可能出错的代码时，需要适当的异常处理程序用于阻止潜在的错
误发生。

在异常可能发生的地方添加异常处理程序， 对于用户明确错误是一种好方法。即使不会及
时解决问题， 至少会记录运行环境并且停止程序执行。如果发生在某些函数中的异常不能
被立刻捕捉， 它会持续，直到被某个调用函数的异常处理程序所捕捉。在你不能提供自己
的异常捕获代码时， Python 会输出错误消息和关于错误发生处的信息，然后终止程序，例
如下面的代码段：
	
	>>> short_list = [1, 2, 3]
	>>> position = 5
	>>> short_list[position]
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	IndexError: list index out of range
与其让错误随机产生，不如使用 try 和 except 提供错误处理程序：

	>>> short_list = [1, 2, 3]
	>>> position = 5
	>>> try:
	... 	short_list[position]
	... except:
	... 	print('Need a position between 0 and', len(short_list)-1, ' but got',position)
	... 
	Need a position between 0 and 2 but got 5
在 try 中的代码块会被执行。如果存在错误，就会抛出异常，然后执行 except 中的代码；
否则，跳过 except 块代码。