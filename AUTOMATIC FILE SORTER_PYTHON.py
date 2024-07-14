import os, shutil
path = r"D:/SCANNED COPIES"
filename = os.listdir(path)

foldernames = ['csv files', 'iamge files', 'text files']

for loop in range(0,3):
    if not os.path.exists(path + foldernames[loop]):
        print(path + foldernames[loop])
        os.makedirs(path + foldernames[loop])

for file in filename:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        print(shutil.move(path +file, path + "csv files/" + file))
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        print(shutil.move(path +file, path + "image files/" + file))
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        print(shutil.move(path +file, path + "text files/" + file))
    else:
        print("this file type is not included")