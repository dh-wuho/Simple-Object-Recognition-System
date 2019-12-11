import os


def generate(category, path):
    filepath = path + os.sep + 'label_map.pbtxt'
    with open(filepath, 'w') as file:
        file.write("item {\n id: 1\n name: '" + category + "'\n}")


# TODO: use getopt to pass in args
# the path of label_map.pbtxt is datalab/label_map.pbtxt
generate('blimp', "D:/Projects/522_test")
