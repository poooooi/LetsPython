'''
实现将python值和yaml格式数据相互转换的常用方法有：
yaml.safe_dump()、yaml.safe_load()、yaml.safe_dump_all()、yaml.safe_load_all()
存在yaml.dump()、yaml.load()函数，同样能实现数据转换功能，只是官方不太推荐使用。
原因："Resolve only basic YAML tags. This is known to be safe for untrusted input."
'''

import yaml
dict_data = {'a': 1, 'b': 2}
dict_data1 = {'c': 3, 'd': 4}
dict_data2 = {'e': 5, 'f': 6}

# 使用safe_dump函数，将dict_data内容,按照yaml的格式写入文件data.yaml
print("=========safe_dump函数的使用=========")
with open('PyYaml/data.yaml', 'w', encoding='UTF-8') as yaml_file:
    yaml.safe_dump(dict_data, yaml_file)

# 使用safe_load函数，将文件data.yaml中的文件内容读取并打印
print("=========safe_load函数的使用=========")
with open('PyYaml/data.yaml', encoding='UTF-8') as yaml_file:
    data = yaml.safe_load(yaml_file)
print(type(data))
print(data)

# 使用safe_dump_all函数，将一序列的python值转换为yaml格式文件
print("=========safe_dump_all函数的使用=========")
with open('PyYaml/data_all.yaml', 'w', encoding='UTF-8') as yaml_file:
    yaml.safe_dump_all([dict_data, dict_data1, dict_data2], yaml_file)

# 使用safe_load_all函数，将文件data_all.yaml中的文件内容读取并打印
print("=========safe_load_all函数的使用=========")
with open('PyYaml/data_all.yaml', encoding='UTF-8') as yaml_file:
    data = yaml.safe_load_all(yaml_file)
    print(type(data))
    for item in data:
        print(item)
