# _*_ coding:utf8 _*_


import struct
import os


def makesLabels(img_dir):
    labels_list = []
    if (os.path.exists(img_dir)):
        # 获取该目录下的所有文件或文件夹目录
        files = os.listdir(img_dir)
        for file in files:
            # 得到该文件下所有目录的路径
            path = os.path.join(img_dir, file)
            # 判断该路径下是否是文件夹
            if (os.path.isdir(path)):
                labels_list.append(int(file))  # file
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

'''
MMCNNU(6000)专用
def readLabel_idx3(labU_name, labels_list, num):
    fileubyte = open(labU_name, "wb")

    fileubyte.write(struct.pack('>I', 2049))
    fileubyte.write(struct.pack('>I', num*6*2))
    fileubyte.write(struct.pack('>I', 1))
    fileubyte.write(struct.pack('>I', 2))

    c = 0
    for i in xrange(num):
        for j in xrange(6):
            fileubyte.write(struct.pack('>B', labels_list[i]))
            fileubyte.write(struct.pack('>B', j+1))

    print

    fileubyte.close()

    print("create " + labU_name + " success")'''
