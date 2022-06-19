from django.contrib.auth.models import User

def get_all_users():
    result = User.objects.all()
    return result.values('id','username')