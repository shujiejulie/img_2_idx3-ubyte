# _*_ coding:utf8 _*_

# #####################################################################
# 将图片数据库转化为与mnsit数据库格式相同的（.idx3-ubyte，.idx1-ubyte）文件
# 方便后续实验操作
# 注意图片数据库格式：
# 根目录
#   |___子目录1（目录名为标签值）
#           |____图片1
#           |____图片2
#           ...
#   ...
# #####################################################################

import getopt, sys
from make_ubyte import makelabels, makeimages


def usage():
    print "\tUsage:%s [--help|--img_dir|--name] args...." % (sys.argv[0])
    print "\t[--img_dir] : Original images storage path"
    print '\t[--name] : The name of the "idx3-ubyte" file'

if __name__ == '__main__':

    try:
        paramDict = {}
        shortargs = '-h'
        longargs = ['help', 'img_dir=', 'name=']
        opts, args = getopt.getopt(sys.argv[1:], shortargs, longargs)
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                usage()
                sys.exit(1)
            else:
                paramDict[opt] = arg

        labels_list = makelabels.makesLabels(paramDict['--img_dir'])
        number_list = makeimages.get_num_idx3lab(labels_list, paramDict['--img_dir'])

        makelabels.readLabel_idx1(paramDict['--name'] + '.idx1-ubyte',
                                  labels_list,
                                  len(labels_list))
        makeimages.readImage(paramDict['--name'] + '.idx3-ubyte',
                             labels_list,
                             paramDict['--img_dir'],
                             number_list[0],
                             number_list[1],
                             number_list[2])
        '''
        MMCBNU(6000)专用
        makelabels.readLabel_idx3(paramDict['--name'] + 'labels.idx3-ubyte',
                             labels_list,
                             len(labels_list))

        makeimages.readImage_idx3lab(paramDict['--name'] + 'data.idx3-ubyte',
                             labels_list,
                             paramDict['--img_dir'],
                             number_list[0],
                             number_list[1],
                             number_list[2])
        '''

    except getopt.GetoptError:
        print 'getopt error!'
        usage()
        sys.exit(1)

