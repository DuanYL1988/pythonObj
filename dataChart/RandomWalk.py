import matplotlib.pyplot as plt

from random import choice

class RandomWalk():
    """一个生产随机漫步数据的类"""

    def __init__(self,numPoint=5000):
        # 初始化
        self.numPoint = numPoint

        # 设置原点
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """计算漫步所有点"""

        while len(self.x_value) < self.numPoint:
            # 方向,水平方向前进或后退
            x_direction = choice([1,-1])
            # 移动距离,0为只在垂直方向移动
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            # 不允许(0,0)不移动
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的坐标
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)

while True:
  rw = RandomWalk()
  rw.fill_walk()

  pointCnt = list(range(rw.numPoint))

  #plt.plot(rw.x_value,rw.y_value,lineWidth=1)

  plt.scatter(rw.x_value,rw.y_value,c=pointCnt,cmap=plt.cm.Blues,
    edgecolor='none',s=5)

  # 突出起点和终点
  plt.scatter(0,0,c='green',edgecolor='none',s=20)
  plt.scatter(rw.x_value[-1],rw.y_value[-1],c='red',edgecolor='none',s=20)
  plt.show()

  keepRunning = input("try again?(y/n) :")
  if keepRunning == 'n':
    break
