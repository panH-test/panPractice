#@Author:Hanpan
#@Time:2022/3/28  10:44
#@File:test0328.py

# with open('test.txt',encoding='utf-8') as f:
#     for i in f:
#         print(i,end=' ')
# import random
#
# print(random.randint(1,3))

# ces = float(input('please input ceswendu:'))
# hus = (ces*1.8)+32
# print(f"hus is:{hus}")
# a,b = 1,2
# a,b = b,a
# print(a,b)
# b=2
# while b>1:
#     a = int(input('please input a number:'))
#     if (a % 2) == 0:
#         print(f"{a}:no")
#     else:
#         print('is')

# a = int(input('min:'))
# b = int(input('max:'))
# if a>0:
#     for i in range(a,b):
#         if (i%2)!=0:
#             print(i)
#         # else:
#         #     continue
# else:
#     print('please input intnumber')
#
# for i in range(1,10):
#     for x in range(1,i+1):
#         print("{}X{}={}".format(x,i,i*x),end=' ')
#     print('')

# a = int(input('num:'))
# print('二进制：',bin(a),'八进制：',oct(a),'十六进制:',hex(a))

# import calendar
# import datetime
#
#
# today = datetime.date.today()
# oneday = datetime.timedelta(days=1)
# yest = today - oneday
# print(yest)
# year = int(input('year'))
# month = int(input('month'))
#
# print(calendar.month(year,month))


#30人，留15，数到9下船

# people={}
# for x in range(1,31):
#     people[x]=1
# print(people)
# check=0
# i=1
# j=0
# while i<=31:
#     if i == 31:
#         i=1
#     elif j == 15:
#         break
#     else:
#         if people[i] == 0:
#             i+=1
#             continue
#         else:
#             check+=1
#             if check == 9:
#                 people[i]=0
#                 check = 0
#                 print("{}号下船了".format(i))
#                 j+=1
#             else:
#                 i+=1
#                 continue

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
driver.find_element_by_link_text('hao123').click()
print(driver.title)
print(driver.current_url)
driver.set_window_size(600,200)
print(driver.get_window_size())
# driver.quit()
