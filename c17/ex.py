from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("从 %s 复制到 %s" % (from_file, to_file))

in_file = open(from_file, 'r', encoding='utf-8')
indata = in_file.read()

print("文件长度为 %d bytes" % len(indata))

print("输出文件是否存在？%r" % exists(to_file))

print("是否复制文件？RETURN继续，CTRL-C取消")

input()

out_file = open(to_file, 'w', encoding='utf-8')
out_file.write(indata)

print("复制完毕")

out_file.close()
in_file.close()

