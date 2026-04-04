import os 
import shutil



src=r"C:\Users\Satish\Downloads"
def FileOrganise(src):
    folders={
    "IMAGES":(".jpg",".png",".gif",".jpeg"),
    "DOCUMENTS":(".pdf",".html",".webp"),
    "VIDEOS":(".mp4",".avi",".flv"),
    "SOFTWARES":(".exe",)
    }
    for folder, extention in folders.items():
        folderPath=os.path.join(src,folder)
        os.makedirs(folderPath, exist_ok=True)
        print("folder Created")

    for file in os.listdir(src):
        filePath=os.path.join(src,file)
        for fl , extentions in folders.items():
            if filePath.lower().endswith(extentions):
                newFile=os.path.join(src,fl,file)
                shutil.move(filePath,newFile)
                

FileOrganise(src)