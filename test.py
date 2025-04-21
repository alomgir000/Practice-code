# print("fhgvhdbvg")
# a=39
# print(a)

#int float double  bool
'''
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



#dict

dict1={
    "name":'alom',
    'rol':20
}

print(dict1.values())
print(dict1.keys())
print(dict1.get("name"))

for i in dict1:
    print(i)
for i in dict1.values():
    print(i)
for i in dict1.keys():
    print(i)

dict1["age"]=22
print(dict1)

dict1.update({
    "gpa":3.90
})
print(dict1)

dict1.pop("gpa")
dict1.clear()
print(dict1)


#tuople 

a=(1,2,4,5,6,7,8)
c=(1,2,4,5,6,7,8)
b=list(a)
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

a=('a','b','c')
(t1,t2,*t3)=a
print(t1)
print(t3)

x=('a','b','c')
(a,b,*c)=x
print(a)
print(b)
print(c)


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

'''