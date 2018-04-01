# C:\Users\Hlim\Desktop
import zipfile
FILE = raw_input('enter your File :')
if zipfile.is_zipfile(FILE):
    print("yes")
else:
    print(zipfile.error)