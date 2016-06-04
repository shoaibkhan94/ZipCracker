'''Author: Shoaib Khan
vErsion:1.0
Website: www.shoaibkhan.in'''
import zipfile
count=0
zip=input("Enter name of passworded protected zip file-> ")
zFile = zipfile.ZipFile(zip)
pass_list=input("Enter name of dictionary file or pass list-> ")
#passFile = open(pass_list)
print('If prog pauses then password is found & file is being extracted. Please Wait!')
with open(pass_list) as r:
    for line in r:
        password = line.strip('\n')
        count+=1
        if count%100==0:
            print(str(count)+" passwords analyzed. current pass -> "+str(password))
        try:
            zFile.extractall(pwd=password.encode())
            print( '[+] Password = ' + password + '\n'+'File Cracked. Enjoy!')
            exit(0)
        except Exception as e:
            pass
