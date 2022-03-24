from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('services/', views.services, name="services"),
    path('register/', views.Register.as_view(), name="register"),
    path('addServices/', views.addServices, name="addServices"),
    path('store/', views.store, name="store"),
    path('updateServices/<int:pk>', views.updateServices, name="updateServices"),
    path('deleteService/<int:pk>', views.deleteService, name="deleteService"),
    path('update/<int:pk>', views.update, name="update"),
    path('about/', views.about, name="about"),

]