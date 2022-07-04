class Course:
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")
    def __str__(self):
        return self.course_name



class Batch:
    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")
    def __str__(self):
        return self.batch_code


class Student:
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.email=kwargs.get("email")
        self.batch=kwargs.get("batch")
    def __str__(self):
        return self.student_name



django=Course()
django.add_course(course_name="django",status=True)

djb1=Batch()
djb1.add_batch(course=django,batch_code="djb12k22",start_date="12-5-2022")
# print(djb1)
# print(djb1.course)
# print(djb1.course.status)

rahul=Student()
rahul.add_student(student_name="rahul",email="rahul@gmail.com",batch=djb1)

akhil=Student()
akhil.add_student(student_name="akhil",email="akhil@gmail.com",batch=djb1)


ms=Course()
ms.add_course(course_name="meanstack",status=True)

ms1=Batch()
ms1.add_batch(course=ms,batch_code="ms2k22",start_date="10-5-2022")

vinay=Student()
vinay.add_student(student_name="vinay",email="vinay@gmail.com",batch=ms1)




students=[]
students.append(vinay)
students.append(akhil)
students.append(rahul)
# for i in students:
#         print(i)

# ms2=[stud for stud in students if stud.batch.course.course_name=="meanstack"]
# for stud in ms2:
#     print(stud)

ms2=[stud.student_name for stud in students if stud.batch.course.course_name=="meanstack"]
print(ms2)

