# Register your models here.
from django.contrib import admin
from .models import Participant, FormModel, FormField



admin.site.register(Participant)
admin.site.register(FormModel)
admin.site.register(FormField)


# from django.contrib.auth.models import User
#
# User.objects.create_superuser(
#    username='admi', email='admin@exampe.com', password='password'
# )
#
# User.objects.create_user(
#    username='use', email='user@exampe.com', password='NotSecRetAtAll'
# )