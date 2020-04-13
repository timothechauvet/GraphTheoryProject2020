import os

array2D = []

os.chdir("C:\\Users\\lasagne\\OneDrive - Efrei\\EF - Mathématiques\\S6 - Graph theory\\Project")


with open("test.csv", 'r') as f:
    for line in f.readlines():
        array2D.append(line.split(';'))

print(array2D)