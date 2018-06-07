
'''
def say():
    print("a")

def f2(f):
    print(f)
    f()
f2(say)

'''

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
# for f in count():
#     print(f())


# def f(n):
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return f(n-1) +f(n-2)

# print(f(0))
# print(f(1))
# print(f(2))
# print(f(3))
# print(f(5))

# def f(n):
#     if n < 2 :
#         return n

#     else:
#         return f(n-1) + f(n-2)

# print(f(0))
# print(f(1))
# print(f(2))
# print(f(3))
# print(f(5))


# import tkinter
# top = tkinter.Tk()
# # 进入消息循环
# top.mainloop()


# a = [1,2,3,4,5]
# L = [x + 2 for x in a[0::2]]
# l = map(lambda x : x+2,a[0::2])
# print(a[0::2])
# print(sum(L))
# print(sum(l))

# l = [5,-2,1,3,6]
# l1 = sorted(l,key=abs)
# print(l)
# print(l1)

# l2 = l.sort()
# print(l2)
# print(l)




# def f(n):
#     if n == 1:
#         return 1 
#     if n == 2:
#         return 2
#     return f(n-1) + f(n-2)

# for i in range(1,10):
#     print(f(i))





# l1 = [5,8,3,4,7,9,2,2,5,4,1,3,9,6,3,2,7]
# l2 = []
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)


# d = {'A':1,'B':2,"C":3}
# d1 = {}

# for k,v in d.items():
#     print('键%s  值%s' % (k,v))

#     d1[v] = k

# print(d1)



# d = {'A':1,'B':2,"C":3}

# d1 = {'A':3,'K':9}

# d.update(d1)
# print(d)

# a = 1
# b = 2
# c = lambda a,b : a+b
# print(c)



# l = [1,2,3,4,5,6,7,8,9]
# s = filter(lambda x : x%2 !=0 ,l)
# for i in s:
#     print(i)


# def mynum(x):
#     if x > 0:
#         print(x,'是正数')
#         return x
#     else:
#         return x
#         print(x,'是负数')
# print(mynum(1))
# print(mynum(-1))




# def myfn():
#     def myfn2():
#         print('My Python')
#     return myfn2()
# print(myfn())


# l = [1,2,3,4]
# l1 = [str(x) for x in l]
# print(l1)
# print('l = '+ '*'.join(l1))


# import time
# def myfn(n):
#     if n == 0:
#         return
#     time.sleep(1)
#     print('hello world')
#     return myfn(n-1)
# myfn(5)


# import random
# l = ['A','B',1,2,3,4,5,6,7,8,9]
# l1 = []
# def f(n):
#     global l1
#     for i in range(n):
#         s = random.choice(l)
#         print(s)
#         l1.append(s)
#     return l1
# print(f(5))



# class Hotel:
#     def __init__(self,room,cf,br):
#         self.room = room
#         self.cf = cf
#         self.br = br 

#     def amount(self,days):
#         return (self.room * self.cf + self.br)*days

# H1 = Hotel(room = 200 , cf = 1.0 , br = 15)

# print(H1.amount(3))


# s2 = 'Hello Tarena'
# f = open('./tarena.txt' , 'wb')
# f.write(s2.encode())
# print(f.tell())
# print(f.seek(0,0))
# s = f.read(5)
# print(s)
# print(f.tell())


# s = 'welcom to 中国'
# s1 = s.encode('utf-8')
# print(s)
# print(s1)   


# b = b'Python\xe7\x89\x9bX'
# b1 = b.decode('utf-8')
# print(b1)


# D = [{"name": "Green","age": 30},{"name": "Bob","age":25}]

# D1 = sorted(D , key = lambda x:x['age'],reverse = True)
# print(D1)


# from django.contrib.auth.hashers import make_password ,check_password

# print(make_password('123456','python','pbkdf_sha1'))
# print(make_password('123456','abcdef','pbkdf_sha1'))
# print(make_password('123456',None,'pbkdf_sha1'))
# print(make_password('123456',None,'pbkdf_sha1'))
# print(make_password('567891',None,'pbkdf_sha1'))
# print(make_password('567891','python','pbkdf_sha1'))

# import threading

# def f():
#     while True:
#         pass
# if __name__ =='__main__':
#     t = threading.Thread(target = f)
#     t.start()

#     while True:
#         pass


# s = 'ABC'
# b = bytes('ABC',encoding='utf-8')
# # s.encoding = 'utf-8'


# print(b)
# print(type(b))
# print(b.decode('utf-8'))
# print(b.decode())
# print('************************************')
# print(s.encode())
# print(s.encode('utf-8'))
# # print(s.encoding)

# def Fn(n):
#     l = []
#     for i in range(n):
#         y = 0
#         s = bin(i)
#         for x in s :
#             print(x)
#             if x == '1':
#                 y += 1
#         l.append(y)

#     return l 
# print(Fn(10))


# y = 0
# for x in range(10):
#     while x != 0:
#         if x % 2 !=0:
#             y += 1
#         x = x%2

# print(y)



# def say_hello():
#     print('hello world')

# def f2(f):
#     print(f)
#     print(id(f))
#     f()

# f2(say_hello())
# f2(say_hello)



# fib = lambda n: n if n < 2 else fib(n-2) + fib(n - 1) #lambda返回的是一个函数关系。绑定到fib上。
# for i in range(1,20):
#    print(fib(i))


# mit = map(lambda x:x**2 ,range(10))
# print(mit)
# l = [x for x in mit]
# print(l)


# l = [1,2,3,3,4,8,9]
# l1 = [i for i in l if l.count(i) == 2]
# l2 =list(set(l1)) 
# print(l2)

# # random模块中的shuffle(洗牌函数)  
# import random  
# alist = [1, 2, 3, 4]  
# random.shuffle(alist)     
# print(alist)  


# #From list to Tuple                   
# tuple(a_list)     
  
# #From Tuple to List  
# def to_list(t):   
# return [i if not isinstance(i,tuple) else to_list(i) for i in t]

# # collapse是一个开关： 1表示打开紧凑的效果；0维持原样显示；
# s = 's df fed'
# key = int(input('是输入0或1:'))
# print(bool(key))
# # print("".join(s.split()))
# processFun = bool(key) and (lambda s:"".join(s.split())) or (lambda s:s)
# print(processFun(s))



# 答:可以使用sub()方法来进行查询和替换，sub方法的格式为：sub(replacement, string[, count=0]) 
# replacement是被替换成的文本 
# string是需要被替换的文本 
# count是一个可选参数，指最大被替换的数量

# s = ''
# s1 = " ab c d  ef "
# for i in s1:
#     if i !=' ':
#         s += i
# print(s)


# s1 = " ab c d  ef "
# s = s1.split(" ")
# print(s)
