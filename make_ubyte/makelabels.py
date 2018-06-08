# _*_ coding:utf8 _*_


import struct
import os


def makesLabels(img_dir):
    labels_list = []
    if (os.path.exists(img_dir)):
        # get all files or directoroes under the current directory
        files = os.listdir(img_dir)
        # get the path to all files or directories in the current directory
        for file in files:
            path = os.path.join(img_dir, file)
            # whether directories or not
            if (os.path.isdir(path)):
                labels_list.append(int(file))
        labels_list.sort()
        return labels_list


def readLabel_idx1(labU_name, labels_list, num):
    fileubyte = open(labU_name, "wb")

    fileubyte.write(struct.pack('>I', 2049))
    fileubyte.write(struct.pack('>I', num))

    for i in xrange(num):
        fileubyte.write(struct.pack('>B', labels_list[i]))

    fileubyte.close()

    print("create " + labU_name + " success")
