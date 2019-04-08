[编程题] 汽水瓶
时间限制：1秒

空间限制：32768K

有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？”答案是5瓶，方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，这时候剩2个空瓶子。然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？ 

输入描述:
输入文件最多包含10组测试数据，每个数据占一行，仅包含一个正整数n（1<=n<=100），表示小张手上的空汽水瓶数。n=0表示输入结束，你的程序不应当处理这一行。


输出描述:
对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。


输入例子1:
3
10
81
0

输出例子1:
1
5
40


import sys
 
def cal_nums(num,total):
    count = num
    if count > 3:
        total = total + num//3        # total 表示目前为止喝了多少个
        count = num//3 + num%3        #count = 空瓶子数
        return cal_nums(count,total)
    if count == 3:
        total = total + 1
        return total
    if count == 2:
        total = total + 1
        return total
    if count == 1:
        return total
 
 
for line in sys.stdin:
    total = 0
    if line == "0":
        break
    num = int(line)
    result = cal_nums(num,total)
    print(result)
         
