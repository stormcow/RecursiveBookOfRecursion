import os


def hasEvenByteSize(fullFilePath):
    fileSize = os.path.getsize(fullFilePath)
    return fileSize % 2 == 0


def hasEveryVowel(fullFilePath):
    name = os.path.basename(fullFilePath).lower()
    return (
        ("a" in name)
        and ("e" in name)
        and ("i" in name)
        and ("o" in name)
        and ("u" in name)
    )


def walk(folder, matchFunc):
    matchedFiles = []
    folder = os.path.abspath(folder)

    for name in os.listdir(folder):
        filepath = os.path.join(folder, name)
        if os.path.isfile(filepath):
            if matchFunc(filepath):
                matchedFiles.append(filepath)
        elif os.path.isdir(filepath):
            matchedFiles.extend(walk(filepath, matchFunc))

    return matchedFiles


print("all files with even byte sizes")
print(walk(".", hasEvenByteSize))
print("all files with every vowel in their name")
print(walk(".", hasEveryVowel))
