from calendar import firstweekday
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

def edit_user(request,id,first_name,last_name,email,username,password):
    user = User.objects.get(id = id)
    user.first_name=first_name
    user.last_name=last_name
    user.email=email
    user.username=username
    user.set_password(password)
    user.save()
    update_session_auth_hash(request,user)
    


def create_user(first_name,last_name,email,username,password):
    user=User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    user.save()
