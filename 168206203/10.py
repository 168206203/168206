# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 10:44:04 2018

@author: Yan
"""

'''
A：我没有偷钻石。
B：D就是罪犯。
C：B是盗窃这块钻石的罪犯。
D：B有意诬陷我
'''

number=1
for thief in ['A','B','C','D']:
    truth=(thief!='A')+(thief=='D')+(thief=='B')+(thief!='D')
    print("假设小偷是"+thief+"  说真话人数%d"%truth)    
    if truth==number:
      str=" 是小偷"
      print(thief+str)
          
      
      
      '''
   程序执行结果
假设小偷是A  说真话人数1
A 是小偷
假设小偷是B  说真话人数3
假设小偷是C  说真话人数2
假设小偷是D  说真话人数2
    '''
