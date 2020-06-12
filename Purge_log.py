import shutil       # for copyfile
import os           # for get filesize and check if file exist
import sys          # for CLI arguments

# Purge_log.py mylog.txt 10 5

if len(sys.argv) < 4:
    print('Missing arguments! Usage is script.py filename.txt 10 5')
    exit(1)

file_name = sys.argv[1]
limit_size = int(sys.argv[2])
logs_number = int(sys.argv[3])


if os.path.isfile(file_name):                   # if logfile exist
    logfile_size = os.stat(file_name).st_size   # get filesize in bytes
    logfile_size = logfile_size / 1024          # convert to kilobytes

    if logfile_size >= limit_size:
        if logs_number > 0:
            for current_file_numb in range(logs_number, 1, -1):
                src = file_name + '_' + str(current_file_numb - 1)
                dst = file_name + '_' + str(current_file_numb)
                if os.path.isfile(src):
                    shutil.copyfile(src, dst)
                    print('Copied: ' + src + ' to ' + dst)

            shutil.copyfile(file_name, file_name + '_1')
            print('Copied: ' + file_name + '  to ' + file_name + '_1')
        myfile = open(file_name, 'w')
        myfile.close()
