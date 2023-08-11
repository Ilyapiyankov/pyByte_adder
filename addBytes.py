import os


def AddData(filename, to_add):
    try:

        f = open(filename, "rb").read()

        n = to_add.toBites()

        with open(filename, "wb") as file:
            file.write(f + '\n'.encode() + b'0' * n)

        return 0

    except PermissionError:
        return 1

class data:
    def __init__(self, type_fo_data, size):
        self.type_fo_data = type_fo_data
        self.size = size

    def toBites(self):
        if self.type_fo_data == "1":
            return self.size
        elif self.type_fo_data == '2':
            return self.size * 8
        elif self.type_fo_data == '3':
            return self.size * 8 * 1024
        else:
            return self.size * 8 * 1024 * 1024


words = ['bits', 'bytes', 'kilobytes', 'megabytes']

print("Hello from byteAdder.py\n")

typeOfData = ''

while len(typeOfData) > len(str(len(words) - 1)) or (not typeOfData in [str(i) for i in range(len(words))]):
    print("Enter type of data to add to file:")
    for i in range(len(words)):
        print(f'{i}. {words[i]}')
    typeOfData = input(">>>>")

typeOfData = int(typeOfData)

files = [i for i in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(i))]

while True:
    print("Select the file from the list to which you want to add data:")

    for i in range(len(files)):
        print(f'{i}. {files[i]} ')

    selectedFile = input(">>>>")

    while (not selectedFile.isalnum()) or (
            selectedFile.isalnum() and (int(selectedFile) > len(files) or int(selectedFile) < 0)):
        selectedFile = input("Incorrect input. Type again.\n>>>>")

    if input(f'All correct and your file is {files[int(selectedFile)]}?\ny/n\n>>>>').lower() == 'y':
        selectedFile = files[int(selectedFile)]
        break

size = input(f"enter number of {words[typeOfData]} to add to {selectedFile}'\n>>>>")

to_add = data(typeOfData, size)

if AddData(selectedFile, to_add) == 1:
    print("No permission")
else:
    print('ok')


