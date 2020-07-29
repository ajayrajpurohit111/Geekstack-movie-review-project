from django.conf.urls import url
from django.urls import path
from . import views
# from .views import video
app_name='accounts'
urlpatterns = [
        path("register/",views.register,name='register'),
        path("login/",views.login_user,name="login"),
        path("logout/",views.logout_user,name="logout")
]
