from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Form1(Form):
    name=CharField(max_length=100,min_length=0,label="Enter your first name")

class Form2(Form):
    username=CharField(max_length=200)
    email=EmailField(max_length=50)
    password=CharField(widget=PasswordInput())

class Form3(Form):
    username=CharField(max_length=200)
    password=CharField(widget=PasswordInput())
