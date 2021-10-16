# 1. 循环语法 for classnm in servantClassList :
# 2. 循环体内需要缩进(可以是一个空格),这块没有java严谨
# 3. 使用函数是看不到系统描述(类似于javadoc的东西)

# 循环写法类似于java  for (String nm : List)即执行循环又定义当前循环变量,注意句尾冒号
# 循环体内需要缩进,结束后处理删除缩进
# 由于没有括号保卫,这块很容易出现语法问题,需要特别注意
servantClassList = ['SABER','ARCHER','LANCER','RIDER','CASTER','ASSASSIN','BERSERKER']
print("每行都输出end")
for classnm in servantClassList :
  print(classnm)
  print("end")

print("\n循环结束后输入end")
for classnm in servantClassList :
  print(classnm)
print("end")

# 生成数字数组:range(START NUM,END NUM,STEP)STEP不设定默认为1
numList = list(range(1,11,3))
print(numList)
