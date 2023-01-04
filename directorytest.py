import os
import shutil

filedir=os.getcwd()
print(filedir)

path1="test3"
os.chdir("D:/")
os.mkdir(path1)
print('新的目录创建successfully!')  
f=open('D:/test3/testw.txt','w')
f.write('Hello Wu Sunjie!')
f.close()

listdir1=os.listdir(path1)
print("目录中包含文件和目录:",listdir1)

dsc = 'D:/test3/movetest.txt'
shutil.move("D:/test3/testw.txt","dsc")
print("移动后位置:")

path3="D:/test3"

os.rmdir(path3)
print('deleted successfully!')  