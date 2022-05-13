import os


token=input('INPUT TOKEN : ')
open('.token.txt','w').write(token)
os.system('python Ultimate.py')
