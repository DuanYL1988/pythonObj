# ==================================================================
# 使用Pygal
# 1. 安装 python -m pip install --user pygal==1.7
# ==================================================================
import pygal
from random import choice

class Die():
    """初始化一个骰子"""

    def __init__(self):
        # 初始化
        self.numSide = list(range(1,7))

    def roll(self):
        return choice(self.numSide)


die1 = Die();
die2 = Die();

results = []
for roll_cnt in range(100):
  rst = die1.roll() + die2.roll()
  results.append(rst)

# 分析结果
frequencyList = []
xLable = []
for value in list(range(2,13)):
  frequency = results.count(value)
  frequencyList.append(frequency)
  xLable.append(str(value))

print(frequencyList)

# 可视化结果
hist = pygal.Bar()
hist.title = "2个骰子结果统计"
# 集合只能为str类型
hist.x_labels = xLable
hist.x_title = "result"
hist.y_title = "count"

hist.add("6+6",frequencyList)
hist.render_to_file("RST.svg");
