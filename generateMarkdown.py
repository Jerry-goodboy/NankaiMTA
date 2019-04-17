#!/user/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liucaidong'

import os
import os.path

excludeFiles = set(['.DS_Store'])


seq = []


def dfs_showdir(path, depth, dirName, seq):
    global href
    fo = open("README.md", "w")
    for item in os.listdir(path):
        if '.git' not in item:
            newitem = path +'/'+ item
            if os.path.isdir(newitem):
                if depth < 3:
                    seq.append("#" * depth + "# " + item)
                elif depth == 3:
                    seq.append("#" * depth + "# 《" + item + "》")
                else:
                    seq.append("  " * (depth - 4) + "- " + item)
                href = item if(dirName == "") else dirName + "/" + item
                dfs_showdir(newitem, depth +1, href, seq)
            elif os.path.isfile(newitem):
                if item not in excludeFiles and depth > 1:
                    seq.append("  " * (depth - 4) + '- <a href="' + href + '/' + item + '">' + item +'</a>')

    print(seq)
    fo.writelines([line + '\n\n' for line in seq])
    fo.close()


if __name__ == '__main__':
    dfs_showdir(os.getcwd(), 1, "", seq)





# import os
# import platform

# currPath = os.getcwd()  # 获取当前路径
# # print(currPath)

# rawMarkdownTitles = []

# excludeDirs = set(['.git'])
# excludeFiles = set(['.DS_Store'])

# fo = open("test.md", "w")
# seq = []
# fo.writelines([line + '\n' for line in seq])
# fo.close()

# # ['电子书和参考资料', '2019年上学期', '旅游投资与财务管理', '各主题资料', '成本控制主题']

# for root, dirs, files in os.walk(currPath, topdown=True):
#     for d in list(dirs):
#         if d in excludeDirs:
#             dirs.remove(d)
#             files.clear()
#     # print("根目录：", root)
#     print("文件夹：", dirs)
#     # print("文件名：", files)
#     for name in files:
#         filePath = os.path.join(root, name)
#         finalPath = filePath.replace(currPath, '', 1)
#         finalPath = finalPath.replace("\\", "/")
#         if os.name == "posix":
#             finalPath = finalPath[1:]
#         elif os.name == "nt":
#             finalPath = finalPath[1:]
#         dirNames = finalPath.split("/")
#         if dirNames[len(dirNames) - 1] not in excludeFiles:
#             dirNames = dirNames[:len(dirNames) - 1]
#             if dirNames not in rawMarkdownTitles:
#                 rawMarkdownTitles.append(dirNames)
#             else:
#                 pass
#         # print(finalPath)


