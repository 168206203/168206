# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 11:09:14 2018

@author: Yan
"""

'''
A：我没有偷钻石。   [1,0,0,0]
B：D就是罪犯。    [0,0,0,-1]
C：B是盗窃这块钻石的罪犯。[0,-1,0,0]
D：B有意诬陷我。 [0,0,0,1]
分析有两个人说的是真话，编程序判断谁偷走了钻石。
'''
N=2 #说真话人数
Talk=[[1,0,0,0],[0,0,0,-1],[0,-1,0,0],[0,0,0,1]]
Truth_num=0 
for thief in ['A','B','C','D']: 
    for i in Talk:
        for j in range(len(i)):
            if i[j]==1:
                if thief!=chr(65+j):
                    Truth_num=Truth_num+1
                    print(chr(65+j)+"说的是真话")
            if i[j]==-1:
                if thief==chr(65+j):
                    Truth_num=Truth_num+1
                    print(chr(65+j)+"说的是真话")
      
    print("假设小偷是:"+thief+"  说真话人数:%d" %Truth_num )
    print()
    if N==Truth_num:
        str = thief + "是小偷！"
        print(str)
        print("---------------------------")
    Truth_num=0
 

       
    '''
    程序执行结果
D说的是真话
假设小偷是:A  说真话人数:1

A说的是真话
B说的是真话
D说的是真话
假设小偷是:B  说真话人数:3

A说的是真话
D说的是真话
假设小偷是:C  说真话人数:2

C是小偷！
---------------------------
A说的是真话
D说的是真话
假设小偷是:D  说真话人数:2

D是小偷！
---------------------------
   '''
 
