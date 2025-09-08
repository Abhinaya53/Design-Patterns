from FileDataSource import FileDataSource
from EncryptionDecorator import EncryptionDecorator
from CompressionDecorator import CompressionDecorator
from BufferingDecorator import BufferingDecorator

file1 = CompressionDecorator(BufferingDecorator(EncryptionDecorator(FileDataSource())))
file1.write_file("Hello! My name is Abhinaya.")
print(file1.read_file())

file2 = CompressionDecorator(EncryptionDecorator(FileDataSource()))
file2.write_file("Hi. I am Abhi")
print(file2.read_file())