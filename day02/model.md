#模块和import语句
继续进入下一个阶段：在多个文件之间创建和使用 Python 代码。一个模块仅仅是 Python代码的一个文件。

按照这样的层次组织： 单词、句子、段落以及章。否则，超过一两页后就没有很好的可读性了。 代码也有类似的自底向上的组织层次：数据类型类似于单词，语句类似于句子，函数类似于段落，模块类似于章。以此类推，当我说某个内容会在第 8 章中说明时，就像是在其他模块中引用代码。引用其他模块的代码时使用 import 语句，被引用模块中的代码和变量对该程序可见。
##导入模块

import 语句最简单的用法是 import 模块，模块是不带 .py 扩展的另外一个 Python 文件的
文件名。现在来模拟一个气象站，并输出天气预报。其中一个主程序输出报告，一个单独
的具有单个函数的模块返回天气的描述。

下面是主程序（命名为 weatherman.py） ：

	import report

	description = report.get_description()
	print("Today's weather:", description)
以下是天气模块的代码（ report.py）：

	def get_description(): #看到下面的文档字符串了吗？
	"""Return random weather, just like the pros"""
		from random import choice
		possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
		return choice(possibilities)
如果上述两个文件在同一个目录下，通过 Python 运行主程序 weatherman.py，会引用
report 模块，执行函数 get_description()。函数 get_description() 从字符串列表中返回一个随机结果。下面就是主程序可能返回和输出的结果：


##使用别名导入模块
在主程序 weatherman.py 中，我们调用了 import report。但是，如果存在同名的另一个模
块或者你想使用更短更好记的名字， 该如何做呢？在这种情况下，可以使用别名 wr 进行
导入：

	import report as wr
	description = wr.get_description()
	print("Today's weather:", description)


##导入模块的一部分
在 Python 中，可以导入一个模块的若干部分。每一部分都有自己的原始名字或者你起的别
名。首先，从 report 模块中用原始名字导入函数 get_description()：

	from report import get_description
	description = get_description()
	print("Today's weather:", description)

用它的别名 do_it 导入：

	from report import get_description as do_it
	description = do_it()
	print("Today's weather:", description)

##模块搜索路径
Python 会在什么地方寻找文件来导入模块？使用命名为 path 变量的存储在标准 sys 模块
下的一系列目录名和 ZIP 压缩文件。你可以读取和修改这个列表。下面是在我的 Mac 上
Python 3.3 的 sys.path 的内容：
	
	>>> import sys
	>>> for place in sys.path:
	... print(place)
	...
	/Library/Frameworks/Python.framework/Versions/3.3/lib/python33.zip
	/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3
	/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/plat-darwin
	/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/lib-dynload
	/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/site-packages

最开始的空白输出行是空字符串 ''，代表当前目录。如果空字符串是在 sys.path 的开始
位置， Python 会先搜索当前目录： import report 会寻找文件 report.py。
第一个匹配到的模块会先被使用， 这也就意味着如果你在标准库之前的搜索路径上定义一
个模块 random，就不会导入标准库中的 random 模块。