#delet
import os
if os.path.exists('text.txt'):
    os.remove('text.txt')
else:
    print("file not exist")
