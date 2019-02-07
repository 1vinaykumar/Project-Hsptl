from django.urls import path
from .views import register,signin,forgot,home,contact,about,logout,user_base,user_edit,priv_user,priv_edit,book_app,cancel_app,app_show

urlpatterns = [
    path('register',register,name='register'),
    path('signin',signin,name='signin'),
    path('forgot',forgot,name='forgot'),
    path('',home,name='home'),
    path('contact',contact,name='contact'),
    path('about',about,name='about'),
    path('logout',logout,name="logout"),
    path('user',user_base,name="user"),
    path('user_edit',user_edit,name="user_edit"),
    path('priv_user',priv_user,name="priv_user"),
    path('priv_edit',priv_edit,name="priv_edit"),
    path('book_app',book_app,name="book_app"),
    path('cancel_app',cancel_app,name="cancel_app"),
    path('app_show',app_show,name="app_show"),
]
