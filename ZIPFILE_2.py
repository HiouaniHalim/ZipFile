# programmer by HALIM HIOUANI

# C:\Users\Halim\Desktop
import zipfile

FILE = 'C:\Users\Hlim\Desktop\TK.zip'
ZIP = zipfile.ZipFile(FILE, 'r')
for ALL in ZIP.namelist():
    print(ALL)
