from django.urls import path
from . import views

urlpatterns = [
    path('all_logins/', views.all_logins,name="all_logins"),
    path('signup/', views.signup,name="signup"),
    path('login/', views.handlelogin,name="handlelogin"),
    path('logout/', views.handlelogout,name="handlelogout")

]