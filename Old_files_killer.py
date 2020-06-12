import os
import time

DAYS = 1                                   # older will be deleted
FOLDERS = [
    r'C:\Users\user\MyPython\Trash',
    r'C:\Users\user\MyPython\Trash2'
]

TOTAL_DELETED_SIZE = 0
TOTAL_DELETED_FILES = 0
TOTAL_DELETED_DIRS = 0

nowTime = time.time()                                   # current time in secs
ageTime = nowTime - 60 * 60 * 24 * DAYS

def delete_old_files(folder):
    global TOTAL_DELETED_FILES
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file)         # full path to file
            fileTime = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile          # count summ of deleted files
                TOTAL_DELETED_FILES += 1                # count number of deleted files
                print('Deleting file: ' + str(fileName))
                os.remove(fileName)                     # remove file

def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    for path, dirs, files in os.walk(folder):
        if not dirs and not files:
            TOTAL_DELETED_DIRS += 1
            print('Deliting empty dir: ' + str(path))
            os.rmdir(path)


start_time = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder)
    delete_empty_dir(folder)

finish_time = time.asctime()

print('Start time: ' + str(start_time))
print('Total deleted size: ' + str(int(TOTAL_DELETED_SIZE / 1024 / 1024)) + 'MB')
print('Total deleted files: ' + str(TOTAL_DELETED_FILES))
print('Total deleted empty folders: ' + str(TOTAL_DELETED_DIRS))
print('Finish time: ' + str(finish_time))
