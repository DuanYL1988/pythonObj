#=======================================================================

#=======================================================================

class File():

  def __init__(self,path,name,encode):
    self.location = path + name
    self.encode = encode

  def readFile(self):
    with open(self.location,mode='r',encoding=self.encode) as fileObj:
      contents = fileObj.read()
      print(contents)

  def readLine(self):
    contents = []
    with open(self.location,mode='r',encoding=self.encode) as fileObj:
      for line in fileObj:
        contents.append(line.rstrip())

    return contents


file = File("D:\\project\\myapp\\src\\main\\webapp\\WEB-INF\\views\\html\\","album.html","utf-8")
contents = file.readLine()
print(type(contents) == "list")
