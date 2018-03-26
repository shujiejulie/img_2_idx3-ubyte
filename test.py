# _*_ coding:utf8 _*_

import os
from PIL import Image
import numpy as np
from make_ubyte import makelabels

# #######################################################
# 修改FERET数据库格式以满足需求
# img_dir = 'E:\python_code\FERET'
# labels_list = makelabels.makesLabels(img_dir)
# for i in xrange(len(labels_list)):
#     img_subdir = img_dir + '\\' + str(labels_list[i])
#     os.remove(img_subdir + '\\Thumbs.db')
# imglist = os.listdir(img_subdir)
# imglist.sort()
# print imglist
# #######################################################

# #######################################################
# 修改MMCBNU(6000)数据库格式以满足需求
# img_dir = 'E:\\python_code\\MMCBNU(6000)'
# labels_list = makelabels.makesLabels(img_dir)
# print labels_list
# for i in xrange(len(labels_list)):
#     name = ''
#     for j in xrange(len(labels_list[i])):
#         if int(labels_list[i][j]) == 0 and name == '':
#             continue
#         name += labels_list[i][j]
#
#     sub_dir = img_dir + '\\' + labels_list[i]
#     sub_list = makelabels.makesLabels(sub_dir)
#     print sub_list
#     for n in xrange(len(sub_list)):
#         if sub_list[n] == 'L_Fore':
#             os.rename(sub_dir + '\\' + sub_list[n], sub_dir + '\\' + '1')
#         elif sub_list[n] == 'L_Middle':
#             os.rename(sub_dir + '\\' + sub_list[n], sub_dir + '\\' + '2')
#         elif sub_list[n] == 'L_Ring':
#             os.rename(sub_dir + '\\' + sub_list[n], sub_dir + '\\' + '3')
#         elif sub_list[n] == 'R_Fore':
#             os.rename(sub_dir + '\\' + sub_list[n], sub_dir + '\\' + '4')
#         elif sub_list[n] == 'R_Middle':
#             os.rename(sub_dir + '\\' + sub_list[n], sub_dir + '\\' + '5')
#         elif sub_list[n] == 'R_Ring':
#             os.rename(sub_dir + '\\' + sub_list[n], sub_dir + '\\' + '6')
#
#     os.rename(img_dir + '\\' + labels_list[i], img_dir + '\\' + name)
#
# #######################################################

# #################################################################
# 测试对照已转存的数据库
# img = Image.open('E:\\python_code\\FERET\\1\\1.pgm').convert('L')
# img.show()
# matrix = np.asarray(img)
# print matrix.shape
# #################################################################