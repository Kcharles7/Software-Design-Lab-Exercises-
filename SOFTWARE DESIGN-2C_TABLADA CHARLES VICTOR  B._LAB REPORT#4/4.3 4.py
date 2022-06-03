import os


def find(path, filename):
    if os.path.isdir(path):
        for obj in os.listdir(path):
            if os.path.isdir(os.path.join(path, obj)):
                find(os.path.join(path, obj), filename)
            elif obj == filename:
                print(os.path.join(path, obj))


find(r'SampleFiles/Ch4FileStructure', 'target.txt')
