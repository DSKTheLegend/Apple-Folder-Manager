import os
import shutil
import datetime


print('Pre-Check - Folders Exists ??')
sub_folder_list = ['Apple_Img_Binaries','Screenshot','Video','Whatsapp','Screen_Record']
for sub_folder in sub_folder_list:
    try:
        os.makedirs('./100APPLE/'+str(sub_folder))
        print("==> Created new folder "+str(sub_folder))
    except:
        print("Folders "+str(sub_folder)+" already exist")
pause = raw_input('Start Processing ? ')

whatsapp_img = 0
screen_rec = 0
screehshot = 0
apple_img_bin = 0
video = 0
images = 0
dir_list = os.listdir('./100APPLE/')
for file in dir_list : 
    if str(file).startswith('IMG'):
        if str(file).endswith('PNG'):
            try:
                shutil.move('./100APPLE/'+str(file),'./100APPLE/Screenshot')
                screehshot = screehshot+1
                print("Screenshot -> "+file)
            except:
                os.remove('./100APPLE/'+str(file))
        elif str(file).endswith('AAE') :
            try:
                shutil.move('./100APPLE/'+str(file),'./100APPLE/Apple_Img_Binaries')
                apple_img_bin=apple_img_bin+1
                print("Apple Img Bin ->"+file)
            except:
                os.remove('./100APPLE/'+str(file))
        elif str(file).endswith('MOV') :
            try:
                shutil.move('./100APPLE/'+str(file),'./100APPLE/Video')
                video=video+1
                print("Videos ->"+file)
            except:
                os.remove('./100APPLE/'+str(file))
        else :
            images=images+1
            print("Images ->"+file)

    else:
        if str(file).endswith('JPG') :
            try:
                shutil.move('./100APPLE/'+str(file),'./100APPLE/Whatsapp')
                whatsapp_img=whatsapp_img+1
                print("Whatsapp ->"+file)
            except:
                os.remove('./100APPLE/'+str(file))
        elif str(file).endswith('MP4') :
            try:
                shutil.move('./100APPLE/'+str(file),'./100APPLE/Screen_Record')
                screen_rec=screen_rec+1
                print("Screen Recordings ->"+file)
            except:
                os.remove('./100APPLE/'+str(file))
        elif str(file).endswith('AAE') :
            try:
                shutil.move('./100APPLE/'+str(file),'./100APPLE/Apple_Img_Binaries')
                apple_img_bin=apple_img_bin+1
                print("Apple Img Bin ->"+file)
            except:
                os.remove('./100APPLE/'+str(file))

try:
    file = open("Img_Count_Log.txt","r").read()
    img_count = int(file)
except:
    img_count = 0

new_images = images - img_count
log = """
\n\n\n Date : """ + str(datetime.datetime.now()) + """\n
================================================================
Moved """+str(whatsapp_img)+""" files to whatsapp folder
Moved """+str(screen_rec)+""" files to Screen Record folder
Moved """+str(screehshot)+""" files to screenshot folder
Moved """+str(apple_img_bin)+""" files to Apple Binary Folder
Moved """+str(video)+""" files to Videos
New Image Files : """+ str(new_images) +"""
================================================================
"""
print(log)

file = open("Img_Count_Log.txt","w")
file.write(str(images))
file.close()

file = open("Log.txt","a")
file.write(str(log))
file.close()

pause = raw_input('')
