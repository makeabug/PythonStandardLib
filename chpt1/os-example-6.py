import os

os.makedirs("samples/test/level2/tmp")

fp = open("samples/test/level2/tmp/file", "w")
fp.write("inspector praline")
fp.close()

os.remove("samples/test/level2/tmp/file")
os.removedirs("samples/test/level2/tmp")
