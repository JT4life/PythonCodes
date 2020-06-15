#Python json : JavaScript Object Notation
#Its an open standard file format that uses human readable text
#to transmit data objs consisting of attrib and value pairs
#and array data types. Its a common data format used for ASYNCHRONUS communication
#over the browser/network
#{"A":"ABCD"}, [11,22,33,4]
import json
str_data="normal string"
int_data=1
float_data=1.56
list_data=[str_data,int_data,float_data]
nested_list=[int_data,float_data,list_data]
dictionary={
    'int':int_data,
    'str':str_data,
    'float':float_data,
    'list':list_data,
    'nested_list':nested_list
    }
#Convert them to json data
print(json.dumps(str_data))
print(json.dumps(int_data))
print(json.dumps(float_data))
print(json.dumps(list_data))
print(json.dumps(nested_list))
print(json.dumps(dictionary))

#Dict--Object
#List,Tuple,--Array
#Str --String
#int,float--Number
#True --true
#False --false
