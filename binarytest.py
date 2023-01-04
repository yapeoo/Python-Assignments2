import os
import shelve
import shutil

studentinfo1={'name':'Wu Sunjie','sex':'Male','Country':'China','City':'GuiLin'}

with shelve.open('test2.bin') as fp: 
    fp['1']=studentinfo1  
    print(fp['1'])


shutil.copy("test2.bin.dat","test2.bin")
shutil.move("test2.bin.dat","movetest2.bin")

os.remove('test2.bin')