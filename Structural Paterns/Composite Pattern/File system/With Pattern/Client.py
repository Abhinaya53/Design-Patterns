from File import File
from Directory import Directory

file1 = File("file1.txt", 100)
file2 = File("file2.txt", 200)

dir1 = Directory("dir1")
dir1.add_component(file1)
dir1.add_component(file2)

file3 = File("file3.txt", 300)

dir2 = Directory("dir2")
dir2.add_component(file3)

root = Directory("root")
root.add_component(dir1)
root.add_component(dir2)
print(root.get_details())