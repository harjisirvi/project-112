import os
import shutil

source= "C:/Users/HARJI/Downloads"
destination= "C:/Users/HARJI/OneDrive/Documents/sjn"

list = os.listdir(source)






for f in list:
	name,extension=os.path.splitext(f)
	if extension=="":
		continue
	if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
		path1=source + "/" + f
		path2=destination + "/" + "image_file"
		path3=destination + "/" + "image file " + f

		if os.path.exists(path2):
			shutil.move(path1,path3)
		else:
			os.makedirs(path2)
			shutil.move(path1,path3)














