squares=[]
for i in range(1,11):
    squares.append(i**2)
print(squares)

square2=[i**2 for i in range(1,11)]
print(square2)

negative=[]
for i in range(1,11):
    negative.append(-i)
print(negative)

new_negative=[-i for i in range(1,11)]
print(new_negative)

name=['Astha','Ravita','Mukul']
new_list=[]
for names in name:
    new_list.append(names[0])
print(new_list)


new_list=[names[0] for names in name]
print(new_list)



'''exercise 1'''

# define a function that take list of string
# list containing reverse of every string

def listofstring(l):
    new_list=[reverse_list[::-1] for reverse_list in l]
    print(new_list)
    
l=['abc','pqr','lmn']
listofstring(l)

def listofstring(l):
    new_list=[]
    for name in l:
        new_list.append(name[::-1])
    return new_list
    
l=['abc','pqr','lmn']
print(listofstring(l))

#list comprehension with if statement

numbers=list(range(1,11))
[1,2,3,4,5,6,7,8,9,10]
nums=[]
for number in numbers:
    if number%2==0:
        nums.append(number)
print(nums)

even_nums=[number for number in numbers if number%2==0]
print(even_nums)
even_nums2=[number for number in range(1,21) if number%2==0]
print(even_nums2)
odd_nums=[number for number in numbers if number%2!=0]
print(odd_nums)

#list comprehension with if else

nums=[1,2,3,4,5,6,7,8,9,10]
new_list=[]
for i in nums:
    if i%2==0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(new_list)


new_list2=[i*2 if (i%2==0) else -i for i in nums]
print(new_list2)

#list comperehension in nested list

# example=[[1,2,3],[1,2,3][1,2,3]]
nested_comp=[  [i for i in range(1,4)]  for j in range(3)  ]
print(nested_comp)