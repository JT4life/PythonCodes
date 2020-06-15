import json
str_data="normal string"
intData=20
floatData=2.345
listData=[str_data,intData,floatData]
nested_list=[intData,floatData,listData]

dictionary={
    'int':intData,
    'str':str_data}

print(json.dumps(str_data))
print(json.dumps(intData))
print(json.dumps(dictionary))
