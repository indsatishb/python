import os

currentFolder=os.listdir(r"C:\Users\Satish\Downloads")
# for root , dirs , file in os.walk(currentFolder):
#     for fl in file:
#         print(os.path.join(root,fl))
for fl in currentFolder:
    print(fl)