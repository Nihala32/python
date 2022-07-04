
from blog.models import users,posts

# authenticate
# authenticate(username,password):



def authenticate(*args,**kwargs):
    username=kwargs.get("username")
    email=kwargs.get(("email"))
    user_data=[user for user in users if user["username"]==username and user["email"]==email]
    return user_data

session={}

def login_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("u must login")
    return wrapper

@login_required
def logged_user():
    username = session.get("user")
    user_id = [user["id"] for user in users if user["username"] == username][0]
    return user_id





class SigninView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        email=kwargs.get("email")
        user=authenticate(username=username,email=email)
        if user:
            print("login succussful")
            session["user"]=username
        else:
            print("invalid credentials")


@login_required
def logout(*args,**kwargs):
    session.pop("user")

class PostListView:
    @login_required
    def get(self,*args,**kwargs):
        return posts

class MyPostView:
    @login_required
    def get(self,*args,**kwargs):
        user_id=logged_user()
        qs=[post for post in posts if post["userId"]==user_id]
        return qs

class PostCreateView:
    @login_required
    def post(self,*args,**kwargs):
        user_id=logged_user()
        title=kwargs.get("title")
        body=kwargs.get("body")
        data={
            "userId":user_id,
            "title":title,
            "body":body
        }
        posts.append(data)
        print("post created successfully")

class PostView:
    @login_required
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        qs=[p for p in posts if p.get("id")==post_id]
        return qs
    def put(self,id=None,*args,**kwargs):

        post=[p for p in posts if p.get("id")==id][0]
        title=kwargs.get("title")
        body=kwargs.get("body")
        post["title"]=title
        post["body"]=body
        print(post)






lg=SigninView()
lg.post(username="django",email="django@gmail.com")
#
# pst=PostCreateView()
# pst.post(title="mypost",body="this is my new post")
#
# posts1=MyPostView()
# print(posts1.get())

details=PostView()
print(details.get(post_id=10))
details.put(id=10,title="my post",body="my new post")




#
# pl=PostListView()
# all_posts=pl.get()
#
logout()
print(session)