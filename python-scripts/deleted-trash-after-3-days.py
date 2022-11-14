import os
import time

path = "/home/alessandro/Scaricati/"
os.chdir(path)

date_before_delete = int( time.time() ) - (3600*48)
print(date_before_delete)

for file in os.listdir(path):

    lastmod = int( os.path.getmtime(file) )
    if ( lastmod < date_before_delete ) :
        os.remove(file) 
        print( file, ":", lastmod)