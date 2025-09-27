from django.urls import path
from . import views

urlpatterns = [
    path('all_logins/', views.all_logins,name="all_logins"),
    path('signup/', views.signup,name="signup"),
    # path('login/', views.handlelogin,name="handlelogin"),
    path('logout/', views.handlelogout,name="handlelogout"),
    path('customer_login/', views.customer_login, name='customer_login'),
    path('login/admin/', views.login_admin, name='login_admin'),
    path('signup/customer/', views.signup_customer, name='signup_customer'),
    path('signup/admin/', views.signup_admin, name='signup_admin'),

]