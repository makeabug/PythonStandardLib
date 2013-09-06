import mmap
import os

filename = "../samples/sample.txt"
file = open(filename, "r+")
size = os.path.getsize(filename)
data = mmap.mmap(file.fileno(), size)

print data
print len(data), size

print repr(data[:10]), repr(data[:10])
print repr(data.read(10)), repr(data.read(10))