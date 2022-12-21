#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#Author: zhangyawei


"""
## 邮局选址

在一个按照东西和南北方向划分成规整街区的城市里，n个居民点散乱地分布在不同的街区中。用x坐标表示东西向，用y坐标表示南北向。各居民点的位置可以由坐标(x,y)表示。街区中任意2点(x1,y1)和(x2,y2)之间的距离可以用数值|x1-x2|+|y1-y2|度量。
居民们希望在城市中选择建立邮局的最佳位置，使n个居民点到邮局的距离总和最小。

### 输入数据

第1行是居民点数n，1≤n≤10000。接下来n行是居民点的位置，每行2个整数x和y，-10000≤x，y≤10000。

### 输出数据

1个数，是n个居民点到邮局的距离总和的最小值。

#### 示例

输入：

> 5
> 1 2
> 2 2
> 1 3
> 3 -2
> 3 3

输出：

> 10
"""

n = int(input())

x_list = []
y_list = []

for i in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    x_list.append(x)
    y_list.append(y)

minx = 999999
miny = 999999
min_sum = 999999
for i in range(n):
    sumx = sumy = 0
    for j in range(n):
        sumx += abs(x_list[i]-x_list[j])
        sumy += abs(y_list[i]-y_list[j])
    if sumx < minx:
        minx = sumx
    if sumy < miny:
        miny = sumy

print(minx + miny)