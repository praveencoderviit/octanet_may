i=0
while(i<10):
    i=i+1
    print(i)##1

for i in range(10):
    print(i)##2

number=[1,2,3,4,5]
for num in number:
    print(num)##3

colors=['pink','yellow','green']
print('yellow'in colors)
print('pink' not in colors)
print('red' in colors)##4

x=[1,2,3]
y=x
print(x is y)
print(x is not y)##5

for i in range(6):
    if(i==2):
        continue
    print(i)##6

for i in range(5):
    if(i==3):
        break
    print(i)##7
    
for i in range(5):
    if(i==2):
        pass
    print(i)##8

name='kommanapalli praveen'
print(name)
a=len(name)
print(a)
b=name[0]
print(b)
c=name[1:20:2]
print(c)##9

person={'name':'praveen','age':20,'city':'vizag'}
print(person)

phone=dict(brand='redmi',model=8,year=2019)
print(phone)

print(person['name'])
print(phone.get('model'))

person['age']=31
print(person)
phone['color']='blue'
print(phone)

person.pop('age')
print(person)
phone.pop('model')
print(phone)##10

def add(a,b):
    return a+b
print(add(2,3))

def add(a,b):
    print(a+b)
add(2,3)
add(5,5)##11

def wish(name,msg):
    print("hello",name,msg)
wish(name="praveen",msg="good morning")
wish(name="vignan",msg="good morning")##12

def add(*b):
    result=0
    for i in b:
        result=result+i
        return result
print(add(1,2,3,4,5))##13
#fibonnaci series
n=int(input("enter the no of fib:"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b ##14

#division of range
a=int(input("enter the start of range:"))
b=int(input("enter the start of end:"))
n=int(input("enter the divisor:"))
for i in range(a,b+1):
    if(i%n==0):
        print(i)##15
#right angle sysbols
n=5
for i in range(n,0,-1):
    print("*"*i) ##16
#sum of two min_num
a=float(input("enter the frist number:"))
b=float(input("enter the second number:"))
min_num=min(a,b)
print(min_num)##17
##two comparing string
s1=input("enter the string1:")
s2=input("enter the string2:")
if(s1==s2):
    print("both are equal")
else:
    print("both are not equal")##18
#using function even odd
def a(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")
print(a(4))
print(a(5))##19
#function with fac
def fac(n):
    if(n==1):
        return 1
    else:
        return n*fac(n-1)
print(fac(5))##20

def wish(name,msg):
    print(name='praveen',msg='good morning')
    wish()
    wish()##21


