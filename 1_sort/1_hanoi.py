def hanoi(n, a, b, c):
    '''
    当有 n 个盘子时：
        1. 把 n - 1 个盘子从 A 经过 C 移动到 B
        2. 把第 n 个大盘子从 A 移动到 C
        3. 把 n - 1 个小盘子从 B 经过 A 移动到 C
    :param n: n 个盘子
    :param a: 第一个棍子
    :param b: 第二个棍子
    :param c: 第三个棍子
    '''
    if n > 0:
        hanoi(n-1, a, c, b)
        print('moving from %s to %s' % (a, c))
        hanoi(n-1, b, a, c)

hanoi(4, 'A', 'B', 'C')