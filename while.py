total = 0
count = 0
userinput = input("请输入数字，输入q结束")
while userinput != "q":
    num = float(userinput)
    total += num
    count += 1
    userinput = input("请输入数字，输入q结束")
if total != 0 :
    average = total / count
    print(average)
else:
    print(0)

