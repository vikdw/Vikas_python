import os

file= "/tmp/test_python.txt"

print("testing pythn from jekins pipeline. will create a file in /tmp folder")

if os.path.exists(file):
    print("file already exist, will remove file.")
    os.remove(file)

with open(file, 'w') as f:
    f.write("testing python in jenking with creating this file.")

print("file created please check /tmp folder.   ")
          
          