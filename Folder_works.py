import os
import time

path = os.walk("C:\\Users\lion7\Downloads")
spisok= []

for adres, dir, files in path:
    for file in files:
        full = os.path.join(adres, file)
        if '.exe' in full:
            if time.time() - os.path.getctime(full) < 1000000:
                spisok.append(full)

print (spisok)