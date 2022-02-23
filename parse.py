
import os

if __name__ == '__main__':
    print("================================================================")
    print("=                     Begin parse file                         =")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("================================================================")

    list_files = os.listdir()
    name = ''

    for file in list_files:
        name = file[:-7]
        if os.path.isfile(file) and (file[file.__len__() - 7:]) == ".tar.gz":
            if not os.path.isdir(name):
                os.mkdir(name)
                os.replace(file, name + "/" + file)

    print("================================================================")
    print("=                   Successful parse file                      =")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("================================================================")