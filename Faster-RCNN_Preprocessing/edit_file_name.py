# import os
#
#
# path = "D:/Projects/522_test/datalab_test/annotations/xmls"
# files = os.listdir(path)
# n = 0
# for i in files:
#     cur_path = path + os.sep + files[n]
#     data = ''
#     with open(cur_path, 'r+') as f:
#         for line in f.readlines():
#             if line.find('<filename>') > 0:
#                 line = '\t<filename>' + files[n].split('.')[0] + '.jpg' + '</filename>' + '\n'
#                 print(line)
#             data += line
#     with open(cur_path, 'r+') as f:
#         f.writelines(data)
#
#     n += 1
#

import os


path = "D:/Projects/522_test/test"
files = os.listdir(path)
test_path = [os.path.join(path, i) for i in files]
print(test_path)
