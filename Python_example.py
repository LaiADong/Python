#


'''
#Example1

#An example of two numbers addition
print("\n\t<计算两个数的和>\n")
sNum1 = input("请输入第一个数字：\n")
sNum2 = input("请输入第二个数字：\n")

fSum = float(sNum1) + float(sNum2)
print(fSum)
print("数字 {0} 和数字 {1} 相加结果为： {1} ".format(sNum1, sNum2, fSum))
'''



'''
#Example2

#An example of square 
import math

print("\n\t<计算平方根>\n")
sNum = input("请输入数字\n")

fResult1 = math.sqrt(float(sNum))
fResult2 = float(sNum) ** 0.5  #另外一种计算方式


print("1:数字 {0} 的平方根为 {1} ".format(sNum, fResult1))
print("2:数字 {0} 的平方根为 {1} ".format(sNum, fResult2))

'''

'''
#Example3

#An example of generating random numbers 
import random
print("生成10个【0-9】的随机数:", random.sample(range(100), 10))
'''

'''
#Example4

#An example of two values swap
iVal1 = int(input("请输入第一个数字："))
iVal2 = int(input("请输入第二个数字："))

iVal1 = iVal1 ^ iVal2
iVal2 = iVal1 ^ iVal2
iVal1 = iVal1 ^ iVal2
print("交换后，第一个数字为 {0} 第二个数字为 {1}".format(iVal1, iVal2))

'''
#Example4

#An example of check the string
"""
while True:
    sString1 = input("请输入任意字符串，回车结束\n")
    if(sString1.isalpha()):
        print("该字符串仅包含字母")
    elif(sString1.isdigit()):
        print("该字符串仅包含数字")
    else:
        print("复合字符串")
"""
"""
#Example5

#An example of check the string


import sys 


def is_number(sString):
    try:
        print(sys._getframe().f_lineno)
        float(sString)
        print(sys._getframe().f_lineno)
        return True
    except ValueError:
       print(sys._getframe().f_lineno)
       pass

    try:
        import unicodedata
        print(sys._getframe().f_lineno)
        unicodedata.numeric(sString)
        print(sys._getframe().f_lineno)
        return True
    except (TypeError, ValueError):
        print(sys._getframe().f_lineno)
        pass        

    return False

print(is_number('3'), "\n====")

print(is_number('五'))
"""

"""
#Example6

#An example of check if the number is odd or even

while True:
    try:
        sInputString = input("请输入数字")
        iNum = int(sInputString)
    except (ValueError, TypeError):
        print("输入有误，请重新输入")
        continue
    if iNum & 0x01:
        print("数字 {0} 是奇数".format(iNum))        
    else:
        print("数字 {0} 是偶数".format(iNum))        

"""

"""
#Example6

#An example of check if the year is a leap year or nots
import calendar

while True:
    try:
        sInputString = input("请输入年\n")
        iNum = int(sInputString)
        #if iNum < 1970:
        #    raise ValueError
    except (ValueError, TypeError):
        print("输入有误，请重新输入")
        continue
    if calendar.isleap(iNum):
        print("{0} 是闰年".format(iNum))        
    else:
        print("{0} 是平年".format(iNum))      

    print("{0}".format(calendar.month_abbr(2010)))

"""
asd