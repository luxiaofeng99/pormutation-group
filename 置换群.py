# -*- coding: utf-8 -*-
"""
@author: luxiao

本程序介绍了置换群的操作
"""
import numpy as np
#******************************************************************************
def trans(X,T):     #  原群是X，按照T置换；T满足第一位最小。例子，(1 4 6 2)
    K = X.size
    R = np.zeros([K],dtype = int)        #R是要返回的
    #************************开始换********************************************
    for i in range(1,K+1):
        if i in T:            
            if i == T[-1]:                
                R[(T[-1]-1)] = X[T[0]-1]
            else:
                temp1 = np.argwhere(T == i) #返回值是[[],[]]这样子的
                temp2 = T[temp1[0][0]]      # T[0]
                temp3 = T[temp1[0][0] + 1]  # T[1]
                R[ temp2-1 ] = X[ temp3-1 ]      
        else:
            R[i-1] = X[i-1]
    return R                            #置换结束，输出R
#******************************************************************************
def How_many_order(A):  #计算一个置换后的A，它的阶是多少？
    Long    = len(A)                                # A = 9 7 1 3 …… m
    Tra     = np.zeros((Long,Long),dtype = 'int')   #    [1 0 0 0 …… 0][2 …… 0]……[n …… 0]
    for i in range(Long):
        for j in range(Long):
            if j == 0:
                Tra[i][j]  = i+1   
            elif A[i] == i+1:   
                break
            else:
                if A[Tra[i][j-1]-1] == i+1:
                    break
                else:
                    Tra[i][j]  = A[Tra[i][j-1]-1]
                    #**********************************************************
    num = np.zeros((Long),dtype = 'int')
    for i in range(Long):
        num[i] = np.count_nonzero(Tra[i])
    #*************
    def L_C_M(A1,A2):       #时间紧张，最大公约数用穷举法
        L = min(A1,A2)        
        for i in range(L):
            if A1%(L-i) == 0 and A2%(L-i) == 0:
                return A1*A2/(L-i)
                break            
    #*************
    Order = 1
    for i in range(Long):
        Order = int(L_C_M(Order, num[i]))
    return Tra,Order
#**************************   计算 下面的群有几阶  *****************************
F1 = np.array([10,15,4,17,20,11,12,9,18,1,5,6,13,14,3,16,7,8,19,2])
print('*'*40)
print(How_many_order(F1)[1])
print('*'*40)
#*************      举例子    如何把21阶群嵌入到S7当中      ********************
def match_A(A):
    S = str(A)
    R = 0
    for i in range(1,7+1):
        if (str(i) in S):R=R+1
    if R == 6:        
        return True
    else:
        return False            
#************************                           ***************************
def match_1234567(A):
    S = (A)
    for i in range(7):
        if ( S[ (i+1)%7 ] - S[i] +7)%7 == 1:
            pass
        else:
            return False
    return True
#**********************                           *****************************
F1 = np.array([1,2,3,4,5,6,7])
for AA in range(123455,166463):
    if match_A(AA):
        S = str(AA)
        F6   = np.array([int(S[0]),int(S[1]),int(S[2])])
        F7   = np.array([int(S[3]),int(S[4]),int(S[5])])
        for i in range(3):        # 检测T是否正确
            if (F6[0] <= F6[i]) and  (F7[0] <= F7[i]) :
                pass
            else:
                continue
        Temp = np.array([1,2,3,4,5,6,7])
        for i in range(1):
            Temp = trans(Temp,F6)
            Temp = trans(Temp,F7)  
        for j in range(1):        
            Temp = trans(Temp,F1)
        for i in range(2):
            Temp = trans(Temp,F6)
            Temp = trans(Temp,F7)
        if match_1234567(Temp):
            pass
            print('******bingo***********',F6,'***',F7,'***',Temp)
#*************************************四元数群-Q8-H8*************************** 
F1   = np.array([1,2,3,4,5,6,7,8])
F2   = np.array([1,2,3,4])
F3   = np.array([5,6,7,8])

F4   = np.array([1,5,3,7])
F5   = np.array([2,8,4,6])

Temp3 = np.array([1,2,3,4,5,6,7,8])
print(Temp3)
for i in range(1):
    Temp3 = trans(Temp3,F3)
    Temp3 = trans(Temp3,F2)
    for j in range(1):
        Temp3 = trans(Temp3,F4)
        Temp3 = trans(Temp3,F5)
        print(Temp3)
#*************************************     End      ***************************