# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 13:12:32 2018

@author: Yan
"""

'''
A：我没有偷钻石。
B：D就是罪犯。
C：B是盗窃这块钻石的罪犯。
D：B有意诬陷我
分析有两个人说的是真话，编程序判断是谁偷走了钻石。
'''

number=2
for thief in ['A','B','C','D']:
    truth=(thief!='A')+(thief=='D')+(thief=='B')+(thief!='D')
    print("假设小偷是:"+thief+"  说真话人数:%d"%truth)    
    if truth==number:
      str=" 是小偷"
      print(thief+str)
          
      
      
      '''
   程序执行结果
假设小偷是:A  说真话人数:1
假设小偷是:B  说真话人数:3
假设小偷是:C  说真话人数:2
C 是小偷
假设小偷是:D  说真话人数:2
D 是小偷
    '''
