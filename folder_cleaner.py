# Importing Libraries
import os
import shutil
import datetime

# Begin
print('Pre-Check - Folders Exists ??')
# List of necessary sub-folders
sub_folder_list = ['Apple_Img_Binaries','Screenshot','Video','Whatsapp','Screen_Record']

# Check if the necessary sub folders exists
for sub_folder in sub_folder_list:
    try:
        os.makedirs('./100APPLE/'+str(sub_folder))
        print("==> Created new folder "+str(sub_folder))
    except:
        print("Folders "+str(sub_folder)+" already exist")

# Start the magic ?
pause = raw_input('Start Processing ? ')
# Exit if donot want to start
# if pause.tolower() in ['n','no']:
#     exit()

# Initializing variables
whatsapp_img = 0
screen_rec = 0
screehshot = 0
apple_img_bin = 0
video = 0
images = 0

# Root Directory where all the images are dumped
dir_list = os.listdir('./100APPLE/')

# Logic for doing what this script is intended to do starts here
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
            #print("Images ->"+file)
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

# If it is a first time run and the Img_Count_Log.txt file doesn't exist
try:
    file = open("Img_Count_Log.txt","r").read()
    img_count = int(file)
except:
    img_count = 0

# Calculating the new images in the main folder
new_images = images - img_count

# Creating a log of current operation
log = """
\n\n Date : """ + str(datetime.datetime.now()) + """\n
================================================================
Moved """+str(whatsapp_img)+""" files to whatsapp folder
Moved """+str(screen_rec)+""" files to Screen Record folder
Moved """+str(screehshot)+""" files to screenshot folder
Moved """+str(apple_img_bin)+""" files to Apple Binary Folder
Moved """+str(video)+""" files to Videos
New Image Files : """+ str(new_images) +"""
================================================================
"""

# Printing log 
print(log)

# Writing the new number of image files after the end of operation in the main folder
file = open("Img_Count_Log.txt","w")
file.write(str(images))
file.close()

# Appending the current opertations to a log file
file = open("Log.txt","a")
file.write(str(log))
file.close()

# Just for freezing the output
pause = raw_input('')