# 1. Write a program that asks the user to enter a list of integers. Do the following:
# (a) Print the total number of items in the list.
# (b) Print the last item in the list.
# (c) Print the list in reverse order.
# (d) Print Yes if the list contains a 5 and No otherwise.
# (e) Print the number of fives in the list.
# (f) Remove the first and last items from the list, sort the remaining items, and print the
# result.

def ex1():
    list1 = eval(input('Enter a list of integers: '))
    print(list1)
    print(len(list1))
    print(list1[-1])
    print(list1[::-1])
    if 5 in list1:
        print('Yes')
    else:
        print('No')
    print(list1.count(5))
    list1.pop(list1[-1])
    list1.pop(list1[0])
    list1.sort()
    print(list1)



# 2. Write a program that generates a list of 20 random numbers between 1 and 100.
# (a) Print the list.
# (b) Print the average of the elements in the list.
# (c) Print the largest and smallest values in the list.
# (d) Print the second largest and second smallest entries in the list
# (e) Print how many even numbers are in the list.


def ex2():
    li = []
    count = 0
    for i in range(20):
        li.append(randint(1, 100))
    print(li)
    print(sum(li)/len(li))
    print(min(li), max(li))
    li.sort()
    print(li[1], li[-2])
    for i in li:
        if i % 2 == 0:
            count += 1
        else:
            pass
    print(count)

# 3. Start with the list [8,9,10]. Do the following:
# (a) Set the second entry (index 1) to 17
# (b) Add 4, 5, and 6 to the end of the list
# (c) Remove the first entry from the list
# (d) Sort the list
# (e) Double the list
# (f) Insert 25 at index 3
# The final list should equal [4,5,6,25,10,17,4,5,6,10,17]

def ex3():
    li = [8,9,10]
    li[1] = 17
    for o in [4,5,6]:
        li.append(o)
    li.pop(0)
    li.sort()
    li = li*2
    li.insert(3,25)
    print(li)

# 6. Create the following lists using a for loop.
# (a) A list consisting of the integers 0 through 49
# (b) A list containing the squares of the integers 1 through 50.
# (c) The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.

def ex6():
    l1 = []
    l2 = []
    l3 = []
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0,50):
        l1.append(i)
    print(l1) 
    for i in range(1,51):
        l2.append(int(m.pow(i,2)))
    print(l2) 
    for i in s:
        l3.append(s[s.index(i)]*(s.index(i)+1))
    print(l3)


# 7. Write a program that takes any two lists L and M of the same size and adds their elements
# together to form a new list N whose elements are sums of the corresponding elements in L
# and M. For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13].


def ex7():
    l = [1,2,3,4,5,6,7,8,9]
    n = [9,8,7,6,5,4,3,2,1]
    k = []
    for i in range(len(l)):
        k.append(l[i-1]+n[i-1])
    print(k)

# 8. Write a program that asks the user for an integer and creates a list that consists of the factors
# of that integer.

def listFactors():
    num = eval(input('Enter an integer: '))
    li = []
    for i in range(1,num+1):
        if num % i == 0:
            li.append(i)
        else:
            pass
    print(li)

# 13. Write a program that removes any repeated items from a list so that each item appears at most
# once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].

def removerepitition():
    li = [1,2,3,4,5,6,7,8,9,0,4,7,2,8,99,1,23,56,9,8,5,1,2,6,2,15,19]
    li.sort()
    print(li)
    for i in li:
        if li.count(i) > 1:
            for a in range(li.count(i)-1):
                li.pop(i)
    print(li)
removerepitition()