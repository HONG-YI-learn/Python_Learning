class Students:
    def __init__(self , name , student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文": 0 , "数学": 0, "英语": 0}

    def set_grade(self , course , grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"学生{self.name}(学号:{self.student_id} ) 的成绩为: ")
        for course in self.grades:
            print(f"{course}: {self.grades[course]} 分")

hongyi = Students("hongyi" , "P161858")

hongyi.set_grade("数学" , 100)
hongyi.set_grade("语文" , 100)
hongyi.set_grade("英语" , 100)
hongyi.print_grades()
print(hongyi.name)
print(hongyi.student_id)
print(hongyi.grades)