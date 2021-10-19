#=======================================================================
# 对象的概念在python中叫做字典,定义方式基本和json一样
# 1.即使知道属性名,也无法像js一样直接使用obj.attr;需要使用obj['attr']
# 2.删除属性 del obj['attr']
#=======================================================================
person = {'name':'Duan YL','age':31,'city':'Tokyo'}
print(person['name'])

del person['city']
print(person)

for key,value in person.items():
    print("key : "+ key + " , value : " + str(value))

person2 = {'name':'Duan Wh','age':58,'city':'Xuancheng'}

person_list = []
person_list.append(person)
person_list.append(person2)
print(person_list)
