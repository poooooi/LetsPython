from collections import namedtuple

'''
创建具名元组需要两个参数，一个是类名，一个是类的各个字段的名字。
后者可以是有数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串。
'''

# 具名元组的两种定义方式
people = namedtuple('peopleInfo', 'name sex age addr')
pet = namedtuple('petInfo', ['name', 'sex', 'age', 'master'])

# 创建具名元组的对象的两种方式
poi = people('poi', '女', 24,  ('浙江', '杭州', '余杭区'))
dodo = ('多多', '男', 2, ('poi', '女'))
pet._make(dodo)

# 具名元组的数据读取
print(people._fields)  # 打印结果：('name', 'sex', 'age', 'addr')
print(pet._fields)     # 打印结果：('name', 'sex', 'age', 'master')

print(poi)             # 打印结果：peopleInfo(name='poi', sex='女', age=24, addr=('浙江', '杭州', '余杭区'))
print(poi.sex)         # 打印结果：女

print(dodo)            # 打印结果：('多多', '男', 2, ('poi', '女'))
print(dodo[0])         # 打印结果：多多
print(dodo[1])         # 打印结果：男
print(dodo[2])         # 打印结果：2
print(dodo[3])         # 打印结果：('poi', '女')
