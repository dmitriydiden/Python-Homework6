'''
41. Напишите программу вычисления арифметического выражения заданного строкой. 
Используйте операции +,-,/,*. приоритет операций стандартный.
*Пример:*
1+2*3 => 7;
1-2*3 => -5;
- Добавьте возможность использования скобок, меняющих приоритет операций.
*Пример:*
1+2*3 => 7;
(1+2)*3 => 9;
'''
calc = '1+2*3'
list = []
for i in calc:
    list.append(i)

list1 = []
list2 = []

def calculator(lst, cl):
    k=0
    n=0
    while lst[k] != '(':
        k=k+1
        if k == len(lst):
            break
   
    if k == len(lst):
        for i in range(len(lst)):
            if lst[i] == '*' or lst[i] == '/':
                n=i
                for j in range(i-1, i+2):
                    list1.append(lst[j])
                if n ==1:
                    list2.append(lst[3])
                    list2.append(lst[4])
                else:
                    list2.append(lst[1])
                    list2.append(lst[0])
    else:
        for i in range(k+1, k+4):
            list1.append(lst[i])
        if k==0:
            list2.append(lst[k+5])
            list2.append(lst[k+6])
        else:
            list2.append(lst[1])
            list2.append(lst[0])
    res1 = 0
    for i in list1:
        if i == '+':
            res1 = int(list1[0])+int(list1[2])
        if i == '-':
            res1 = int(list1[0])-int(list1[2])
        if i == '*':
            res1 = int(list1[0])*int(list1[2])
        if i == '/':
            res1 = int(list1[0])/int(list1[2])
            
    for i in list2:
        if i == '+':
            res = res1+int(list2[1])
        if i == '-':
            if n==1:
                res = res1-int(list2[1])
            else:
                res = int(list2[1])-res1
        if i == '*':
            res = res1*int(list2[1])
        if i == '/':
            res = res1/int(list2[1])
    print(f"{cl} = {res}")
    return list1
    return list2
    return res
calculator(list, calc)
