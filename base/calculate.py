# 整除 求余 次方
print(9//4)
print(9%4)
print(9**2)


# # input为str类型
# name = input()
# print(type(name))


# 转义、多行
print('123\nasd')
print('123\'asd')
print(r'123\nasd')
print('''123
asd
567''')


# 字符、整数 转换
print(ord('A'))
print(chr(65))


# 包含的字符数、字节数
print(len('asd'))
print(len('中文'))

print(len(b'asd'))
print(len('中文'.encode('utf-8')))


# %格式化方式
print('input nume is %d%%' %99)
print('input name is %s No.%f' %('Jon', 2))


# 列表
list = [1, 'a', 2.356, 'djijo', [2]]
print(list)
print(len(list))


# 隐藏函数
f = lambda x: x*x
print([f(x) for x in range(10)])
# print([lambda x: x*x for x in range(3)])

def foo():
    return [lambda x:i+x for i in range(4)] #Lambda函数只能返回一个表达式的值
print([x(1) for x in foo()])    #x（3）是一条单独的语句 调用了匿名函数


print(int('6'))
print(int('0b100', base=0))


# 字典
dirt = {'a':1, 'b':'ssdd', 2:'q'}
print(dirt[2])  #通过key提取value
print('a' in dirt)  #判断key是否存在
print(dirt.get('c'))    #判断key是否存在
dirt.pop('b')   #删除key
print(dirt)
key = '6'
dirt[key] = 89
print(dirt)


# set
s = set ([1, '2', 'dfe'])
s.add('q')
print(s)

