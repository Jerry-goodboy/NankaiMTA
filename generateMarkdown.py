#!/user/bin/env python
# -*- coding:utf-8 -*-

import os
import platform

currPath = os.getcwd()  # 获取当前路径
print(currPath)

excludeDirs = set(['.git'])

for root, dirs, files in os.walk("d:\\github\\NankaiMTA", topdown=True):
    [dirs.remove(d) for d in list(dirs) if d in excludeDirs]
    # print("根目录：", root)
    # print("文件夹：", dirs)
    # print("文件名：", files)
    for name in files:
        filePath = os.path.join(root, name)
        print(os.path.dirname(filePath))
        finalPath = filePath.replace(currPath, '', 1)
        finalPath = finalPath.replace("\\", "/")
        if finalPath[0] == "/":
            finalPath = finalPath[1:]
        dirNames = finalPath.split("/")
        print(dirNames[len(dirNames) - 2])
        print(finalPath)


