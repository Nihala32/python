def admin_permission_required(fn):
    def inner_fun(*args,**kwargs):
        user=kwargs.get("user")
        if user.role!="admin":
            raise Exception("permission denied")
        else:
            return fn(*args,**kwargs)
    return inner_fun


class User:

    def set_user(self,username,role):
        self.usernane=username
        self.role=role
    def print_details(self):
        print(self.usernane,self.role)

class AddCourse:
    @admin_permission_required
    def set_course(self,*args,**kwargs):
        self.user=kwargs.get("user")
        self.course_name=kwargs.get("course_name")
    def print_details(self):
        print(self.course_name)

class AddBatch:
    @admin_permission_required
    def set_batch(self,*args,**kwargs):
        self.user=kwargs.get("user")
        self.batch_code=kwargs.get("b_code")
        self.course=kwargs.get("course")
    def print_details(self):
        print(self.batch_code)

user=User()
user.set_user("rahul","admin")

course=AddCourse()
course.set_course(user=user,course_name="django")

batch=AddBatch(user=user,batch_code="aprdj2k22",course=course)

course.print_details()
batch.print_details()