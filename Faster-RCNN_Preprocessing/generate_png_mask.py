import os
from PIL import Image

# path is the path of datalab/annotations
def generate(path):
    trimaps_path = path + os.sep + 'trimaps'
    if not os.path.exists(trimaps_path):
        os.makedirs(trimaps_path)
    else:
        for root, dirs, files in os.walk(trimaps_path):
            for name in files:
                os.remove(os.path.join(trimaps_path, name))

    image = Image.new('RGB', (640, 480))
    xmls_path = os.path.join(path, 'xmls')
    for filename in os.listdir(xmls_path):
        filename = os.path.splitext(filename)[0]
        image.save(trimaps_path + os.sep + filename + '.png')


# TODO: use getopt to pass args
generate("D:/Projects/522_test/baseball-bat/annotations")
generate("D:/Projects/522_test/baseball-glove/annotations")
generate("D:/Projects/522_test/baseball-hoop/annotations")
