"""
打印 print 和循环控制 嵌套
"""
rows = int(input("请输入* 的行数: "))
startype = input("请确定* 塔的形式，right， left or all: ")
if startype == "right":
    for i in range(1, rows + 1, 1):
        for j in range(1, i + 1, 1):
            print("*", end="\t")
        print()
elif startype == "left":
    for i in range(1, rows + 1, 1):
        for j in range(1, rows + 1, 1):
            if j < rows - i + 1:
                print(" ", end="\t")
            else:
                print("*", end="\t")
        print()
elif startype == "all":
    for i in range(1, rows + 1, 1):
        for j in range(rows - i + 1, 0, -1):
            print(" ", end="\t")
        for j in range(1, 2 * i, 1):
            print("*", end="\t")
        print()