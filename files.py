import os
import shutil

source="C:/Users/ME/Documents/abbas/whitehat prolects/images"
dist="C:/Users/ME/Documents/abbas/whitehat prolects/organizeImages"
#print(os.path.exists(source))
print(os.listdir(source))
list_of_files=os.listdir(source)

for i in list_of_files:
    name,extention=os.path.splitext(i)
    #print(name)
    if extention =="":
        continue
    if extention in ['.gif','.png','.jpg','.jfif','.jpeg' ]:
        path1=source+"/"+i
        path2=dist+"/"+"images_files"
        path3= dist+"/"+"images_files"+"/"+i

        if os.path.exists(path2):
            print("Moving "+i+".......")

            shutil.move(path1,path2)
        else:
            os.makedirs(path2)
            print("Moving "+i+".......")

            shutil.move(path1,path2)

