#encoding:utf-8

# 变量名必须是大小写英文字母，下划线，不能用数字开头
#多行注释 ''' 内容 '''

#变量类型，使用type()获取变量类型 int float str bool布尔类型(True False) 空值（None）
a=None
print(a)

#类型转换: int()	str() float() bool() 空字符串 0 None 时bool的值为False
cunk="1000"
cunk=int(cunk)

#列表list = [],列表索引从0开始
list1 = [1,2,23,"hello world","new world"]
# list1[2] = "2.123"
# print(list1)

# 列表的切片 索引下标从0开始，最后一个不取
print(list1[0:3]) #正向切片
print(list1[-4:-1]) #负向切片：-1表示最后一个

#修改列表
#增加 list1.appand("内容") 
list1.append("内容") 
print(list1)
#根据索引增加 list1.insert(3,"aaa")
list1.insert(3,"aaa")
print(list1)
#删除 list1.remove(23)
list1.remove(23)
print(list1)
#根据索引删除 del list1[1]
del list1[1]
print("del删除方式：",list1)
#删除 list1.pop(2)
list1.pop(2)
print("pop删除方式：",list1)
#获取列表长度
print(len(list1))

#元组(tuple)数组结构与列表类似，与列表不同的地方在于：元组中的数据不可更改

#定义元组()，元组也可以进行切片
a=(1,2,3,4,"laiah","aaa",3.14)
print(a[4:6])
#数据字典（dict）在其他语言中被称为哈希hash map或者相关数组
#字典是一个键值对的形式，字典的键不允许重复
user={"name":"张三","age":18,"hobby":"打球"}
print(user['name'])

#集合（set） 是一种无序集，它是一组键的集合
#两张定义方式
jihe = {1,2,3,4,5,"上山打老虎"}
jihe2 = set([1,2,3,4,5])

#集合可以去重
x = ['ad','ada','jj','da','ad','adfa']
x = set(x)  #转集合
print(list(x)) #转list

a={1,2,1,4,5}
b={4,3,4,6}
print(a,b,"集合的差：",a-b,"集合的并集",a|b,"集合的交集",a&b,"集合的对称差",a^b)

#重点是使用list列表和dict字典