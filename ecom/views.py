from ecom.models import users,carts,product

def authenticate(*args,**kwargs):
    username=kwargs.get("username")
    email=kwargs.get("email")
    user_data=[user for user in users if user["username"]==username]
    return user_data

session={}

def login_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("you must login")
    return wrapper


class SigninView:
    def post(self,*args,**kwargs):
        username = kwargs.get("username")
        email = kwargs.get("email")
        user=authenticate(username=username,email=email)
        if user:
            print("login successfull")
            session["user"]=username
        else:
            print("invalid credentials")


@login_required
def logout(*args,**kwargs):
    session.pop("user")





lg=SigninView()
lg.post(username="django",email="django@gmail.com")

logout()
print(session)