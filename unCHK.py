import filetype
import glob
import os

path =  os.path.dirname(__file__)
new_folder = path + "/recovery"

if not os.path.exists(new_folder):
       os.mkdir(new_folder)

def chk(file):
    kind = filetype.guess(file)
    if kind is None:
        print('Cannot guess file type!')
        os.remove(file)
        return


    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)
    print( file.split(".CHK")[0])
    new_name = file.split(".CHK")[0]+"."+kind.extension
    # os.rename(file, file.split(".CHK")[0]+"."+kind.extension)
    os.rename(file, os.path.join(new_folder, new_name))


cwd = os.getcwd()
mylist = [os.path.join(cwd, f) for f in os.listdir(cwd) if 
os.path.isfile(os.path.join(cwd, f))]
# print(mylist) 


# mylist = [f for f in glob.glob("*.CHK")]
for file in mylist:
   print(chk(file))
