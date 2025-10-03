from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('all_logins/', views.all_logins,name="all_logins"),
    path('logout/', views.handlelogout,name="handlelogout"),
    path('customer_login/', views.customer_login, name='customer_login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('signup_customer/', views.signup_customer, name='signup_customer'),
    path('signup_admin/', views.signup_admin, name='signup_admin'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)