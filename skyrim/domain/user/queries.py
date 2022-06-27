from django.contrib.auth.models import User

def get_all_users():
    result = User.objects.all()
    return result.values('id','username','email')

def get_user(user_id):
    result = User.objects.filter(id = user_id)
    return result.values('username','email','last_name','first_name')[0]

def email_exist(email):
    return  User.objects.filter(email=email).exists()

def username_exist(username):
    return  User.objects.filter(username = username).exists()  