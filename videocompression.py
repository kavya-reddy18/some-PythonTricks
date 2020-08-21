import os
os.system("ls ?*.mp4")
file_name=input("Enter video file name : ")
output_filename=input("Enter output filename tto store output : ")
start=input("Enter start time : ")
end=input("Enter end time : ")
qu="ffmpeg -i "+file_name+" -ss "+start+" -to "+end+" -c copy "+output_filename
os.system(qu)
pl="xdg-open "+output_filename
os.system(pl)
