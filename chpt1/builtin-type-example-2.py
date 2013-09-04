def load(file):
    if isinstance(file, type('')):
        file = open(file, 'rb')
    return file.read()

print len(load('samples/sample.jpg')), 'bytes'
print len(load(open('samples/sample.jpg', 'rb'))), 'bytes'