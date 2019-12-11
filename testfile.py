import os
print(os.path.isfile('./SAVE.txt'))
f = open("SAVE.txt","r+")
str1 = f.readline().split()

str2 = f.read().split()

print(str2)
b= []
c= []
b= [[int(str1[i]), int(str1[i+1])] for i in range(0,len(str1)-1,2)]
c = [[int(str2[i]), int(str2[i+1])] for i in range(0,len(str2)-1,2)]
print (b)
print(c)