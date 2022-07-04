
from  ecom.models import users,product,carts

def authenticate(*args,**kwargs):
    username=kwargs.get("username")
    email=kwargs.get("email")
    user_data=[user for user in users if user["username"]==username and user["email"]==email]
    return user_data

session={}

def login_required(fn):
    def wrapped(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("you must login")
    return wrapped


class SigninView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        email=kwargs.get("email")
        user=authenticate(username=username,email=email)
        if user:
            print("login successful")
            session["user"]=username
        else:
            print("invalid credentials")

@login_required
def logout(*args,**kwargs):
    session.pop("user")

class CartListView:
    @login_required
    def get(self,*args,**kwargs):
        return carts

class ProductListView:
    @login_required
    def get(self,*args,**kwargs):
        return product

class MyCartView:
    @login_required
    def get(self,*args,**kwargs):
        username=session.get("user")

ob=SigninView()
ob.post(username="django",email="django@gmail.com")
cart=CartListView()
all_carts=cart.get()
for c in  all_carts:
    print(c)

product1=ProductListView()
all_products=product1.get()
for p in all_products:
    print(p)