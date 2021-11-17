#import os module which provides a protable way of using operating system 
import os
#import shutil module which helps in automating process of copying and removal of files or directory
import shutil
#using try and except block we can handle any error if it occurs
try:
    #creating methods of organizing
    def category():
        #listing file types
        image_formats = ["jpg","png","jpeg","gif","webp","tiff","psd","eps","raw","bmp"]
        audio_formats =["mp3","wav","aac","dsd"]
        video_formats = ["mp4","avi","webm","mkv","mov"]
        docs_formats = ["ai","pdf","txt","ppt","doc","docx","xls","html","htm","odt","pptx","xslx","py","c","ipynb"]
        application =["exe"] 

        #making directories in destination folder
        Dest_dirs = ["music","videos","documents","others","images","softwere"]
        for d in Dest_dirs:
            dir_path = os.path.join(Dest_path,d)
            if not os.path.isdir(dir_path):
                    os.mkdir(dir_path)

        #listing all files
        files = os.listdir(src)

        #traversing all files 
        for file in files:
            filename,extention = os.path.splitext(file) #splitting extention
            extention = extention[1:] 

            if extention in image_formats:
                shutil.move( src+'/'+file,Dest_path+'/'+'images'+'/'+file)
            elif extention in video_formats:
                shutil.move( src+'/'+file,Dest_path+'/'+'videos'+'/'+file)
            elif extention in audio_formats:
                shutil.move( src+'/'+file,Dest_path+'/'+'music'+'/'+file)
            elif extention in docs_formats:
                shutil.move( src+'/'+file,Dest_path+'/'+'documents'+'/'+file)
            elif extention in application:
                shutil.move( src+'/'+file,Dest_path+'/'+'softwere'+'/'+file)
            else:
                shutil.move( src+'/'+file,Dest_path+'/'+'others'+'/'+file)

    def Ext():
        # listing all files
            files = os.listdir(src)
        #traversing all files 
            for file in files:
                filename,extention = os.path.splitext(file) #splitting extention
                extention = extention[1:] 
        #moving files based on extention if directory exists
                if os.path.exists(Dest_path +'/'+extention):
                    shutil.move(src+'/'+file,Dest_path+'/'+extention+'/'+file)
        #if directory doesn't exists make directory then move file
                else :
                    os.makedirs(Dest_path +'/'+extention)
                    shutil.move(src+'/'+file,Dest_path+'/'+extention+'/'+file)

    #getting path input from user in which we want to organize files
    src=input(r'enter source path :')
    Dest_path = input(r'enter destination path : ')
    #Getting choice from user
    print('By which method want to Organize file')
    print('1. By Category \n2. By Extention ')
    choice = int(input("Enter your choice : "))

    if (choice == 1):
        category()
    elif(choice == 2):
        Ext()
    else:
        print('invalid choice')
except Exception as e:
    print('ops!! An error has been occurred.')
  #  print(e)
else:
    print('successfully executed \U0001F600')