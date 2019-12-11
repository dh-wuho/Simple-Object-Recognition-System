import os


def normalize_file_name(category, path):
    files = os.listdir(path)
    n = 0
    for i in files:
        oldname = path + os.sep + files[n]
        newfilename = category + '_' + files[n].split('_')[1]
        newname = path + os.sep + newfilename
        os.rename(oldname, newname)
        n += 1


def normalize_dataset(category, path):
    images_path = path + os.sep + 'images'
    xmls_path = path + os.sep + 'annotations' + os.sep + 'xmls'
    normalize_file_name(category, images_path)
    # normalize_file_name(category, xmls_path)


# TODO: use getopt to read args
# first arg is the category name, second arg is the full path of the datalab
# the structure of the datalab is
# datalab
# |-images
# |-anotations
#   |-xmls
normalize_dataset('baseball-hoop', "D:/Projects/522_test/test")
