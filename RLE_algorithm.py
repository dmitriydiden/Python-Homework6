'''
#42. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.
Sample Input 1:
aaaabbcaa
Sample Output 1:
a4b2c1a2
Sample Input 2:
abc
Sample Output 2:
a1b1c1
'''
string = input("Введите строку из прописных латинских букв:")
with open("file1.txt", 'a') as data:
    data.writelines(string)

list = []
str2=""
count = 1
for i in string:
    list.append(i)
for i in range(len(list)-1):
    if list[i] != list[i+1]:
        count+=1
if count == 1:
    str2 =str2 + str(list[0])+str(len(list))
count=1  
for i in range(len(list)):
     if i < len(list)-1:
        if list[i]==list[i+1]:
            count+=1
        else:
            str2 =str2 + str(list[i])+str(count)
            count=1
count=1
for i in range(len(list)-1, 0, -1):
    if list[i]==list[i-1]:
            count+=1
    else:
        str2 =str2 + str(list[i])+str(count)
        break
with open("file2.txt", 'a') as data:
    data.writelines(str2)
path = 'file2.txt'
data = open(path, 'r')
for line in data:
    print(f'{string}: {line}')
data.close()
