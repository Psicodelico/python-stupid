from sys import argv

script, filename = argv

target = open(filename, 'r')

print(target.read())

target.close()

print("我们即将清空文件%r"%filename)
print("如果你并不想这样做，按CTRL-C")
print("如果你希望这样做，按Enter")

input("?")

print("正在打开文件...")
target = open(filename, 'w', encoding='utf-8')

print("正在清空文件，再见")
target.truncate()

print("现在我们开始输入三行内容")

line1 = input("第一行：")
line2 = input("第二行：")
line3 = input("第三行：")

print("现在将这些内容写入文件。")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('现在我们关闭文件')
target.close()