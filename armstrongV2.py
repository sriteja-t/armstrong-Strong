import os.path
import time
st = time.time()
path = './strong.txt'
start = 0
count = 0
if os.path.isfile(path):
    with open('strong.txt', 'r') as f:
        for last_line in f:
            pass
        # lines = f.readlines()
        # print(lines)
        print(last_line)
        start = int(last_line.strip())          
else:
    pass
num = 0
data =[]
# for i in range(start,5000000000):
while True:
    sum_ = 0
    start = start + 1
    num = start
    # print(num)
    order = len(str(num))
    # print(order)
    temp = num
    # print(temp)
    while temp > 0:
        digit = temp%10
        # print(digit)
        sum_ += digit ** order
        temp //= 10
        # print(sum_)
    if num == sum_:
        data.append(num)
        count = count + 1
        print(num,"yes")
    else:
        # print(num,"no")             
        pass
    if count == 1:
        break

if os.path.isfile(path):
    print("file exists")
    with open('strong.txt', 'a') as f:
       for line in data:
        f.write(str(line))
        f.write('\n')
else:
    print("creating file strong.txt")     
    with open('strong.txt', 'w') as f:
        for line in data:
            f.write(str(line))
            f.write('\n')

et = time.time()
tt = et - st
tt = tt/60
print('Execution time:', tt, 'min')
# print(data)