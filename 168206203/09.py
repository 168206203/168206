# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 22:28:04 2018

@author: Yan
"""

start='hit'
end='cog'

adict =[ 'hot','dot','dog','lot','log']
def OnewordDiff(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    if count == 1:
        return 1
    else:
        return 0

def find_path(start, end, adict):
    visited = []
    def loop(a, b, c,record=[]):#a 表示当前单词，b 表示目的单词，c 表示剩余单词
        for i in c:
            if OnewordDiff(a, i) and OnewordDiff(i, b): # i 表示字典选择单词，
                r=record.copy()
                r.append(a)
                r.append(i)
                r.append(b)
                visited.append([r,len(r)])
            if OnewordDiff(a, i) and not OnewordDiff(i, b):
                r = record.copy()
                r.append(a)
                c_copy = c.copy()
                try:
                    c_copy.remove(a)  
                except:
                    pass
                loop(i, b, c_copy, r)
    loop(start, end, adict)
    print(visited)
    return visited

find_path(start, end, adict)
visited=find_path(start, end, adict)
visited_path_length=[path_length for [r,path_length] in visited]#把所有路径长度组成新列表
words=min(visited_path_length)#计算最短路径长度
#print(visited_path_length)
print('最短路径为:')
for visited_a_path in visited:
    for i in range(len(visited_a_path)):
        if (visited_a_path[i]==words):
             print(visited_a_path)#输出最短路径
             
