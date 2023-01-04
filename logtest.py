import datetime
import os
import shutil

# 创建文件
logfile= open('test1.txt',"w",encoding='utf-8')
logfile.write('Wu Sunjie')
logfile.write('something test')
logfile.write('information retrieval systems\n')
logfile.close()

with open(r'test1.txt',"r",encoding='utf-8') as one:
 t=one.readline()
 print(t)
logfile.close()

with open("test1.txt", "a") as two:
 two.write("ok.good!\n")


# 移动文件
shutil.copy("test1.txt","test1.txt.bak") 
shutil.move("test1.txt","movetest1.txt")

# 删除文件
os.remove('movetest1.txt')