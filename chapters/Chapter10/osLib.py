import os

filename = "/bin/ls"
os.path.basename(filename)
os.path.dirname(filename)
os.path.split(filename)
os.path.getatime(filename)
os.path.getctime(filename)
os.path.getmtime(filename)
ctimestamp = os.path.getctime(filename)
import time

time.localtime(ctimestamp)
st = time.localtime(ctimestamp)
st.tm_year
st.tm_mon
st.tm_mday
st.tm_wday
st.tm_hour
st.tm_min
st.tm_sec

time.asctime(st)
time.localtime(ctimestamp)
time.gmtime(ctimestamp)

import shutil

spam = open("spam.txt", "a")
spam.write("test")
spam.close()

shutil.copy("spam.txt","spam2")
shutil.move("spam.txt", "someFolder")

os.unlink("spam2")
os.unlink("someFolder")