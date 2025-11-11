user_hight = float(input("请输入您的身高（单位为m）："))
user_weight = float(input("请输入您的体重（单位为kg）："))
BMI = user_weight / (user_hight) ** 2
print("您的BMI为：" + str(BMI))