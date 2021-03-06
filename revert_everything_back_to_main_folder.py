# Importing Libraries
import os
import shutil
import datetime

# List of important sub-folders
sub_folder_list = ['Apple_Img_Binaries','Screenshot','Video','Whatsapp','Screen_Record','Duplicate_Compatible','Only_Compatible']
pause = raw_input('Start Processing ? ')
# Check flag to verify that all folders are empty before deleting them
error = 0

# Logic for doing what this script is intended to do starts here
for sub_folder in sub_folder_list:
    dir_list = os.listdir('./100APPLE/'+str(sub_folder))
    for file in dir_list:
        if file not in sub_folder_list:
            try:
                shutil.move('./100APPLE/'+str(sub_folder)+'/'+str(file),'./100APPLE/')
            except:
                print('')
    try:
        os.rmdir('./100APPLE/'+str(sub_folder))
        print('Deleted '+str(sub_folder)+'!!')
    except:
        pause = raw_input('Please make sure '+sub_folder+' is empty!')
        error = 1

# If everything works as expected, write operation to log file
if error == 0:
    print("It's messy again - just like Apple made it [ I mean the DCIM folder :) ]")
    log = """\n\n
==+ >  The reset command was executed at """+ str(datetime.datetime.now()) 
    file = open("Log.txt","a")
    file.write(log)

# Just a random pause to freeze output
pause=raw_input('')