from calendar import firstweekday
from django.contrib.auth.models import User

def edit_user(id,first_name,last_name,email,username,password):
    user = User.objects.get(id = id)
    user.first_name=first_name
    user.last_name=last_name
    user.email=email
    user.username=username
    user.set_password(password)
    user.save()

def create_user(first_name,last_name,email,username,password):
    user=User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    user.save()
