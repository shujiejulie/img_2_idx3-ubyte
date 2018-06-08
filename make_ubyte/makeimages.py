# _*_ coding:utf8 _*_


from PIL import Image
import struct
import os
from make_ubyte import makelabels


def get_num(labels_list, img_dir):
    '''
    Get num, rows and columns
    :return: A list including num, rows and columns
    '''
    img_subdir = img_dir + '\\' + str(labels_list[0])
    imglist = os.listdir(img_subdir)
    aImg = Image.open(img_subdir + '\\' + imglist[0]).convert('L')

    num = len(labels_list) * len(imglist)
    rows = aImg.size[1]
    columns = aImg.size[0]

    list = []
    list.append(num)
    list.append(rows)
    list.append(columns)

    return list


def readImage(imgU_name, labels_list, img_dir, num, rows, columns):

    file = open(imgU_name, "wb")
    file.write(struct.pack('>I', 2051))
    file.write(struct.pack('>I', num))
    file.write(struct.pack('>I', rows))
    file.write(struct.pack('>I', columns))
    for i in xrange(len(labels_list)):
        img_subdir = img_dir + '\\' + str(labels_list[i])
        imglist = os.listdir(img_subdir)
        imglist.sort()
        for n in xrange(len(imglist)):
            imgD = Image.open(img_subdir + '\\' + imglist[n]).convert('L')

            for j in xrange(rows):
                for k in xrange(columns):
                    file.write(struct.pack('>B', imgD.getpixel((k, j))))

    file.close()
    print("create " + imgU_name + " success")
