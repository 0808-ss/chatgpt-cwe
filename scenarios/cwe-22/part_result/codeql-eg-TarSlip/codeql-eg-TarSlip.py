import tarfile
import os

# 解压缩 tar 文件到 /tmp/unpack 目录
with tarfile.open("archive.tar.gz", "r:gz") as tar:
    tar.extractall("/tmp/unpack")