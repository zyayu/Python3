def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    print(fs[:])
    return fs


fx = count()  # 这里 是一个list  list 里面的元素是 三个函数
b = fx[0]()
print(fx)
print(b)
f1, f2, f3 = count()
print(f1)
print(f2)
print(f3)
a = f1()
print(f1(), f2(), f3())
