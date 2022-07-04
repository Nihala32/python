from blog_app.models import users,posts

# username
# password

session={}

def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("you must login")
    return wrapper


def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user=[user for user in users if user["username"]==username and user["password"]==password]
    return user


class SignInView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            print("login successful")
            session["user"]=user[0]
        else:
            print("invalid")

class PostView:
    @signin_required
    def get(self,*args,**kwargs):
        return posts
    @signin_required
    def post(self,*args,**kwargs):
        userid=session["user"]["id"]
        kwargs["userid"]=userid
        posts.append(kwargs)
        print(posts)

class MyPostListView:
    @signin_required
    def get(self,*args,**kwargs):
        userid=session["user"]["id"]
        print(userid)
        my_post=[post for post in posts if post["userId"]==userid]
        return my_post

class PostDetailsView:
    def get_object(self,id):
        post=[post for post in posts if post["postId"]==id]
        return post
    @signin_required
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        post=self.get_object(post_id)
        return post
    @signin_required
    def delete(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=self.get_object(post_id)
        if data:
            post=data[0]
            posts.remove(post)
            print("post removed")
            print(len(posts))
    @signin_required
    def put(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=kwargs.get("data")
        instance=self.get_object(post_id)
        if instance:
            post_obj=instance[0]
            post_obj.update(data)
            return post_obj

class LikeView:
    @signin_required
    def get(self,*args,**kwargs):
        post_id=kwargs.get("postId")
        post=[post for post in posts if post["postId"]==post_id]
        if post:
            post=post[0]
            user_id=session["user"]["id"]
            post["liked_by"].append(user_id)
            print(post["liked_by"])




log=SignInView()
log.post(username="richard",password="Password@123")
# print(session)

# data={
#     "title":"my post"
# }
#
# post_detail=PostDetailsView()
# print(post_detail.put(post_id=4,data=data))

# like=LikeView()
# like.get(postId=6)


#
mypost=MyPostListView()
print(mypost.get())
#
# post_details=PostDetailsView()
# post_details.delete(post_id=6)
# print(post_details.get(post_id=6))

# data=PostView()
# # print(data.get())
# data.post(postid="9",
#           title="hello there",
#           content="content",
#           liked_by=[])
#
# #





