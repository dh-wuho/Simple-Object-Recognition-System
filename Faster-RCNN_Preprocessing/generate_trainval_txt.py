import os


# path is the path of datalab
def generate(path):
    images_path = path + os.sep + 'images'
    trainval_path = path + os.sep + 'annotations' + os.sep + 'trainval.txt'
    images_files = os.listdir(images_path)
    im_files = [x.split('.')[0] for x in images_files]
    with open(trainval_path, 'w') as file:
        for row in im_files:
            file.write(row + '\n')


# TODO: use getopt to pass args
generate("D:/Projects/522_test/baseball-bat")
