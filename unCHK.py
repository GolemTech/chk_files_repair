import filetype
import glob
import os

path =  os.path.dirname(__file__)
new_folder = path + "/recovery/Recuperado"
print("hola")


def chk(file):
    kind = filetype.guess(file)
    if kind is None:
        print('Cannot guess file type!')
        os.remove(file)
        return


    print('File : %s' % file)
    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)
    print()
    print()
    print()
    # print( file.split(".msox.zip")[0])
    # new_name = file.split(".CHK")[0]+"."+kind.extension
    # os.rename(file, file.split(".CHK")[0]+"."+kind.extension)

for path,dirs,files in os.walk(new_folder):
    for file in files:
        chk(f'{path}/{file}')
        # print(f'{path}/{file}')
