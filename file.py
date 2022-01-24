# import os
#
# f=open('myFile.txt','w')
# print(f.name)
# f.write("hello")
# f.close()
#
# f=open("myFile.txt",'r')
# print(f.read())
# f.close()
#
# #конструкция with as, close не нужен
# with open("myFile.txt",'r') as f:
#     print(f.read())
#
# #подключение os
#     print(os.path.exists("myFile.txt")) #Существует ли файл
#     print(os.path.exists("С:\\myFile.txt"))
#
#     print(os.path.isfile("С:\\myFile.txt"))  #проверка существования файла,или это папка
#
#     #новый
# try:
#     with open("myFile.txt") as f:
#         print("file is open")
# except:
#     print('no open')
#
#     #копирование файла
# import shutil
# shutil.copyfile("С:\\myFile.txt","С:\\myFile11.txt")#копирование из одного файла в другой.должны оба существовать
# shutil.copy("С:\\myFile.txt","С:\\folder")#копирование из вайла в папку
#
# #размер файла
# print(os.path.getsize("С:\\myFile.txt"))
#
# #seek на практике не встречается
# with open("С:\\myFile.txt")as f:
#     f.seek(0,os.SEEK_END)
#     print(f.tell())
#
#     #переименовать файл
# os.rename("С:\\myFile.txt","С:\\myFile1111.txt")
#
# #очистка файла
f = open("test.txt",'w+')
f.write('something string')
f.seek(0)
f.write('new string')
f.close()