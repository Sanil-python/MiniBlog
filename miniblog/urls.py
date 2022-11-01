from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('addblog/', views.addblog, name='addblog'),
    path('updateblog/<int:id>/', views.updateblog, name='updateblog'),
    path('deleteblog/<int:id>/', views.deleteblog, name='deleteblog')
]