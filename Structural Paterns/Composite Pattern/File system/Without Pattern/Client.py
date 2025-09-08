from File import File
from Directory import Directory

file1 = File("file1.txt", 100)
file2 = File("file2.txt", 200)
dir1 = Directory("dir1")
dir1.add_file(file1)
dir1.add_file(file2)
file3 = File("file3.txt", 300)
dir2 = Directory("dir2")
dir2.add_file(file3)
print(dir1.get_details())
print(dir2.get_details())