# list 常见操作

# 定义一个list
list0 = [1, 5, 9, 10]
print(list0)

# list生成式
list1 = [i * i for i in range(10)]
# 结果[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list1)


# 创建一个list，list中的元素为：2，4，6，8，10
j = 2
list2 = [i * j for i in range(1, 6)]
print(list2)

# 使用内置函数list()
list3 = list()
print(list3, type(list3))


# 查询元素索引,index中输入list中的元素值
a = list0.index(9)
print(a)

# 获取单个元素,方括号中输入元素的索引值
b = list0[2]
print(b)

# 获取多个元素，切片,输出1到结尾
c = list0[1:]
print(c)

# in 和 not in，判断一个元素是否在list中，返回值是Boolean类型
d = 1 in list0
print(d, type(a))
e = 100 not in list0
print(e, type(e))


# list内置方法append()，在list末尾添加一个元素
print(list0)
list0.append(100)
print(list0)

# list内置方法extend(),在list末尾添加至少一个元素
list4 = ['hello', 'world']
print(list0)
list0.extend(list4)
print(list0)

# list内置方法insert(),在list指定位置添加元素
print(list0)
list0.insert(1, 99)
# 在一号位置插入99，其他位置元素向后顺延
print(list0)


# list切片,改变list中任意多的值，改变的数量可以与原来list中的元素数量不同
print(list0)
list0[1:] = [5, 6, 5, 28]
print(list0)


# list中的内置方法remove(),括号中输入list中的元素值，一次删除一个元素，重复元素只删除第一个，元素不存在抛出ValueError
print(list0)
list0.remove(5)
print(list0)
# list0.remove(100)
# print(list0)会抛出异常

# list中的内置方法pop(),删除一个指定索引位置上的元素，指定索引不存在抛出IndexError，不指定索引，删除list中最后一个元素
print(list0)
list0.pop(1)
print(list0)
list0.pop()
print(list0)


# 利用切片删除list中的元素
print(list0)
# 清空list
list0[:] = []
print(list0)
list0 = [i for i in range(10)]
print(list0)
# 将从5号开始的元素全部删除，包括5号元素
list0[5:] = []
print(list0)

# list内置方法clear()，清空list,但是list对象还在
print(list0)
list0.clear()
print(list0, id(list0))

# 全局函数del,删除list
list0 = [i for i in range(10)]
print(list0, id(list0))
# 可以删除单个元素
del list0[0]
print(list0, id(list0))
# 可以删除多个元素
del list0[1:3]
print(list0)
# 可以删除整个list，相当于回收了list0，这个对象不存在，没有id了
del list0


# list元素的修改操作
# 为指定的元素赋予一个新值
list0 = [i for i in range(10)]
print(list0)
list0[2] = 100
print(list0)


# 修改list的多个值
print(list0)
# 还是一样的，个数不用对应，相当于在第0个数据和第三个数据之间插入了四个数据
list0[1:3] = [15, 6, 89, 65]
print(list0)


# list排序操作 sort() 和 全局函数sorted
print(list0, id(list0))
# sort默认按照升序排列，不会产生新的对象
list0.sort()
print(list0, id(list0))
list0.sort(reverse=True)
print(list0, id(list0))

# sorted默认按照升序排列，会产生一个新的list对象
print(list0, id(list0))
list5 = sorted(list0)
print(list5, id(list5))
list6 = sorted(list0, reverse=True)
print(list6, id(list6))

# list的遍历
print(list0)
for i in list0:
    print(i)
