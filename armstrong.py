import os.path
path = "./strong.txt"
num = 0
data = []
for i in range(0, 400):
    num = num + 1
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp%10
        sum += digit**order
        temp //= 10
    if num == sum:
        print(num,"yes")
        data.append(num)
    else:
        pass
if os.path.isfile(path):
    print("data already exist, appending to it.")
    with open('strong.txt', 'a+') as f:
       f.write("this part is still in devlopment") 

else:
    print("creating file, strong.txt")
    with open ('strong.txt', 'w') as f:
        for line in data:
            f.write(str(line))
            f.write('\n')
print(data)