print("Hello World!")

# // this is comment
# /* 
# this is a line of comments
# */

# this is a comment
'''
this is a line 
this is another line of comments
'''

x=100
x="hello"
x=[1,2,3]
print(x)

x=100
y=10
result=x//y
print(result)
print(int(x/y))

min_value=min(1,2,3)
print(min_value)
raised=pow(2,3)
print(raised)
raised=2**3
print(raised)

x=-1
y=0
if x<0:
    print("x is negative")
    y+=1
elif x>0:
    print("x is positive")
else:
    print("x is zero")

start=10
end=100

if x>start and x<end:
    print("x is within range")

if x<start or x>end:
    print("x is not in range")

count=0
while count<5:
    print(count)
    count+=1

for i in range(1,15,2):
    print(i, end=" ")
print()

lst=[2,4,6,8]
for i in range(len(lst)):
    print(i,lst[i])

for val in lst:
    print(val, end=" ")
print()

for index,value in enumerate(lst):
    print(index,value)

def hello_world():
    print("Hello World!")
hello_world()

def hello(name):
    print("Hello "+name)
hello("Bob")

def hello2(name="Bob"):
    print("Hello "+name)
hello2()
hello2("Jane")

hello="hello"
for c in hello:
    print(c)

course="Platform Computing"
plat=course[:8]
computing=course[9:]
print(plat)
print(computing)