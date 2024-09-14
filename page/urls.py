from django.urls import path

from .views import *

urlpatterns=[
    path("",         home,     name="home"),
    path("ajnas/",   ajnas,    name="ajnas"),
    path("ajnas/<str:code>/",jens, name="jens"),
    path("ajnas/<str:code>/buy/",buy,name="buy"),
    path("sharayet/", text,    name="sharayet"),
    path("about/",    aboutme, name="aboutme"),
    path("call/",     callme,  name="callme"),
    path("factor/",   factor,  name="factor"),
    path("pardakht/", pardakht,name="pardakht"),
    path("login/",    login,   name="login"),
    path("sabt/",     signin,  name="sabt"),
]