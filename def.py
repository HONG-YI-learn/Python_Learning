def caculate_BMI(user_hight , user_weight) :
    BMI = user_weight / (user_hight) ** 2
    if BMI <= 18:
        category = "偏瘦"
    elif BMI <= 23.9:
        category = "正常"
    elif BMI <= 30:
        category = "偏胖"
    print(f"您的BMI分类为{category}")
    return BMI

user_hight = float(input("请输入您的身高（单位为m）："))
user_weight = float(input("请输入您的体重（单位为kg）："))
print("您的BMI为" + str(caculate_BMI(user_hight , user_weight)))