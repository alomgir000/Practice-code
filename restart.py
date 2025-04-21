'''
#class-1
print("Hbvghfvgfdh")
print(type("fhvghdhjv"))
print(type(54))

a=657756
print(a)
print(type(a))

#int float double  bool

a=10
print(type(a))
a=1.0
print(type(a))
a="10"
print(type(a))
a=True
print(type(a))
a=False
print(type(a))

#list dict tuple set

list1=[1,2,3,4,5,6]
print(type(list1))

dict1={
    "name":"alomghir hossain",
    "roll":20
}
print(dict1)
print(type(dict1))


tuple1=(1,2,3,4,5,67)
print(tuple1)
print(type(tuple1))


set1={2,4,56,6,7,6,76,8}
print(set1)
print(type(set1))



# list explain 
list1=[1,3,4,5,6,76]
print(list1)
print(list1[3])
print(list1[2:5])
print(list1[1:6:2])
print(list1[-1:-4:-1])
print(list1.index(4))

#list convert
list2=[1,2,3,4]
list3=list(list2)
print(list3)

list2=[1,2,3,4]
list2.append(34)
list2.insert(1,3)
list2.remove(2)
list2.pop(3)
list2.clear()
print(list2)

list4=[2,4,879,65,4]
list4.sort()
print(list4)
list4.reverse()
print(list4)

list1=[1,2,4,5]
list2=[6,7,8,9]
list1.extend(list2)
print(list1)

list3=[1,3,3,5,7,88,9,7,7]
list3=set(list3)
print(list3)


#class-----2

dict1={
    "nmae":"alomghir",
    "roll":20
}
#print(type(dict1.values()))
print(dict1.keys())
print(dict1.values())
print(dict1["nmae"])
print(dict1.get("nmae"))
print(dict1.get("roll"))
nmae=dict1.pop("nmae")
print(nmae)

print(dict1.items())

dict1["nmae"]="modina" # addding
dict1["age"]=22
print(dict1)

dict1.update({
    "varsity":'FHGBVHD',
    "batch":106

})

print(dict1)

for x in dict1:
    print(x)

for x in dict1.values():
    print(x)
popitm=dict1.popitem()
print(popitm)

dict1.clear()
print(dict1)



#..........tuple....


a=(1,2,4,5,6,7,8)
c=(1,2,4,5,6,7,8)
b=list(a)
print(type(b))
b.append(10)
print(b)
print(a[2:4])
print(a[0])
print(a.index(4))
print(a.count(5))

a=a + c
print(a)
a=a * 2
print(a)

t=(1,4,9)
(t1,t2,*t3)=t
print(t1)
print(t3)



#set

s={"a","b","c","h"}
s.add("kk")
print(s)
s1={"a","bb","cs","hg"}
s.update(s1)
print(s)
s.pop()
s.clear()
s=s1.copy()
print(s)

set1={1,3,4,5,6,7}
set2={5,7,9,0,5}
set3=set1.union(set2)
print(set3)
set4=set1.difference(set2)
print(set4)
set5=set1.intersection(set2)
print(set5)


#string

name="my name is alomghir"
print(name)
print(name[0])
print(name.index("i"))
print(name[:5])
print(name.count("i"))
print(name.lower())
print(name.upper())
print(name.capitalize())
num=10
print("hwllo " , num)
name=name.replace('alomghir',"abia")
print(name)

num1="     hello"
print(num1.split())

#clas--------3

#operator 
a=10
b=20
sum=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b
power=a**b
print(sum)
print(sub)
print(mul)
print(div)
print(mod)
print(power)

#comparisom
==
!= NOT equal
> greather than
> less than
>= grather than or equal
<= less than or equal

# assignment operator 
=
+=
-=
*=
/=
//=
%/


# logical operator 
and 
or
not

# identity and membership
is 
in
is not
in not

# condition
a=10
if a==12:
    print("it is a")
elif a==0:
    print("not asign 0")
else:
    print("it is no a")


a=10
b=12
if a==10:
    print("a is 10")
    if b==12:
        print("b is 12")
    else:
        print("b is not 12")
else:
    if a==12:
     print("a is 12")
    else:
        print("a is not 12")

#class----------------4
# loop 

a="1232643278"
for i in a:
    print(i)



num1=int(input("enter number"))
if(num1>80):
    print("A+")
elif(num1>70):
    print("A")
else:
    print("fall")


num="1234565675"
i=0
while i<len(num):
    print(num)
    i+=1


for x in "12633":
    if x=="3":
        break
    print(x)


for x in "12633":
    if x=="3":
        continue
    print(x)
list1=["apple","mango","orange"]
for x in list1:
    print(x)
list1.append("Water")
print(list1)
print(x)


dict1={"name":"alom","roll":20}
for i in dict1.items():
    print(i)
    for j in i:
        print(j)

#List comprehensim

list2=[i for i in {"apple","apple","chery"} if i!="apple"]
print(list2)

list1=[x**2 for x in range(6) ]
print(list1)


list3=["apple","apple","chery"]
for i,j in enumerate(list3):
    print(i,j)


list4=["apple","orange","chery"]
list5=["mango","apple","water"]
for i,j in zip(list4,list5):
    print(i,j)

#next-------


#classs 5--------

#function

def func_name():
    print("hello functon")
    return "hello return"
var=func_name()
print(var)

global1="hello i am global"
def func_name():
    print(global1)
    l="hello i am loacl"
var=func_name()
print(l)
print(var)


global1="hello i am global"
l="hello i am loacl"
def func_name():
    print(global1)
  
var=func_name()
print(l)
print(var)


def num_numver(a,b):
    sum=a+b
    print(sum)
result=num_numver(10,20)
print(result)


def num_numver(*arg):
    return sum(arg)
result=num_numver(10,20,6,99)
print(result)


def my_function(**kwargs):
    return(kwargs)
result=my_function(name="alom",age="22")
print(result)

#lamda function
sum=lambda a,b:a+b
print(sum(10,20))


sum_lambda= lambda *args,: sum(args)
print(sum_lambda(10,20))


sum_lambda= lambda *args,**kwargs:(sum(args) ,kwargs) 
print(sum_lambda(10,20,a=22,b=44))


'''

#decorator--------------------------


#hello
a=20%2
print(a)

#recursion------------



